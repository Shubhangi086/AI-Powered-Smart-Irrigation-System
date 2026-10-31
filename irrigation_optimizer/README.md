# Milestone 2: Irrigation Schedule Optimizer API (Krishi Jal)

## Overview
This module is the core backend scheduling engine for **Krishi Jal** (AI-Powered Smart Irrigation System). It receives the required irrigation time (from the ML model) and weather data, and converts it into an actionable, time-slotted irrigation plan. 

The API is specifically designed to integrate with the Krishi Jal Next.js frontend, providing the exact JSON data structures needed to render the "Irrigation Schedule" UI cards.

## Features
- **Time-Slot Optimization:** Splits the required irrigation minutes into Morning (6:00 AM) and Evening (5:00 PM) slots to minimize water evaporation.
- **Rain Guard Logic:** Automatically cancels irrigation and returns a `SKIPPED` status if heavy rain (>2mm) is forecasted, preventing over-watering.
- **Zero-Water Skip:** Automatically skips irrigation if the ML model predicts that soil moisture is already sufficient (0 minutes needed).
- **Frontend-Ready Output:** Returns exact JSON structures (`PENDING`/`SKIPPED`, volume liters, duration) that map directly to the Krishi Jal dashboard cards.
- **Automated Testing:** 100% passing unit tests using Pytest for all edge cases.

## API Endpoint
**`GET /api/schedule/{field_id}`**

### Query Parameters:
- `minutes_needed` (int): The total duration of irrigation predicted by the ML model (default is 120).
- `rain_mm` (float): The rain intensity from the Weather API (default is 0.0).

### Example Response 1: Scheduled (Normal Day)
```json
{
  "field_id": "field_1",
  "date": "2026-10-31",
  "status": "SCHEDULED",
  "total_minutes": 120,
  "schedule": [
    {
      "start_time": "06:00",
      "end_time": "07:00",
      "duration_minutes": 60,
      "volume_liters": 3000,
      "status": "PENDING",
      "reason": "Morning irrigation to prevent evaporation"
    }
  ]
}
```
### Example Response 2: Skipped (Heavy Rain)
```json
{
  "field_id": "field_1",
  "date": "2026-10-31",
  "status": "SKIPPED",
  "reason": "Rain Guard: Monsoon shower of 10.0mm forecast. Skipped to prevent over-watering.",
  "schedule": []
}
```

## Frontend Integration (Krishi Jal)
This API directly powers the **Irrigation Schedule** page of the Krishi Jal PWA.
- The `"status": "SKIPPED"` response triggers the grey **Rain Guard** card on the UI.
- The `"status": "PENDING"` response populates the green **Time-Slot** cards, displaying the start times, duration, and volume liters.

## Current Repository Structure 
```text
irrigation_optimizer/
├── test/
│   └── test_api.py           # Automated Pytest unit tests (3 passing)
├── main.py                   # FastAPI application server
├── optimizer.py              # Core scheduling & Rain Guard logic
├── requirements.txt
└── README.md
```

## How to Run Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the FastAPI server (from the root fetch_weather_APIs folder):
```bash
python -m uvicorn irrigation_optimizer.main:app --reload
```

3. Open API Docs in your browser: http://127.0.0.1:8000/docs

## Running Automated Tests
To verify the core logic (Normal, Rain Guard, Zero Water), run:

```bash
python -m pytest irrigation_optimizer/test/test_api.py -v
```