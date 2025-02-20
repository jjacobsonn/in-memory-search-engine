import pytest
from fastapi.testclient import TestClient
from api.app import app

@pytest.fixture(scope="module")
def client():
    """Fixture to provide test client."""
    return TestClient(app)

def assert_valid_response(response, expected_status=200):
    """Helper method to validate common response attributes."""
    assert response.status_code == expected_status
    assert response.headers["content-type"].startswith("application/json")

def assert_valid_metadata(data):
    """Verify response contains required metadata fields."""
    assert "execution_time_ms" in data
    assert isinstance(data["execution_time_ms"], float)
    assert data["execution_time_ms"] >= 0

def test_autocomplete_found(client):
    """Test successful autocomplete search."""
    response = client.get("/autocomplete?prefix=co")
    assert_valid_response(response)
    
    data = response.json()
    assert_valid_metadata(data)
    assert "results" in data
    assert any("commit" in result for result in data["results"])
    assert data["query"] == "co"

def test_autocomplete_not_found(client):
    """Test autocomplete with non-matching prefix."""
    response = client.get("/autocomplete?prefix=xyz")
    assert_valid_response(response, 404)
    assert "detail" in response.json()

def test_fuzzy_found(client):
    """Test successful fuzzy search."""
    response = client.get("/fuzzy?query=comit&max_distance=1")
    assert_valid_response(response)
    
    data = response.json()
    assert_valid_metadata(data)
    assert "results" in data
    
    # Check if "commit" is in results (comparing term field)
    matches = [item["term"] for item in data["results"]]
    assert "commit" in matches

def test_fuzzy_not_found(client):
    """Test fuzzy search with no matches."""
    response = client.get("/fuzzy?query=xyzabc&max_distance=1")
    assert_valid_response(response, 404)
    assert "detail" in response.json()

def test_api_performance(client):
    """Test API endpoint performance."""
    import time
    start_time = time.time()
    response = client.get("/autocomplete?prefix=co")
    end_time = time.time()
    
    assert_valid_response(response)
    response_time = (end_time - start_time) * 1000  # Convert to milliseconds
    assert response_time < 100, "API response time exceeded performance threshold"
