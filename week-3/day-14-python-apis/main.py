# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests

URL = "https://pokeapi.co/api/v2/pokemon"


def get_pokemon_data(limit=5, offset=0):
    params = {"limit": limit, "offset": offset}
    try:
        response = requests.get(URL, params=params, timeout=10)
        print("Status code:", response.status_code)
        print("Request URL:", response.url)

        if response.status_code == 200:
            return response.json()

        print("Request failed with status code:", response.status_code)
        return None
    except requests.exceptions.RequestException as error:
        print("Network error:", error)
        return None


# ── Step 1: Fetch Data ────────────────────────────────────────────────────────
# Make a GET request to the API and return the parsed JSON response.
# Handle network errors and non-200 status codes gracefully.


# ── Step 2: Parse and Display ─────────────────────────────────────────────────
# Extract at least 3 useful pieces of information from the response.
# Print them in a clear, labelled format — not raw JSON.

def main():
    data = get_pokemon_data(limit=5, offset=0)
    if data is None:
        return

    # Step 6: explore the JSON structure
    print("\nJSON type:", type(data).__name__)
    print("Keys:", list(data.keys()))
    print("'results' type:", type(data["results"]).__name__)

    # Step 7 and 10: extract and show clearly
    results = data["results"]
    print("\n=== Pokemon Report ===")
    print(f"Total Pokemon in database: {data['count']}")
    print(f"Showing: {len(results)}")
    for number, pokemon in enumerate(results, start=1):
        print(f"{number}. Name: {pokemon['name'].title()} | Link: {pokemon['url']}")
main()

