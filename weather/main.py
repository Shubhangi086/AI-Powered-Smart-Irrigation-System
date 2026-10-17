from weather_service import get_weather_forecast
from sarvam_service import get_ai_decision

def main():
    # Step 1: Get weather
    weather_summary = get_weather_forecast()
    
    if weather_summary:
        # Step 2: Get AI decision
        decision = get_ai_decision(weather_summary)
        
        # Step 3: Print final result
        print("\n--- SARVAM AI DECISION ---")
        print(decision)

if __name__ == "__main__":
    main()