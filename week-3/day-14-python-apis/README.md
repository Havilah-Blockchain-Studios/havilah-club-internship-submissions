Day 14 — Python and APIs

API Used

I used the Open-Meteo Geocoding API. It is a free public API that returns location information in JSON format and does not require an API key.

Endpoint

The endpoint I used is:

"https://geocoding-api.open-meteo.com/v1/search"

Parameters

The program uses these parameters:

- "name" — the city or location entered by the user
- "count" — limits the number of results
- "language" — sets the language of the response
- "format" — sets the response format to JSON

What the Program Does

The program asks the user to enter a city or location. It sends the search to the API using "requests.get()" and processes the JSON response.

It displays useful information such as:

- Location name
- Country
- Latitude
- Longitude

The program also checks the HTTP status code and handles network errors using "try" and "except".

Testing

I tested the program with Lagos and Abuja, and it successfully returned the location information for both.