import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
WEATHER_API = os.getenv("WEATHER_API_KEY")
SARVAM_API = os.getenv("SARVAM_API_KEY")
if not WEATHER_API or not SARVAM_API:
    print("ERROR: Missing API keys. Check your .env file.")
    exit()

lat = "12.9716"        #(Location = Bengaluru, India)
lon = "77.5946"
weather_url = f"https://api.tomorrow.io/v4/weather/forecast?location={lat},{lon}&apikey={WEATHER_API}"

print("1. Fetching weather data from Tomorrow.io..")
weather_response = requests.get(weather_url, headers={"accept": "application/json"})
if weather_response.status_code != 200:
    print("Failed to get weather data.")
    exit()

hourly_data = weather_response.json()['timelines']['hourly']

summary = "Next 12 hours forecast:\n"     #Summarize the next 12 hours 
for hour in hourly_data[:12]:
    temp = hour['values']['temperature']
    rain = hour['values']['rainIntensity']
    time = hour['time']
    summary += f"- Time: {time} | Temp: {temp}C | Rain: {rain}mm\n"

print("2. Weather data collected. Sending to Sarvam AI for analysis...")

sarvam_url = "https://api.sarvam.ai/v1/chat/completions"    #Send the summary to Sarvam AI
sarvam_headers = {
    "Authorization": f"Bearer {SARVAM_API}",
    "Content-Type": "application/json"
}

prompt = f"""
I am running a Smart Irrigation System. Here is the weather forecast:
{summary}

Based on this data, should I turn on the irrigation system? 
If yes, for how long (in minutes) should I water the crops? 
Keep the answer short and practical.
"""

sarvam_data = {
    "model": "sarvam-105b", 
    "messages": [
        {"role": "system", "content": "You are an expert agricultural AI assistant."},
        {"role": "user", "content": prompt}
    ]
}
sarvam_response = requests.post(sarvam_url, headers=sarvam_headers, json=sarvam_data)
print("\n--- SARVAM AI DECISION ---")
if sarvam_response.status_code == 200:
    ai_answer = sarvam_response.json()['choices'][0]['message']['content']
    print(ai_answer)
else:
    print("Failed to get AI response.")
    print(f"Status Code: {sarvam_response.status_code}")
    print(f"Error: {sarvam_response.text}")
