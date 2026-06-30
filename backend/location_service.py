import requests
import urllib.parse
import httpx
import inspect
from typing import Dict, Any, Optional, Tuple

class AwaitableDict(dict):
    def __await__(self):
        async def _identity():
            return self
        return _identity().__await__()

class GeocodeLocationWrapper:
    def __call__(self, location_name: str) -> dict:
        """
        Synchronous entry point called by the existing main.py without await.
        """
        print(f"[Location Service] Calling geospatial microservice synchronously: '{location_name}'")
        try:
            with httpx.Client() as client:
                response = client.post(
                    "http://localhost:8001/chatbot/locate",
                    json={"location_name": location_name},
                    timeout=15.0
                )
                if response.status_code == 200:
                    res_json = response.json()
                    print(f"[Location Service] Microservice returned: {res_json}")
                    return AwaitableDict(res_json)
                else:
                    print(f"[Location Service] Microservice returned non-200 status code: {response.status_code}")
        except Exception as e:
            print(f"[Location Service] Microservice lookup failed: {e}")
        return AwaitableDict({})

    async def async_call(self, location_name: str) -> dict:
        """
        Asynchronous fallback in case the function is called or tested asynchronously.
        """
        print(f"[Location Service] Calling geospatial microservice asynchronously: '{location_name}'")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://localhost:8001/chatbot/locate",
                    json={"location_name": location_name},
                    timeout=15.0
                )
                if response.status_code == 200:
                    return response.json()
        except Exception as e:
            print(f"[Location Service] Asynchronous microservice lookup failed: {e}")
        return {}

geocode_location = GeocodeLocationWrapper()
inspect.markcoroutinefunction(geocode_location)


def extract_location_from_query(query: str) -> str:
    """
    Extracts the wedding venue, hotel, landmark, address or location mentioned in the query.
    """
    prompt = (
        "You are an information extraction assistant.\n"
        "Extract the name of the wedding venue, resort, hotel, landmark, address, village, or town "
        "mentioned in the user query that they want to find the registration office for.\n"
        "Return ONLY the extracted name of the location. Do not explain, do not add punctuation, do not output markdown.\n\n"
        f"Query: '{query}'\n"
        "Location:"
    )
    try:
        from backend.llm_router import generate_answer
        res = generate_answer([{"role": "user", "content": prompt}])
        return res.strip()
    except Exception as e:
        print(f"[Location Service] extract_location_from_query failed: {e}")
        return query

def extract_locality_from_query(location_name: str) -> str:
    """
    Extracts the city, town, village, or area/locality portion of the venue name (e.g. from 'Mayfair Lake Resort, Naya Raipur' -> 'Naya Raipur').
    """
    prompt = (
        "You are an information extraction assistant.\n"
        "Extract only the area, suburb, city, town, or village name from the provided location name (e.g. from 'Mayfair Lake Resort, Naya Raipur' extract 'Naya Raipur').\n"
        "Return ONLY the extracted locality name. Do not explain, do not add punctuation, do not output markdown.\n\n"
        f"Location Name: '{location_name}'\n"
        "Locality:"
    )
    try:
        from backend.llm_router import generate_answer
        res = generate_answer([{"role": "user", "content": prompt}])
        return res.strip()
    except Exception as e:
        print(f"[Location Service] extract_locality_from_query failed: {e}")
        return location_name
