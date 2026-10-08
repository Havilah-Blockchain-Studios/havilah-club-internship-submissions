# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests
import os

# Load your API key from the environment (never hardcode it here).
# Copy .env.example to .env and fill in your key before running.

# No API key needed for OPENFOODFACTS.ORG
BASE_URL = "https://world.openfoodfacts.org/api/v2/search" 


# ── Step 1: Fetch Data ────────────────────────────────────────────────────────
# Make a GET request to the API and return the parsed JSON response.
# Handle network errors and non-200 status codes gracefully.

def fetch_data(query):
    # Search parameters configured for Open Food Facts v2 API
    params = {
        "search_terms": query,
        "json": "true",
        "page_size": 3  # Restrict to 3 products to keep terminal print readable
    }
    
    # Open Food Facts requires a custom User-Agent to avoid getting blocked
    headers = {
        "User-Agent": "Day14AssignmentApp/1.0 (student@example.com)"
    }
    
    try:
        # Call requests.get() using our endpoint, variables, and headers
        response = requests.get(BASE_URL, params=params, headers=headers)
        
        # Check response.status_code dynamically 
        response.raise_for_status()
        
        # Parse and return JSON payload
        return response.json()
        
    except requests.exceptions.HTTPError as http_err:
        print(f"\n[Error] Server returned an HTTP error: {http_err}")
    except requests.exceptions.ConnectionError:
        print("\n[Error] Failed to connect. Please check your network connection.")
    except requests.exceptions.Timeout:
        print("\n[Error] The request timed out. Please try again.")
    except requests.exceptions.RequestException as err:
        print(f"\n[Error] An unexpected error occurred: {err}")

    return None    
        


# ── Step 2: Parse and Display ─────────────────────────────────────────────────
# Extract at least 3 useful pieces of information from the response.
# Print them in a clear, labelled format — not raw JSON.

def display_results(data):
    products = data.get("products", [])
    
    if not products:
        print("\nNo global grocery items found matching that search string.")
        return

    print(f"\n=== Found {data.get('count', len(products))} Global Products (Displaying Top {len(products)}) ===")
    
    # Loop over the returned records (runs up to 3 times based on page_size)
    for index, product in enumerate(products, start=1):
        
        # Creating a manual DICTIONARY to explicitly store extracted details
        extracted_info = {
            "item_name": product.get("product_name", "Unknown Product Name"),
            "brand_name": product.get("brands", "Unknown Brand"),
            "net_quantity": product.get("quantity", "Unknown Weight/Volume"),
            "nutrition": product.get("nutriscore_grade", "Not Scored").upper()
        }

        # Listing and printing the useful information using our dictionary keys
        print(f"\n[{index}] Item: {extracted_info['item_name']}")
        print(f"    • Manufacturer/Brand: {extracted_info['brand_name']}")
        print(f"    • Net Quantity: {extracted_info['net_quantity']}")
        print(f"    • Nutrition Grade: {extracted_info['nutrition']}")
        print("-" * 50)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("--- Open Food Facts Catalog Query Engine ---")
    
    while True:
        print("\nAvailable options: Type a grocery item, or type 'exit' to quit.")
        query = input("Enter a grocery item or brand (e.g., Nutella, Oreo): ").strip()
        
        # Break condition to end the loop execution safely
        if query.lower() == 'exit':
            print("Exiting search engine. Goodbye!")
            break
            
        if not query:
            print("[Error] Query string input cannot be empty.")
            continue  # Skips the rest of the loop block and asks again
            
        data = fetch_data(query)
        if data:
            display_results(data)


if __name__ == "__main__":
    main()
