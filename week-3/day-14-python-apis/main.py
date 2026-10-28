# Day 14 - Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import os
import requests

# Load your API key from the environment (never hardcode it here).
# Copy .env.example to .env and fill in your key before running.
API_KEY = os.getenv("API_KEY", "")
BASE_URL = "https://api.coingecko.com/api/v3/simple/price"  # Free public API (no key required)


# --- Step 1: Fetch Data --------------------------------------------------
# Make a GET request to the API and return the parsed JSON response.
# Handle network errors and non-200 status codes gracefully.

def fetch_data(query):
    """
    query: dict containing cryptocurrency params (e.g., {"ids": "bitcoin,ethereum", "vs_currencies": "usd"})
    """
    params = query

    try:
        # User-Agent header helps avoid strict rate-limiting blocks on public endpoints
        headers = {"User-Agent": "Python/RequestsApp"}
        response = requests.get(BASE_URL, params=params, headers=headers, timeout=10)
        
        print(f"Request URL: {response.url}")
        print(f"Status Code: {response.status_code}\n")

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: API returned status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Network error encountered: {e}")
        return None


# --- Step 2: Parse and Display -------------------------------------------
# Extract at least 3 useful pieces of information from the response.
# Print them in a clear, labelled format - not raw JSON.

def display_results(data, target_currency):
    if not data or not isinstance(data, dict):
        print("No market data returned or invalid response format.")
        return

    curr = target_currency.lower()
    symbol = "$" if curr == "usd" else ("€" if curr == "eur" else f"{curr.upper()} ")

    print("=" * 60)
    print(f"         CRYPTOCURRENCY MARKET SUMMARY ({curr.upper()})         ")
    print("=" * 60)

    for coin_id, details in data.items():
        # Extract at least 3 useful pieces of information
        price = details.get(curr, "N/A")
        market_cap = details.get(f"{curr}_market_cap", "N/A")
        change_24h = details.get(f"{curr}_24h_change", "N/A")

        formatted_price = f"{symbol}{price:,.2f}" if isinstance(price, (int, float)) else "N/A"
        formatted_mcap = f"{symbol}{market_cap:,.2f}" if isinstance(market_cap, (int, float)) else "N/A"
        formatted_change = f"{change_24h:+.2f}%" if isinstance(change_24h, (int, float)) else "N/A"

        print(f"Asset: {coin_id.title()}")
        print(f"  Current Price   : {formatted_price}")
        print(f"  24h Price Change: {formatted_change}")
        print(f"  Market Cap      : {formatted_mcap}")
        print("-" * 60)


def main():
    # Query 1: Prices for Bitcoin, Ethereum, and Solana in USD
    print("--- Query 1: Fetching USD prices for Bitcoin, Ethereum, Solana ---")
    query_usd = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd",
        "include_24hr_change": "true",
        "include_market_cap": "true"
    }
    data_1 = fetch_data(query_usd)
    if data_1:
        display_results(data_1, "usd")

    print("\n" + "#" * 60 + "\n")

    # Query 2 (Parameter change test): Fetching prices in EUR
    print("--- Query 2: Fetching EUR prices for Bitcoin and Cardano ---")
    query_eur = {
        "ids": "bitcoin,cardano",
        "vs_currencies": "eur",
        "include_24hr_change": "true",
        "include_market_cap": "true"
    }
    data_2 = fetch_data(query_eur)
    if data_2:
        display_results(data_2, "eur")


if __name__ == "__main__":
    main()