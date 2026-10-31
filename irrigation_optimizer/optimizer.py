"""Pure logic engine for the Irrigation Schedule Optimizer. Converts predicted irrigation minutes and weather 
data into time-slotted schedules. Implements a Rain Guard to prevent over-watering during monsoon forecasts.
"""

from datetime import datetime, timedelta

def create_irrigation_schedule(field_id: str, total_minutes_needed: int, rain_intensity_mm: float):
    """
    Generates the time-slotted irrigation schedule.
    Rules:
    1. RAIN GUARD: If rain > 2.0mm, skip irrigation entirely.
    2. ZERO WATER: If minutes <= 0, skip irrigation.
    3. TIME SLOTS: Split the total minutes evenly between Morning (6 AM) and Evening (5 PM).
    Returns a dictionary formatted for the Krishi Jal frontend UI cards.
    """
    today_date = datetime.now().strftime("%Y-%m-%d")
    if rain_intensity_mm > 2.0: #rule 1
        return {
            "field_id": field_id,
            "date": today_date, 
            "status": "SKIPPED",
            "reason": f"Rain Guard: Monsoon shower of {rain_intensity_mm}mm forecast. Skipped to prevent over-watering.",
            "schedule": []
        }
    if total_minutes_needed <= 0: #rule 2
         return {
            "field_id": field_id,
            "date": today_date, 
            "status": "SKIPPED",
            "reason": "Soil moisture is sufficient.",
            "schedule": []
        }
    schedule = [] #rule 3
    half_time = total_minutes_needed / 2

    morning_start = datetime.strptime("06:00", "%H:%M") 
    morning_end = morning_start + timedelta(minutes=half_time)

    evening_start = datetime.strptime("17:00", "%H:%M")
    evening_end = evening_start + timedelta(minutes=half_time)

    volume_liters = total_minutes_needed * 50  #volume calculation
    schedule.append({
        "start_time": morning_start.strftime("%H:%M"),
        "end_time": morning_end.strftime("%H:%M"),
        "duration_minutes": half_time,
        "volume_liters": volume_liters / 2,
        "status": "PENDING",
        "reason": "Morning irrigation to prevent evaporation"
    })
    schedule.append({
        "start_time": evening_start.strftime("%H:%M"),
        "end_time": evening_end.strftime("%H:%M"),
        "duration_minutes": half_time,
        "volume_liters": volume_liters / 2,
        "status": "PENDING",
        "reason": "Evening irrigation"
    })
    return {
        "field_id": field_id,
        "date": today_date,
        "status": "SCHEDULED",
        "total_minutes": total_minutes_needed,
        "schedule": schedule
    }