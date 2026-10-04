# Day 14 - Python and APIs
# Task: Build a Python program that retrieves data from a public API
# and processes the JSON response to display useful information.

import requests
import os

# Load your API key from the environment (Open Library needs no key)
API_KEY = os.getenv("API_KEY", "")
BASE_URL = "https://openlibrary.org/search.json"


# Step 1: Fetch Data
# Make a GET request to the API and return the parsed JSON.
# Handle network errors and non-200 status codes.
def fetch_data(query, limit=5):
    params = {"q": query, "limit": limit}
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")
        return None

    print(f"Request URL: {response.url}")
    print(f"Status code: {response.status_code}")

    if response.status_code != 200:
        print("The API did not return a successful response.")
        return None

    return response.json()


# Step 2: Explore the JSON structure
def explore_json(data):
    print("\n--- JSON structure ---")
    print(f"Top-level type: {type(data).__name__}")
    print(f"Top-level keys: {list(data.keys())}")
    docs = data.get("docs", [])
    print(f"'docs' is a {type(docs).__name__} with {len(docs)} items")
    if docs:
        print(f"Keys in first item: {list(docs[0].keys())[:8]}")


# Step 3: Parse and Display
def display_results(data):
    books = data.get("docs", [])
    if not books:
        print("No results found.")
        return

    print(f"\nFound {data.get('numFound', 0)} books. Showing the top {len(books)}:\n")
    for number, book in enumerate(books, start=1):
        title = book.get("title", "Unknown title")
        authors = ", ".join(book.get("author_name", ["Unknown author"]))
        year = book.get("first_publish_year", "Unknown year")
        print(f"{number}. Title: {title}")
        print(f"   Author: {authors}")
        print(f"   First published: {year}\n")


# Main
def main():
    query = input("Enter your search query: ")
    limit_text = input("How many results do you want? (default 5): ")
    limit = int(limit_text) if limit_text.strip().isdigit() else 5

    data = fetch_data(query, limit)
    if data:
        explore_json(data)
        display_results(data)


if __name__ == "__main__":
    main()
