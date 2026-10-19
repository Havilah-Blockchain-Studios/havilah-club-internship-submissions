# Day 14: Python APIs - Coinlore Integration

## API Overview
- **API Name**: Coinlore Crypto API
- **Endpoint Used**: `https://www.coinlore.com/api/tickers/`
- **Authentication**: None required (Free public API, no API keys or personal access tokens needed)

## Parameters
- Accepts optional query parameters like `?start=0&limit=100` to paginate through lists of cryptocurrencies.

## Program Functionality
- Sends a GET request using Python's `requests` library.
- Validates the response status code and handles network exceptions.
- Parses the returned JSON data to extract and display key market details (such as coin name, symbol, price in USD, and market rank).
