import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from chatbotlocation.services.geocoding_service import geocode_location_pipeline
from chatbotlocation.services.boundary_hierarchy_service import extract_boundary_details
from chatbotlocation.services.jurisdiction_classifier import classify_jurisdiction
from chatbotlocation.services.confidence_scorer import score_confidence

app = FastAPI(
    title="SewaSetu Geospatial Resolution Microservice",
    description="Standalone microservice for geocoding and administrative boundary lookup in Chhattisgarh.",
    version="1.0.0"
)

class LocateRequest(BaseModel):
    location_name: str

class LocateResponse(BaseModel):
    body_type: Optional[str] = None
    body_name: Optional[str] = None
    area: Optional[str] = None
    district: Optional[str] = None
    block: Optional[str] = None
    confidence: float
    confidence_level: str
    warning: Optional[str] = None

@app.post("/chatbot/locate", response_model=LocateResponse)
async def locate_endpoint(request: LocateRequest):
    print(f"\n[Microservice Locate] Request received for: '{request.location_name}'")
    
    # Phase 1: Geocoding
    geocode_result = await geocode_location_pipeline(request.location_name)
    if not geocode_result:
        print("[Microservice Locate] Geocoding completely failed.")
        return LocateResponse(
            body_type=None,
            body_name=None,
            area=None,
            district=None,
            block=None,
            confidence=0.0,
            confidence_level="low",
            warning="Low geocoding precision. Verify exact jurisdiction before submitting documents."
        )

    lat = geocode_result["lat"]
    lon = geocode_result["lon"]
    importance = geocode_result["importance"]
    print(f"[Microservice Locate] Coordinates resolved: ({lat}, {lon}) via {geocode_result['source']}")

    # Phase 2: Overpass Boundary Extraction
    boundary_info = await extract_boundary_details(lat, lon)
    
    resolved_name = boundary_info["resolved_name"]
    resolved_tags = boundary_info["resolved_tags"]
    admin_level = boundary_info["admin_level"]
    method = boundary_info["method"]
    district = boundary_info["district"]
    block = boundary_info["block"]
    area = boundary_info["area"]
    reverse_village = boundary_info["reverse_village"]

    # Phase 3: Classification
    body_type, body_name = classify_jurisdiction(resolved_name, resolved_tags, admin_level)

    # Phase 4: Scoring
    venue_resolved = geocode_result.get("venue_resolved", True)
    locality_used = geocode_result.get("locality_used")
    confidence, confidence_level, warning = score_confidence(
        method, body_name, reverse_village, importance,
        venue_resolved=venue_resolved, locality_used=locality_used
    )

    response_payload = LocateResponse(
        body_type=body_type,
        body_name=body_name,
        area=area or "N/A",
        district=district or "N/A",
        block=block or "N/A",
        confidence=confidence,
        confidence_level=confidence_level,
        warning=warning
    )
    print(f"[Microservice Locate] Successfully resolved request: {response_payload.dict()}\n")
    return response_payload

if __name__ == "__main__":
    uvicorn.run("chatbotlocation.main:app", host="127.0.0.1", port=8001)
