# #Day 14 — Python and APIs
# #Task: Build a Python program that retrieves information from an API
# #and processes the JSON response to produce a useful output.
# #Submit this script + a screenshot of the printed output.

#import requests
#import os

## Load your API key from the environment (never hardcode it here).
## Copy .env.example to .env and fill in your key before running.
#API_KEY = os.getenv("API_KEY", "")
#BASE_URL = # TODO: set your chosen API's base URL


## ── Step 1: Fetch Data ────────────────────────────────────────────────────────
## Make a GET request to the API and return the parsed JSON response.
## Handle network errors and non-200 status codes gracefully.

#def fetch_data(query):
#   # TODO: build params dict and call requests.get()
#  # TODO: check response.status_code before calling .json()
#    pass


## ── Step 2: Parse and Display ─────────────────────────────────────────────────
## Extract at least 3 useful pieces of information from the response.
## Print them in a clear, labelled format — not raw JSON.

#def display_results(data):
#    # TODO: navigate the JSON structure and print each field with a label 
#    pass


## ── Main ──────────────────────────────────────────────────────────────────────
#def main():
#    query = input("Enter your search query: ") 
#    data = fetch_data(query)
#    if data: 
#        display_results(data)
    
    
#    if __name__ == "__main__":
#        main()




# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.


import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY =os.getenv("API_KEY", "")
BASE_URL = "https://finnhub.io/api/v1/quote"

def fetch_data(query):
    try:
        params ={
            "symbol": query,
            "token": API_KEY
        }
        
        
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            print("Error: API returned status code", response.status_code)
            return None
        
        
    except requests.exceptions.RequestException as error:
        print("Network error:", error)
        return None
    
    
def display_results(data, symbol):
    print("==== Stock Information ====")
    
    print("symbol:", symbol)
    print("current price: $", data["c"])
    print("price change: $", data["d"])
    print("percentage change: ", data["dp"])
    print("previous close: $", data["pc"])
    
def main():
    query = input("Enter stock symbol: ")
    data = fetch_data(query)
    if data:
        display_results(data, query.upper())
        
if __name__ == "__main__":
    main()