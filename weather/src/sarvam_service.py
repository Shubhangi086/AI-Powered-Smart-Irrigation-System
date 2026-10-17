import requests
from src.config import SARVAM_API_KEY, SARVAM_URL

def get_ai_decision(weather_summary):
    print("2. Weather data collected. Sending to Sarvam AI for analysis..")
    
    headers = {
        "Authorization": f"Bearer {SARVAM_API_KEY}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""
    I am running a smart irrigation system. Here is the weather forecast:
    {weather_summary}
    Based on this data, should I turn on the irrigation system?
    If yes, for how long (in minutes) should I water the crops?
    Keep the answer short and practical.
    """
    
    data = {
        "model": "sarvam-105b", 
        "messages": [
            {"role": "system", "content": "You are an expert agricultural AI assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    
    response = requests.post(SARVAM_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.text}"