# 🌾 AI-Powered Smart Irrigation System - Weather & API Integration
## 📌 Project Overview
Farmers consistently overuse or underuse water due to the absence of real-time, data-driven insights, leading to significant water wastage and reduced crop yield. This project is building a full-stack AI platform to solve this.

This specific repository/module covers Milestone 1 (Weeks 1-2): Weather API Integration and Basic AI Decision Making. It fetches real-time weather forecasts and uses the Sarvam AI LLM to provide actionable irrigation advice.

## 🚀 Current Features
Live Weather Fetching: Integrates with the Tomorrow.io API to get hourly forecasts (temperature, rain intensity).

AI Decision Engine: Sends the weather forecast to Sarvam AI (sarvam-105b model), which acts as an agricultural expert to decide if irrigation is needed and for how long.

Secure Environment: Uses python-dotenv to hide API keys.

## 🛠️ Tech Stack
Language: Python 3.x

External APIs: Tomorrow.io (Weather), Sarvam AI (LLM)

Libraries: requests, python-dotenv

## 📁 Current Repository Structure

```text
weather/
├── .gitignore               # Prevents sensitive files from being uploaded
├── .env                     # Stores secret API keys 
├── requirements.txt         # Python dependencies
├── irrigation_decision.py   # Main script for weather fetching and AI decision
└── README.md                # Project documentation
```

## ⚙️ How to Setup and Run
1. Clone the repository

```bash
git clone <your-github-repo-link>
cd weather
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up your Environment Variables
Create a file named .env in the weather folder and add your keys:
```env
API=your_tomorrow_io_api_key
SARVAM_API=your_sarvam_api_key
```

4. Run the script

```bash
python irrigation_decision.py
```

## 🧠 How it Works

-The script connects to Tomorrow.io and pulls the next 12-24 hours of weather data.

-It creates a summary of the Temperature and Rain Intensity.

-It sends this summary to Sarvam AI with a prompt asking: "Should I turn on the irrigation system? If yes, for how long?"

-The AI analyzes the rain forecast (e.g., if rain is coming, it says no) and outputs a practical recommendation in the terminal.