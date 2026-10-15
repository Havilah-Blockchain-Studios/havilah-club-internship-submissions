# Day 14 — Python and APIs

import requests
import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("API_KEY", "")
BASE_URL = "https://api.restcountries.com/countries/v5"  



def fetch_data(query):
    params = {"q": query}
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        response = requests.get(BASE_URL, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error: received status code", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None



def display_results(data):
    try:
        country = data["data"]["objects"][0]
        name = country["names"]["common"]
        capital = country["capitals"][0]["name"]
        region = country["region"]
        population = country["population"]

        print("country:", name)
        print("capital:", capital)
        print("region:", region)
        print("population:", population)
    except (KeyError, IndexError):
        print("Could not extract expected fields from the response.")
    


def main():
    query = input("Enter your search query: ")
    data = fetch_data(query)
    if data:
        display_results(data)


if __name__ == "__main__":
    main()
