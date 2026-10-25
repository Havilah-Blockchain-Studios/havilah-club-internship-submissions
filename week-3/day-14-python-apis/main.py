# Day 14 — Python and APIs

import requests
import os

API_KEY = os.getenv("API_KEY", "")
BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"


# Fetch data from the API
def fetch_data(query):
    params = {
        "name": query,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        print("Status code:", response.status_code)
        print("Request URL:", response.url)

        if response.status_code != 200:
            print("Request failed.")
            return None

        data = response.json()
        return data

    except requests.exceptions.RequestException as error:
        print("Network error:", error)
        return None


# Display useful information from the API
def display_results(data):
    if "results" not in data or not data["results"]:
        print("No results found.")
        return

    location = data["results"][0]

    print("\n--- Location Information ---")
    print("Name:", location.get("name"))
    print("Country:", location.get("country"))
    print("Latitude:", location.get("latitude"))
    print("Longitude:", location.get("longitude"))


def main():
    query = input("Enter a city or location: ")

    data = fetch_data(query)

    if data:
        display_results(data)


if __name__ == "__main__":
    main()