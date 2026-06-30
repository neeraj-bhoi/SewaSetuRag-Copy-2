import re
import urllib.parse
from typing import Optional, Tuple, Dict, Any
import httpx
from rapidfuzz import fuzz

# ---------------------------------------------------------------------------
# Venue decorator keywords — stripped from venue names during parsing
# ---------------------------------------------------------------------------
VENUE_DECORATORS = [
    "the wedding place", "wedding place", "banquet hall", "banquet",
    "marriage garden", "marriage hall", "resort", "palace", "vatika",
    "lawn", "garden", "convention centre", "convention center",
    "celebration hall", "party plot", "community hall", "guest house",
    "farm house", "farmhouse",
]

# ---------------------------------------------------------------------------
# Hardcoded dict of famous Chhattisgarh landmarks with coordinates & locality
# ---------------------------------------------------------------------------
LANDMARK_OVERRIDES = {
    "mayfair lake resort": {"lat": 21.1764, "lon": 81.3543, "locality": "Atal Nagar, Raipur"},
    "hyatt raipur": {"lat": 21.2449, "lon": 81.6296, "locality": "Mowa, Raipur"},
    "jharokha": {"lat": 21.1938, "lon": 81.3509, "locality": "Supela, Bhilai"},
    "jharokha the wedding place": {"lat": 21.1938, "lon": 81.3509, "locality": "Supela, Bhilai"},
    "mana camp": {"lat": 21.1827, "lon": 81.7354, "locality": "Mana, Raipur"},
    "hotel hukam's lalit mahal": {"lat": 21.2385, "lon": 81.6961, "locality": "Telibandha, Raipur"},
}

# Filler words stripped before override comparison
_FILLER_WORDS = {"the", "a", "an"}

CLEANUP_PATTERNS = [
    # English prefixes
    r'(?i)^\s*where\s+is\s+',
    r'(?i)^\s*located\s+in\s+',
    # Hindi/Hinglish suffixes
    r'(?i)\s+me\s+aata\s+hai\s*$',
    r'(?i)\s+ke\s+under\s+aata\s+hai\s*$',
    r'(?i)\s+kis\s+gp\s+me\s+hai\s*$',
    # English suffixes
    r'(?i)\s+comes\s+under\s+which\s+gp\s*$',
    r'(?i)\s+located\s+in\s*$',
]


# ===================================================================
# Fix 1 — Venue name parser
# ===================================================================
def parse_venue_and_locality(raw_input: str) -> tuple:
    """
    Separates a branded venue name from its city/locality component.

    Returns (venue_name, locality) where either part may be empty.

    Examples:
      "Jharokha - The Wedding Place, Bhilai" -> ("Jharokha", "Bhilai")
      "Mayfair Lake Resort, Raipur"           -> ("Mayfair Lake Resort", "Raipur")
      "Basna"                                 -> ("", "Basna")
      "Shri Ram Vatika Dhamtari"              -> ("Shri Ram Vatika", "Dhamtari")
    """
    text = raw_input.strip()
    venue_name = ""
    locality = ""

    if "-" in text:
        # Rule 1: Dash present — everything before dash is venue, after last comma is locality
        before_dash = text.split("-")[0].strip()
        venue_name = before_dash
        if "," in text:
            locality = text.rsplit(",", 1)[-1].strip()
        else:
            # No comma — try to extract locality from after the dash
            after_dash = text.split("-", 1)[1].strip()
            # Take the last word of after_dash as locality if it looks like a city
            words_after = after_dash.split()
            if words_after:
                locality = words_after[-1].strip()
    elif "," in text:
        # Rule 2: Comma present, no dash — before last comma is venue, after is locality
        parts = text.rsplit(",", 1)
        venue_name = parts[0].strip()
        locality = parts[1].strip()
    else:
        # Rule 3: No dash, no comma — last word is potential city, rest is venue
        words = text.split()
        if len(words) >= 2:
            venue_name = " ".join(words[:-1])
            locality = words[-1]
        else:
            # Single word — treat entirely as locality
            venue_name = ""
            locality = text

    # Strip decorator keywords from venue name
    venue_name = _strip_decorators(venue_name)

    return (venue_name.strip(), locality.strip())


def _strip_decorators(name: str) -> str:
    """Remove venue decorator phrases from a venue name."""
    cleaned = name
    for decorator in VENUE_DECORATORS:
        # Case-insensitive removal
        pattern = re.compile(re.escape(decorator), re.IGNORECASE)
        cleaned = pattern.sub("", cleaned)
    # Collapse whitespace and strip trailing/leading punctuation
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    cleaned = cleaned.strip(",.!?- ")
    return cleaned


