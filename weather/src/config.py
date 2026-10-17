import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

LAT = "12.9716"  # Location (Bengaluru)
LON = "77.5946"

WEATHER_URL = f"https://api.tomorrow.io/v4/weather/forecast?location={LAT},{LON}&apikey={WEATHER_API_KEY}"
SARVAM_URL = "https://api.sarvam.ai/v1/chat/completions"