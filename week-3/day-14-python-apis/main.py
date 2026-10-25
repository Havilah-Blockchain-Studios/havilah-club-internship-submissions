# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests

import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Load your API key from the environment (never hardcode it here).
# Copy .env.example to .env and fill in your key before running.

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

            print(f"API request failed: {response.status_code}")

            print("Please check the city name or API key.")

            return None

        return response.json()

    except requests.exceptions.RequestException as error:

        print(f"Network error: {error}")
        return None
    


# ── Step 2: Parse and Display ─────────────────────────────────────────────────
# Extract at least 3 useful pieces of information from the response.
# Print them in a clear, labelled format — not raw JSON.

def display_results(data):

    city = data["name"]

    country = data["sys"]["country"]

    temperature = data["main"]["temp"]

    feels_like = data["main"]["feels_like"]

    humidity = data["main"]["humidity"]

    weather = data["weather"][0]["description"]

    print("\n--- Weather Information ---")

    print(f"Location: {city}, {country}")

    print(f"Temperature: {temperature}°C")

    print(f"Feels Like: {feels_like}°C")

    print(f"Humidity: {humidity}%")

    print(f"Condition: {weather.title()}")



# ── Main ──────────────────────────────────────────────────────────────────────
  def main():

    if not API_KEY:

        print("Error: API_KEY is not set.")

        print("Add your API key to the .env file.")

        return

    query = input("Enter a city: ").strip()

    if not query:

        print("Please enter a city name.")

        return

    data = fetch_data(query)

    if data:

        display_results(data)

if __name__ == "__main__":

    main()