# ===================================================================
# Existing helpers
# ===================================================================
def clean_location_query(location_name: str) -> str:
    """
    Cleans up input queries to strip conversational prefixes and suffixes.
    """
    cleaned = location_name.strip()
    for pattern in CLEANUP_PATTERNS:
        cleaned = re.sub(pattern, '', cleaned)
    # Remove extra spaces and strip trailing/leading punctuation
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    cleaned = cleaned.strip(",.?! ")
    return cleaned


def _normalize_for_override(text: str) -> str:
    """Lowercase, strip punctuation and filler words for override matching."""
    lowered = text.lower()
    # Remove punctuation (dashes, commas, dots, etc.)
    lowered = re.sub(r'[^\w\s]', ' ', lowered)
    # Remove filler words
    tokens = [w for w in lowered.split() if w not in _FILLER_WORDS]
    return " ".join(tokens).strip()


def get_override_coordinates(cleaned_query: str) -> Optional[Dict[str, Any]]:
    """
    Checks if the cleaned query matches any hardcoded landmark override.

    Uses rapidfuzz token_set_ratio with threshold >= 75 for partial matching.
    Returns full override dict (lat, lon, locality) or None.
    """
    normalized_input = _normalize_for_override(cleaned_query)

    best_match_key = None
    best_score = 0.0

    for name, data in LANDMARK_OVERRIDES.items():
        normalized_name = _normalize_for_override(name)
        score = fuzz.token_set_ratio(normalized_input, normalized_name)
        if score >= 75 and score > best_score:
            best_score = score
            best_match_key = name

    if best_match_key:
        data = LANDMARK_OVERRIDES[best_match_key]
        print(f"[GEO] Override Match: '{cleaned_query}' -> '{best_match_key}' "
              f"(score={best_score}) -> lat={data['lat']}, lon={data['lon']}, locality={data['locality']}")
        return data

    return None


async def search_nominatim(query_str: str) -> list:
    """
    Performs standard Nominatim search for India and filters for Chhattisgarh.
    """
    headers = {
        "User-Agent": "SewaSetu-Chatbot",
        "Referer": "https://sewasetu.cgstate.gov.in"
    }
    encoded_query = urllib.parse.quote(f"{query_str}, Chhattisgarh, India")
    url = f"https://nominatim.openstreetmap.org/search?q={encoded_query}&countrycodes=in&addressdetails=1&format=json&limit=5"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, timeout=10.0)
            if response.status_code == 200:
                results = response.json()
                if isinstance(results, list):
                    filtered = []
                    for r in results:
                        addr = r.get("address", {})
                        state = addr.get("state", "")
                        if "chhattisgarh" in state.lower():
                            filtered.append(r)
                    return filtered
    except Exception as e:
        print(f"[Nominatim Search] Error querying '{query_str}': {e}")
    return []


