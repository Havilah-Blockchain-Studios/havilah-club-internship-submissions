# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests

def get_data(limit):
    try:
        res = requests.get(
            "https://api.coinlore.com/api/tickers/",
            params={"start": 0, "limit": limit},
        )
        print("URL:", res.url)
        print("Status:", res.status_code)
        if res.status_code == 200:
            return res.json()
        return None
    except requests.exceptions.RequestException:
        print("Network error")
        return None
data = get_data(3)

if data:
    for coin in data["data"]:
        print("Name :", coin["name"])
        print("Price: $", coin["price_usd"])
        print("Rank :", coin["rank"])
        print("_" * 20)