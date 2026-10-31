# Krishi Jal: AI-Powered-Smart-Irrigation-System-For-Predictive-Water-Management-And-Crop-Optimization-OCT-2026

## Project Overview
Farmers consistently overuse or underuse water due to the absence of real-time, data-driven insights, leading to significant water wastage and reduced crop yield. 

This repository contains the backend architecture for **Krishi Jal**, a full-stack AI platform designed to solve this. The backend is split into two modular microservices covering Milestones 1 and 2.

## Repository Structure

This project is organized into two main folders:

### 1. `weather/` (Milestone 1: Weather & API Integration)
- Fetches real-time weather data from Tomorrow.io.
- Uses Sarvam AI (LLM) to generate agricultural advice based on the forecast.
- Exposes services that the ML pipeline and frontend can use.
- *[View Milestone 1 Documentation](./weather/README.md)*

### 2. `irrigation_optimizer/` (Milestone 2: ML-Based Scheduling Engine)
- Takes the predicted irrigation time (from the ML model) and weather data.
- Converts it into an actionable, time-slotted schedule (Morning/Evening).
- Implements a "Rain Guard" to automatically skip irrigation if heavy rain is forecasted.
- Built with FastAPI to serve exact JSON structures to the Krishi Jal frontend.
- *[View Milestone 2 Documentation](./irrigation_optimizer/README.md)*

## Tech Stack
- **Language:** Python 3.x
- **Web Framework:** FastAPI, Uvicorn
- **External APIs:** Tomorrow.io (Weather), Sarvam AI (LLM)
- **Testing:** Pytest
- **Libraries:** requests, python-dotenv

##  Current Repository Structure
```text
AI-Powered-Smart-Irrigation-System/
│
├── irrigation_optimizer/              # MILESTONE 2 
│   ├── test/
│   │   └── test_api.py                # Automated Pytest unit tests (3 passing)
│   ├── main.py                        # FastAPI application server
│   ├── optimizer.py                   # Core scheduling & Rain Guard logic
│   ├── requirements.txt               # Module dependencies
│   └── README.md
│
├── weather/                           # MILESTONE 1 (Weather & AI)
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py                    # Entry point for weather script
│   │   ├── config.py                  # Configuration and API key loading
│   │   ├── weather_service.py         # Fetches data from Tomorrow.io
│   │   └── sarvam_service.py          # Interacts with Sarvam AI
│   ├── .env.example
│   ├── requirements.txt
│   └── README.md
│
├── .gitignore
└── README.md
```

## How to Run the Full Backend

### 1. Set up Environment Variables
You will need API keys for Tomorrow.io and Sarvam AI. 
Create a `.env` file in the `weather` folder and add:

```env
WEATHER_API_KEY=your_tomorrow_io_api_key
SARVAM_API_KEY=your_sarvam_api_key
```
### 2. Install Dependencies
From the root folder, install the required packages:
```bash
pip install -r requirements.txt
pip install -r weather/requirements.txt
pip install -r irrigation_optimizer/requirements.txt
```
### 3. Run the Milestone 1 (Weather) Script
To see the live weather + Sarvam AI decision in the terminal:
```bash
python -m weather.src.main
```
### 4. Run the Milestone 2 (Optimizer) API
To start the FastAPI server for the frontend to connect to:
```bash
python -m uvicorn irrigation_optimizer.main:app --reload
```
API Docs: http://127.0.0.1:8000/docs

Example Schedule Request: http://127.0.0.1:8000/api/schedule/field_1?minutes_needed=120&rain_mm=0

## Schedule Optimizer Test Results

| Test Case | Status | Logic Verified |
| :--- | :--- | :--- |
| Normal Schedule (120 mins, 0mm rain) | **PASSED** | Splits time into 2 PENDING slots (6 AM & 5 PM). |
| Rain Guard (120 mins, 10mm rain) | **PASSED** | Returns SKIPPED status to prevent over-watering. |
| Zero-Water (0 mins, 0mm rain) | **PASSED** | Returns SKIPPED status (soil moisture sufficient). |
| **Total Automated Tests** | **3 / 3** | **100% Success Rate** |
