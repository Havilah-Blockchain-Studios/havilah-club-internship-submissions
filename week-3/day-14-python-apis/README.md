# Day 14 - Python and APIs

## API used
Open Library Search API (free, no API key required).

## What the program does
The program asks for a search word and a number of results, sends a GET request to the API, checks the response, and prints the title, author and first publish year of each book found.

## Endpoint and parameters
- Endpoint: `https://openlibrary.org/search.json`
- `q`: the search word entered by the user
- `limit`: how many results to return

## JSON structure
The response is a dictionary. `numFound` is the total number of matches and `docs` is a list of dictionaries, one per book.

## Information extracted
- `title`
- `author_name`
- `first_publish_year`

## Error handling
Network errors are caught with `requests.exceptions.RequestException`, and non-200 status codes are reported without crashing.

## How to run
Activate the virtual environment, install requests with `python -m pip install requests`, then run `python3 main.py`.
