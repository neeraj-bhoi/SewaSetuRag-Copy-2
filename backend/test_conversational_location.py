import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock, MagicMock, ANY

# Import the FastAPI app
from backend.main import app

client = TestClient(app)

@pytest.fixture
def mock_llm_helpers():
    """
    Fixture to patch LLM router and async helpers to control test execution.
    """
    with patch("backend.main.detect_query_language") as mock_lang, \
         patch("backend.main.classify_query_intent") as mock_intent, \
         patch("backend.main.classify_service") as mock_class_service, \
         patch("backend.main.run_rag_pipeline", new_callable=AsyncMock) as mock_rag_run, \
         patch("backend.main.run_rag_pipeline_intermediates", new_callable=AsyncMock) as mock_intermediates, \
         patch("backend.main.synthesize_consensus_response", new_callable=AsyncMock) as mock_synthesize:
        
        mock_lang.return_value = "en"
        mock_intent.return_value = "information"
        mock_class_service.return_value = {"sno": "1", "service_id": "3"}
        mock_rag_run.return_value = {"response": "Mocked standard RAG response"}
        
        # Default mock return for intermediates pipeline
        mock_intermediates.return_value = (
            "en",                                    # query_lang
            "query_en",                              # english_query
            "query_hi",                              # hindi_query
            "context_en",                            # context_en
            "context_hi",                            # context_hi
            "Intermediate English RAG response",     # english_answer
            "Intermediate Hindi RAG response",       # hindi_answer
            "Information not available."             # fallback_msg
        )
        
        mock_synthesize.return_value = {"response": "Mocked synthesized response"}
        
        yield {
            "lang": mock_lang,
            "intent": mock_intent,
            "classify": mock_class_service,
            "rag": mock_rag_run,
            "intermediates": mock_intermediates,
            "synthesize": mock_synthesize
        }


def test_marriage_location_intent_triggers_options(mock_llm_helpers):
    """
    Asserts that queries routed to Marriage Registration (sno='1'/service_id=3) 
    that ask about office locations trigger the interactive 2-button choice options.
    """
    mock_llm_helpers["intent"].return_value = "location"
    
    payload = {
        "query": "where to submit marriage certificate for mayfair resort",
        "selected_sno": "1"  # Marriage Registration
    }
    
    response = client.post("/api/chat", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert "options" in data
    assert len(data["options"]) == 2
    assert data["options"][0]["value"] == "flow_location"
    assert data["options"][1]["value"] == "flow_info"
    assert data["original_query"] == "where to submit marriage registration and certificate for mayfair resort"
    assert data["service_id"] == 3


def test_marriage_info_intent_runs_rag_immediately(mock_llm_helpers):
    """
    Asserts that informational queries for Marriage Registration do NOT trigger options
    and immediately execute the RAG pipeline.
    """
    mock_llm_helpers["intent"].return_value = "information"
    
    payload = {
        "query": "what documents are required for marriage registration",
        "selected_sno": "1"
    }
    
    response = client.post("/api/chat", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert "options" not in data
    assert data["response"] == "Mocked standard RAG response"
    mock_llm_helpers["rag"].assert_called_once()


def test_other_service_does_not_trigger_options(mock_llm_helpers):
    """
    Asserts that Caste Certificate queries (sno='2'/service_id=4) do NOT trigger location routing
    even if location keywords are mentioned.
    """
    mock_llm_helpers["classify"].return_value = {"sno": "2", "service_id": "4"}
    mock_llm_helpers["intent"].return_value = "location"  # Even if LLM says location
    
    payload = {
        "query": "where is the office to register OBC Caste certificate",
        "selected_sno": "2"  # Caste certificate serial number
    }
    
    response = client.post("/api/chat", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert "options" not in data
    assert data["response"] == "Mocked standard RAG response"


def test_selecting_flow_info_proceeds_to_rag(mock_llm_helpers):
    """
    Asserts that selecting the 'General Information' button (location_flow='flow_info')
    executes standard RAG on the original query.
    """
    payload = {
        "query": "ℹ️ General Information",
        "selected_sno": "1",
        "location_flow": "flow_info",
        "original_query": "where to register marriage at mayfair resort"
    }
    
    response = client.post("/api/chat", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert "options" not in data
    assert data["response"] == "Mocked standard RAG response"
    mock_llm_helpers["rag"].assert_called_once()
    # Ensure it ran RAG with the original query, not the button text
    args, kwargs = mock_llm_helpers["rag"].call_args
    assert args[0] == payload["original_query"]


@patch("backend.main.geocode_location")
@patch("backend.main.extract_location_from_query")
def test_selecting_flow_location_direct_success(mock_extract, mock_geocode, mock_llm_helpers):
    """
    Asserts that when location_name is provided directly, it is geocoded directly
    bypassing LLM query extraction, and synthesis runs with location details.
    """
    mock_geocode.return_value = {
        "display_name": "Mayfair Lake Resort, Raipur, Chhattisgarh, India",
        "suburb": "Naya Raipur",
        "city": "Raipur",
        "district": "Raipur District",
        "state": "Chhattisgarh",
        "admin_type": "Municipal Corporation",
        "admin_name": "Raipur Municipal Corporation"
    }
    
    mock_extract.return_value = "mayfair resort"
    
    payload = {
        "query": "Mayfair Lake Resort",
        "location_name": "Mayfair Lake Resort",
        "selected_sno": "1",
        "location_flow": "flow_location",
        "original_query": "where to register marriage at mayfair resort"
    }
    
    response = client.post("/api/chat", json=payload)
    assert response.status_code == 200
    
    # Assert extract_location_from_query was called once to parse old venue name
    mock_extract.assert_called_once_with(payload["original_query"])
    
    # Assert geocode_location was called directly with explicit location_name
    mock_geocode.assert_called_once_with("Mayfair Lake Resort")
    
    # Assert run_rag_pipeline was called with replaced query containing new location name and loc_details
    mock_llm_helpers["rag"].assert_called_once_with(
        query="where to register marriage at Mayfair Lake Resort",
        request=ANY,
        service_id=3,
        loc_details=mock_geocode.return_value,
        is_location_flow=True
    )


@patch("backend.main.geocode_location")
@patch("backend.main.extract_location_from_query")
def test_selecting_flow_location_fallback_success(mock_extract, mock_geocode, mock_llm_helpers):
    """
    Asserts that if location_name is missing, backend extracts it using extract_location_from_query
    and geocodes it.
    """
    mock_extract.return_value = "extracted resort"
    mock_geocode.return_value = {
        "display_name": "Extracted Resort Address, Raipur",
        "state": "Chhattisgarh",
        "admin_type": "Municipal Corporation",
        "admin_name": "Raipur Municipal Corporation"
    }
    
    payload = {
        "query": "📍 Find Local Office",
        "selected_sno": "1",
        "location_flow": "flow_location",
        "original_query": "where to register marriage at extracted resort"
    }
    
    response = client.post("/api/chat", json=payload)
    assert response.status_code == 200
    
    # Assert extract_location_from_query was called
    mock_extract.assert_called_once_with(payload["original_query"])
    # Assert geocode_location was called with extracted venue name
    mock_geocode.assert_called_once_with("extracted resort")
    
    # Assert run_rag_pipeline was called with replaced query containing extracted venue and loc_details
    mock_llm_helpers["rag"].assert_called_once_with(
        query="where to register marriage at extracted resort",
        request=ANY,
        service_id=3,
        loc_details=mock_geocode.return_value,
        is_location_flow=True
    )
