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