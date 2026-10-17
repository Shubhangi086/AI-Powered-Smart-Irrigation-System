import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# API Keys
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

# Location (Bengaluru)
LAT = "12.9716"
LON = "77.5946"

# URLs
WEATHER_URL = f"https://api.tomorrow.io/v4/weather/forecast?location={LAT},{LON}&apikey={WEATHER_API_KEY}"
SARVAM_URL = "https://api.sarvam.ai/v1/chat/completions"