import requests
from src.config import WEATHER_URL

def get_weather_forecast():
    print("1. Fetching weather data from Tomorrow.io...")
    response = requests.get(WEATHER_URL, headers={"accept": "application/json"})
    
    if response.status_code != 200:
        print("Failed to get weather data.")
        return None
        
    data = response.json()
    hourly_data = data['timelines']['hourly']
    
    # Summarize the next 12 hours
    summary = "Next 12 hours forecast:\n"
    for hour in hourly_data[:12]:
        temp = hour['values']['temperature']
        rain = hour['values']['rainIntensity']
        time = hour['time']
        summary += f"- Time: {time} | Temp: {temp}°C | Rain: {rain}mm\n"
        
    return summary