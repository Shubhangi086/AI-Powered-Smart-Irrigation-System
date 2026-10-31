"""FastAPI server for the Milestone 2 Irrigation Schedule Optimizer.
Exposes the REST API endpoint that the Krishi Jal frontend calls to get schedule cards.
"""

from fastapi import FastAPI
from irrigation_optimizer.optimizer import create_irrigation_schedule
#from irrigation_optimizer.test_api import get_weather_forecast # (Optional if you want to integrate)
import requests

app = FastAPI(title="Irrigation Schedule Optimizer API")

@app.get("/api/schedule/{field_id}")
def get_schedule(field_id: str, minutes_needed: int = 120, rain_mm: float = 0.0):
    result = create_irrigation_schedule(
        field_id=field_id, 
        total_minutes_needed=minutes_needed, 
        rain_intensity_mm=rain_mm
    )
    return result