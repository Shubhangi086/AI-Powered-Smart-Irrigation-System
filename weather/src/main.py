from src.weather_service import get_weather_forecast
from src.sarvam_service import get_ai_decision

def main():
    weather_summary = get_weather_forecast() #get weather
    
    if weather_summary:
        decision = get_ai_decision(weather_summary) #get AI decision

        print("\n--- SARVAM AI DECISION ---")
        print(decision)

if __name__ == "__main__":
    main()