# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests
import os
from dotenv import load_dotenv

# Load your API key from the environment (never hardcode it here).
# Copy .env.example to .env and fill in your key before running.
load_dotenv()
API_KEY = os.getenv("API_KEY", "")
print(f"Using API Key: {API_KEY[:4]}...")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ── Step 1: Fetch Data ────────────────────────────────────────────────────────
# Make a GET request to the API and return the parsed JSON response.
# Handle network errors and non-200 status codes gracefully.

def fetch_data(query):
    params = {
        "q": query,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code != 200:
            print(f"Error: API request failed with status code {response.status_code}")
            return None

        return response.json()

    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")
        return None


# ── Step 2: Parse and Display ─────────────────────────────────────────────────
# Extract at least 3 useful pieces of information from the response.
# Print them in a clear, labelled format — not raw JSON.

def display_results(data):
    city = data.get("name", "Unknown")
    country = data.get("sys", {}).get("country", "Unknown")
    temperature = data.get("main", {}).get("temp", "N/A")
    humidity = data.get("main", {}).get("humidity", "N/A")
    weather = data.get("weather", [{}])[0].get("description", "N/A")

    print("\n--- Weather Information ---")
    print(f"Location: {city}, {country}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {weather.capitalize()}")



# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    query = input("Enter your search query: ")
    data = fetch_data(query)
    if data:
        display_results(data)


if __name__ == "__main__":
    main()
