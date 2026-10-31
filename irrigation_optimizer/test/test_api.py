"""Automated Pytest suite for the Irrigation Schedule Optimizer API.
Tests the core logic: normal scheduling, rain-skip (Rain Guard), and zero-water skip.
"""

from fastapi.testclient import TestClient
from irrigation_optimizer.main import app

client = TestClient(app)

def test_normal_schedule():
    """Test that 120 minutes splits into two 60-minute slots."""
    response = client.get("/api/schedule/field_1?minutes_needed=120&rain_mm=0")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "SCHEDULED"
    assert len(data["schedule"]) == 2 
    assert data["schedule"][0]["start_time"] == "06:00" #morning slot verificaton
    assert data["schedule"][0]["status"] == "PENDING"

def test_rain_skip():
    """Test that heavy rain skips the irrigation."""
    response = client.get("/api/schedule/field_1?minutes_needed=120&rain_mm=10")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "SKIPPED"
    assert "Rain Guard" in data["reason"]
    assert len(data["schedule"]) == 0

def test_no_water_needed():
    """Test that 0 minutes skips the irrigation."""
    response = client.get("/api/schedule/field_1?minutes_needed=0&rain_mm=0")
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "SKIPPED"
    assert "Soil moisture is sufficient" in data["reason"]