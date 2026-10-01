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
    try:
        # Find the city's coordinates
        location_url = "https://geocoding-api.open-meteo.com/v1/search"
        location_params = {
            "name": query,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        location_response = requests.get(
            location_url,
            params=location_params,
            timeout=10
        )

        if location_response.status_code != 200:
            print("Error finding the location.")
            return None

        location_data = location_response.json()

        if "results" not in location_data:
            print("Location not found.")
            return None

        location = location_data["results"][0]

        # Get weather using the city's coordinates
        params = {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": "temperature_2m,wind_speed_10m,weather_code"
        }

        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code != 200:
            print("Error retrieving weather data.")
            return None

        data = response.json()

        data["city"] = location["name"]
        data["country"] = location.get("country", "")

        return data

    except requests.RequestException:
        print("Network error. Please check your internet connection.")
        return None


# ── Step 2: Parse and Display ─────────────────────────────────────────────────
# Extract at least 3 useful pieces of information from the response.
# Print them in a clear, labelled format — not raw JSON.

def display_results(data):
    current = data["current"]

    print("\n=== Weather Information ===")
    print(f"City: {data['city']}")
    print(f"Country: {data['country']}")
    print(f"Temperature: {current['temperature_2m']} °C")
    print(f"Wind Speed: {current['wind_speed_10m']} km/h")
    print(f"Weather Code: {current['weather_code']}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    query = input("Enter your search query: ")
    data = fetch_data(query)
    if data:
        display_results(data)


if __name__ == "__main__":
    main()