# ===================================================================
# Fix 2 — Cascaded geocoding strategy  (3-attempt + existing fuzzy)
# ===================================================================
async def geocode_location_pipeline(location_name: str) -> Optional[Dict[str, Any]]:
    """
    Runs the full Phase 1 pipeline:
    Cleanup -> Venue Parse -> Overrides -> Attempt 1 (venue+locality)
    -> Attempt 2 (locality only) -> Attempt 3 (existing fuzzy retry)
    """
    cleaned_query = clean_location_query(location_name)
    if not cleaned_query:
        print(f"[GEO] Cleaned query is empty for input '{location_name}'")
        return None

    print(f"[GEO] Original: '{location_name}' | Cleaned: '{cleaned_query}'")

    # ----- Fix 1: Parse venue and locality -----
    venue_name, locality = parse_venue_and_locality(cleaned_query)
    print(f"[GEO] Parsed -> venue_name='{venue_name}', locality='{locality}'")

    # ----- Step: Landmark Overrides (uses full cleaned query + venue name) -----
    override = get_override_coordinates(cleaned_query)
    if not override and venue_name:
        override = get_override_coordinates(venue_name)
    if override:
        return {
            "lat": override["lat"],
            "lon": override["lon"],
            "importance": 1.0,
            "source": "override",
            "venue_resolved": True,
        }

    venue_resolved = True  # assume true; set false if we fall back to locality-only

    # ----- Attempt 1: Venue + Locality combined -----
    if venue_name:
        attempt1_query = f"{venue_name}, {locality}"
        results = await search_nominatim(attempt1_query)
        top_importance = float(results[0].get("importance", 0)) if results else 0.0
        print(f"[GEO] Attempt 1: query='{attempt1_query}', results={len(results)}, "
              f"top_importance={top_importance:.4f}")

        if results and top_importance >= 0.3:
            top_res = results[0]
            try:
                lat = float(top_res["lat"])
                lon = float(top_res["lon"])
                print(f"[GEO] Attempt 1 succeeded: {top_res.get('display_name')}")
                print(f"[GEO] venue_resolved=True, lat={lat}, lon={lon}")
                return {
                    "lat": lat,
                    "lon": lon,
                    "importance": top_importance,
                    "source": "search_venue_locality",
                    "venue_resolved": True,
                }
            except (ValueError, KeyError) as e:
                print(f"[GEO] Attempt 1 parse error: {e}")

    # ----- Attempt 2: Locality only (primary fallback for unknown venues) -----
    if locality:
        results = await search_nominatim(locality)
        top_importance = float(results[0].get("importance", 0)) if results else 0.0
        print(f"[GEO] Attempt 2: query='{locality}', results={len(results)}, "
              f"top_importance={top_importance:.4f}")

        if results:
            top_res = results[0]
            try:
                lat = float(top_res["lat"])
                lon = float(top_res["lon"])
                venue_resolved = False
                print(f"[GEO] Attempt 2 succeeded (locality fallback): {top_res.get('display_name')}")
                print(f"[GEO] venue_resolved=False, lat={lat}, lon={lon}")
                return {
                    "lat": lat,
                    "lon": lon,
                    "importance": top_importance,
                    "source": "search_locality_fallback",
                    "venue_resolved": False,
                    "locality_used": locality,
                }
            except (ValueError, KeyError) as e:
                print(f"[GEO] Attempt 2 parse error: {e}")

    # ----- Attempt 3: Existing fuzzy retry pipeline -----
    print("[GEO] Attempts 1 & 2 failed. Starting fuzzy retry pipeline (Attempt 3)...")

    # Fuzzy sub-attempt A: Simplified query (first + last word)
    words = cleaned_query.split()
    simplified_query = cleaned_query
    if len(words) >= 2:
        simplified_query = f"{words[0]} {words[-1]}"

    results = await search_nominatim(simplified_query)
    top_importance = float(results[0].get("importance", 0)) if results else 0.0
    print(f"[GEO] Attempt 3a: query='{simplified_query}', results={len(results)}, "
          f"top_importance={top_importance:.4f}")

    if results:
        best_match = None
        best_score = -1.0
        for r in results:
            display_name = r.get("display_name", "")
            first_part = display_name.split(",")[0] if display_name else ""
            score = max(
                fuzz.token_sort_ratio(cleaned_query, display_name),
                fuzz.token_sort_ratio(cleaned_query, first_part)
            )
            if score >= 70 and score > best_score:
                best_score = score
                best_match = r

        if best_match:
            try:
                lat = float(best_match["lat"])
                lon = float(best_match["lon"])
                imp = float(best_match.get("importance", 0.40))
                print(f"[GEO] Attempt 3a succeeded (score={best_score}): {best_match.get('display_name')}")
                print(f"[GEO] venue_resolved=True, lat={lat}, lon={lon}")
                return {
                    "lat": lat,
                    "lon": lon,
                    "importance": imp,
                    "source": "fuzzy_retry_simplified",
                    "venue_resolved": True,
                }
            except (ValueError, KeyError):
                pass

    # Fuzzy sub-attempt B: Parent locality query (last 1-2 comma-separated tokens or trailing words)
    if "," in cleaned_query:
        tokens = [t.strip() for t in cleaned_query.split(",") if t.strip()]
        parent_locality = ", ".join(tokens[-2:] if len(tokens) >= 2 else tokens[-1:])
    else:
        if len(words) >= 2:
            parent_locality = " ".join(words[-2:])
        else:
            parent_locality = cleaned_query

    if parent_locality != cleaned_query:
        results = await search_nominatim(parent_locality)
        top_importance = float(results[0].get("importance", 0)) if results else 0.0
        print(f"[GEO] Attempt 3b: query='{parent_locality}', results={len(results)}, "
              f"top_importance={top_importance:.4f}")

        if results:
            top_res = results[0]
            try:
                lat = float(top_res["lat"])
                lon = float(top_res["lon"])
                imp = float(top_res.get("importance", 0.30))
                print(f"[GEO] Attempt 3b succeeded: {top_res.get('display_name')}")
                print(f"[GEO] venue_resolved=False, lat={lat}, lon={lon}")
                return {
                    "lat": lat,
                    "lon": lon,
                    "importance": imp,
                    "source": "fuzzy_retry_parent",
                    "venue_resolved": False,
                    "locality_used": parent_locality,
                }
            except (ValueError, KeyError):
                pass

    print("[GEO] Geocoding pipeline failed to locate coordinates.")
    return None
