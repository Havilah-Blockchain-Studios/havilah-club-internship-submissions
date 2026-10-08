# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests
import os

# Load your API key from the environment (never hardcode it here).
# Copy .env.example to .env and fill in your key before running.
API_KEY = os.getenv("API_KEY", "")
BASE_URL = "https://www.cheapshark.com/api/1.0/games"


# ── Step 1: Fetch Data ────────────────────────────────────────────────────────
# Make a GET request to the API and return the parsed JSON response.
# Handle network errors and non-200 status codes gracefully.

def fetch_data(query):
    search_term = query.strip() if query.strip() else "Call of Duty"
    params = {"title": search_term}
    
    # Header required to prevent CheapShark 400 Bad Request errors
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(BASE_URL, params=params, headers=headers, timeout=10)

        # Print status code and request URL
        print("Status Code:", response.status_code)
        print("Request URL:", response.url)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Error: Search term '{search_term}' not found.")
            return None
        else:
            print("API Error: Received status code", response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print("Network error occurred:", e)
        return None


# -- Step 2: Parse and Display ---------------------------------------------
def display_results(data):
    if not data or not isinstance(data, list):
        print("No matching game results found.")
        return

    print("\n=== GAME SEARCH RESULTS ===")

    # Extract useful information for top 5 matching games
    for item in data[:5]:
        title = item.get("external", "N/A")
        price = item.get("cheapest", "N/A")
        game_id = item.get("gameID", "N/A")
        steam_id = item.get("steamAppID", "N/A")

        print(f"Title       : {title}")
        print(f"Lowest Price: ${price}")
        print(f"Game ID     : {game_id}")
        print(f"Steam App ID: {steam_id if steam_id else 'N/A'}")
        print("-" * 35)


# -- Main ------------------------------------------------------------------
def main():
    query = input("Enter your search query: ")
    data = fetch_data(query)
    if data:
        display_results(data)


if __name__ == "__main__":
    main()