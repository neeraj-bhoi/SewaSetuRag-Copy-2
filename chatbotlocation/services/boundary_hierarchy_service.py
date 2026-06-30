import re
import httpx
from typing import Optional, Tuple, Dict, Any, List
from rapidfuzz import fuzz

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

async def reverse_geocode_nominatim(lat: float, lon: float) -> dict:
    """
    Reverse geocodes coordinates at zoom level 10 to extract address details.
    """
    headers = {
        "User-Agent": "SewaSetu-Chatbot",
        "Referer": "https://sewasetu.cgstate.gov.in"
    }
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&zoom=10&addressdetails=1&format=json"
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, headers=headers, timeout=10.0)
            if res.status_code == 200:
                return res.json()
    except Exception as e:
        print(f"[Boundary Overpass] Reverse geocoding failed: {e}")
    return {}

async def query_overpass_is_in(lat: float, lon: float) -> List[Dict[str, Any]]:
    """
    Executes primary enclosing is_in boundary query on Overpass.
    """
    query = f"""[out:json][timeout:25];
is_in({lat},{lon})->.a;
(
  relation(pivot.a)[boundary=administrative];
  way(pivot.a)[boundary=administrative];
);
out tags;"""
    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(OVERPASS_URL, data={"data": query}, timeout=30.0)
            if res.status_code == 200:
                return res.json().get("elements", [])
            else:
                print(f"[Overpass is_in] Non-200 response: {res.status_code}")
    except Exception as e:
        print(f"[Overpass is_in] Connection error: {e}")
    return []

async def query_overpass_around(lat: float, lon: float) -> List[Dict[str, Any]]:
    """
    Executes nearby (5km radius) boundary relation search on Overpass.
    """
    query = f"""[out:json][timeout:25];
relation(around:5000,{lat},{lon})[boundary=administrative];
out tags;"""
    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(OVERPASS_URL, data={"data": query}, timeout=30.0)
            if res.status_code == 200:
                return res.json().get("elements", [])
            else:
                print(f"[Overpass around] Non-200 response: {res.status_code}")
    except Exception as e:
        print(f"[Overpass around] Connection error: {e}")
    return []

def clean_admin_name(name: str) -> str:
    """
    Removes administrative suffixes like 'District', 'Tehsil', etc.
    """
    if not name:
        return ""
    cleaned = name
    cleaned = re.sub(r'(?i)\s+district$', '', cleaned)
    cleaned = re.sub(r'(?i)\s+tehsil$', '', cleaned)
    cleaned = re.sub(r'(?i)\s+block$', '', cleaned)
    return cleaned.strip()

async def extract_boundary_details(lat: float, lon: float) -> Dict[str, Any]:
    """
    Extracts administrative boundaries using Overpass API with nearby and node fallbacks.
    """
    print(f"[Boundary Service] Extracting boundaries for ({lat}, {lon})")
    
    # Pre-fetch reverse geocoding for fallback values and confidence scoring matches
    rev_data = await reverse_geocode_nominatim(lat, lon)
    address = rev_data.get("address", {})
    
    # Establish fallback location hierarchy from address
    reverse_village = (
        address.get("village") or 
        address.get("suburb") or 
        address.get("city_district") or 
        address.get("town") or 
        address.get("municipality") or 
        address.get("neighbourhood") or 
        address.get("county") or
        ""
    )
    
    rev_district = address.get("county") or address.get("state_district") or address.get("district") or "Raipur"
    rev_block = address.get("subdistrict") or address.get("suburb") or address.get("city_district") or address.get("municipality") or address.get("town") or address.get("village") or rev_district
    
    district = clean_admin_name(rev_district)
    block = clean_admin_name(rev_block)
    area = reverse_village

    # 1. Primary Query: enclosing is_in
    elements = await query_overpass_is_in(lat, lon)
    
    valid_enclosing = []
    enclosing_district = None
    enclosing_block = None

    for el in elements:
        tags = el.get("tags", {})
        lvl_str = tags.get("admin_level")
        name = tags.get("name") or tags.get("name:en")
        if not lvl_str or not name:
            continue
        try:
            lvl = int(lvl_str)
            if lvl == 6:
                enclosing_district = clean_admin_name(name)
            elif lvl == 7:
                enclosing_block = clean_admin_name(name)
            valid_enclosing.append((lvl, tags, name))
        except ValueError:
            pass

    # Apply more precise block/district names if found in spatial enclosing borders
    if enclosing_district:
        district = enclosing_district
        print(f"[Boundary Service] Found district enclosing relation: '{district}'")
    if enclosing_block:
        block = enclosing_block
        print(f"[Boundary Service] Found block enclosing relation: '{block}'")

    # Sort enclosing relations ascending by admin_level
    valid_enclosing.sort(key=lambda x: x[0])
    
    # Check for enclosing administrative boundaries with level >= 8
    for lvl, tags, name in valid_enclosing:
        if lvl >= 8:
            print(f"[Boundary Service] Success using enclosing relation: '{name}' (admin_level={lvl})")
            return {
                "resolved_name": name,
                "resolved_tags": tags,
                "admin_level": lvl,
                "method": "enclosing",
                "district": district,
                "block": block,
                "area": area,
                "reverse_village": reverse_village
            }

    # 2. Fallback 1: Nearby boundary search (5 km radius)
    print("[Boundary Service] No enclosing relations >= 8 found. Initiating Fallback 1 (5km around)...")
    around_elements = await query_overpass_around(lat, lon)
    best_nearby = None
    best_score = -1.0

    for el in around_elements:
        tags = el.get("tags", {})
        name = tags.get("name") or tags.get("name:en")
        lvl_str = tags.get("admin_level")
        if not name or not reverse_village:
            continue
        try:
            lvl = int(lvl_str) if lvl_str else 8
        except ValueError:
            lvl = 8
            
        # Compare with Nominatim resolved village/locality name
        score = fuzz.token_sort_ratio(name.lower(), reverse_village.lower())
        if score >= 80 and score > best_score:
            best_score = score
            best_nearby = (name, tags, lvl)

    if best_nearby:
        name, tags, lvl = best_nearby
        print(f"[Boundary Service] Success using Fallback 1 (score={best_score}): '{name}' (admin_level={lvl})")
        return {
            "resolved_name": name,
            "resolved_tags": tags,
            "admin_level": lvl,
            "method": "nearby",
            "district": district,
            "block": block,
            "area": area,
            "reverse_village": reverse_village
        }

    # 3. Fallback 2: Reverse geocode village node
    print("[Boundary Service] Fallback 1 failed. Initiating Fallback 2 (reverse geocode village node)...")
    fallback_name = reverse_village or block or "Unknown Location"
    return {
        "resolved_name": fallback_name,
        "resolved_tags": {},
        "admin_level": 10,
        "method": "reverse_geocode",
        "district": district,
        "block": block,
        "area": area,
        "reverse_village": reverse_village
    }
