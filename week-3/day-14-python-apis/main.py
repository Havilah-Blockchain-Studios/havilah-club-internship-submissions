# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests
import os

# Load your API key from the environment (never hardcode it here).
# Copy .env.example to .env and fill in your key before running.
API_KEY = os.getenv("API_KEY", "")
BASE_URL = "https://api.open-meteo.com/v1/forecast"  


# ── Step 1: Fetch Data ────────────────────────────────────────────────────────
# Make a GET request to the API and return the parsed JSON response.
# Handle network errors and non-200 status codes gracefully.

def fetch_data(query):
    # We use a free public weather API that needs no API key
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Build your parameters dictionary
    params = {
        "latitude": 51.50,
        "longitude": -0.12,
        "current_weather": True
    }
    
    # Make the GET request
    response = requests.get(url, params=params)
    
    # Check if the status code is 200 (Success) before returning .json()
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None


# ── Step 2: Parse and Display ─────────────────────────────────────────────────
# Extract at least 3 useful pieces of information from the response.
# Print them in a clear, labelled format — not raw JSON.

def display_results(data):
    # Extract the current weather dictionary from the JSON response
    weather = data.get("current_weather", {})
    
    temperature = weather.get("temperature")
    windspeed = weather.get("windspeed")
    is_day = weather.get("is_day")
    
    # Print the extracted information cleanly with labels
    print("\n--- API Data Results ---")
    print(f"City / Location: London")
    print(f"Current Temperature: {temperature}°C")
    print(f"Wind Speed: {windspeed} km/h")
    print(f"Is it daytime?: {'Yes' if is_day == 1 else 'No'}")
    print("------------------------\n")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    query = input("London")
    data = fetch_data(query)
    if data:
        display_results(data)


if __name__ == "__main__":
    main()
