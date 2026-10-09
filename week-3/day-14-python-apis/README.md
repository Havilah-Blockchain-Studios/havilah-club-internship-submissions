# Day 14: Python + APIs (Open Food Facts)

## API selected
Open Food Facts, a free, collaborative database of food products from around
the world. It was found on PublicAPIs.io. No API key is required.

## What the program does
`main.py` asks the user to type a food category, sends a GET request to the
Open Food Facts search endpoint for that category, checks that the request
succeeded, converts the JSON response into Python data, and prints a numbered,
readable list of products. The work is split into functions: `fetch_data`
retrieves and returns the JSON, `display_results` prints it, and `main` ties
them together.

## Endpoint and parameters
- Endpoint: `https://world.openfoodfacts.org/api/v2/search`
- Parameters (passed with `params`):
  - `categories_tags`: the food category to search, typed in by the user
    (e.g. `breakfast-cereals`, `sweets`, `grains`)
  - `fields`: limits the response to `product_name,brands,nutriscore_grade`
  - `page_size`: number of products returned (5)
- Header: a custom `User-Agent`, which Open Food Facts requires for API calls.
  Without it, my request was refused with a 403 status code.

## JSON structure
The response is a dictionary. Its `products` key holds a list of dictionaries,
one per product. Other keys include `count` (total matches), `page`,
`page_size` and `skip`.

## Information extracted
- Total number of products found in the category (`count`)
- Product name
- Brand
- Nutri-Score grade (A to E). Some products have no grade, and the API returns
  `not-applicable` for them (for example a chewing gum), which the program
  prints as it is.

## Error handling
- `try/except requests.exceptions.RequestException` catches network failures,
  including timeouts (the request uses `timeout=10`).
- `response.status_code` is checked, and any status other than 200 prints an
  error message instead of crashing.
- If a category returns no products, the program prints a "No products found"
  message instead of an empty list.
- Missing fields are handled with `.get()` and a default of "Unknown".

## How to run
```
python -m venv .venv
.venv\Scripts\activate
python -m pip install requests
python main.py
```
The program then prompts:
```
Enter a food category (e.g. breakfast-cereals): sweets
```

## Testing
I ran the program with several categories and each returned a different set of
results:

| Category | Total products found |
|---|---|
| `breakfast-cereals` | 27545 |
| `sweets` | 24494 |
| `grains` | 35899 |

In each case the request URL, the total count and the list of products changed,
and the program processed the new response correctly.

## Issues met while testing
- **403 Forbidden:** my first request was refused until I added a custom
  `User-Agent` header, which Open Food Facts requires.
- **503 Service Unavailable:** the server often returned 503 during testing.
  Opening the same kind of URL in a browser showed a page saying the service
  was under unusually high demand and that anonymous users can be limited. The
  program printed the status code and exited cleanly each time, and retrying
  later gave a 200.
- **Timeout:** one request (`oats`) hit the 10 second timeout. The `except`
  branch caught it and printed a network error message instead of crashing.
- **Empty category:** opening the search URL for a nonsense category (`zzzz`)
  in a browser returned `count: 0` and an empty `products` list, which the
  program's "No products found" check is written to handle. When I ran
  `zzzz` through the program itself, the server returned 503 each time, so I
  could not confirm that message from a script run.