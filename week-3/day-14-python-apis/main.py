# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

from dotenv import load_dotenv
load_dotenv()
import requests
import os

# Load your API key from the environment (never hardcode it here).
# Copy .env.example to .env and fill in your key before running.
API_KEY = os.getenv("API_KEY", "")
BASE_URL = "https://api.nasa.gov/planetary/apod"


# ── Step 1: Fetch Data ────────────────────────────────────────────────────────
# Make a GET request to the API and return the parsed JSON response.
# Handle network errors and non-200 status codes gracefully.

def fetch_data(query):
    # TODO: build params dict and call requests.get()
    # TODO: check response.status_code before calling .json()
    params = {
        "api_key": API_KEY
    }
    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error: Status code", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Network error occurred:", e)
        return None


# ── Step 2: Parse and Display ─────────────────────────────────────────────────
# Extract at least 3 useful pieces of information from the response.
# Print them in a clear, labelled format — not raw JSON.

def display_results(data):
    # TODO: navigate the JSON structure and print each field with a label
    if data:
        print("\n--- NASA Picture of the Day ---")
        print("Title:", data.get("title"))
        print("Date:", data.get("date"))
        print("Media Type:", data.get("media_type"))
        print("URL:", data.get("url"))


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    query = input("Enter your search query: ")
    data = fetch_data(query)
    if data:
        display_results(data)


if __name__ == "__main__":
    main()
