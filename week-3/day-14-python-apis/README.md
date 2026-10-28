# Day 14: Working with Public APIs in Python

## Overview
This program retrieves real-time cryptocurrency price data using HTTP GET requests sent to the public CoinGecko API, parses the JSON response, handles network errors, and displays formatted market statistics.

## API Selection & Endpoint
- **API**: CoinGecko Public API
- **Endpoint**: `https://api.coingecko.com/api/v3/simple/price`
- **Authentication**: None required (Free public tier)

## Query Parameters Used
- `ids` (string): Comma-separated asset identifiers (e.g., `bitcoin`, `ethereum`, `solana`).
- `vs_currencies` (string): Target fiat/crypto conversion currency (e.g., `usd`, `eur`).
- `include_24hr_change` (boolean): Set to `true` to include 24-hour percentage price changes.
- `include_market_cap` (boolean): Set to `true` to include market capitalization data.

## Extracted Useful Information
1. **Current Price**: Real-time asset unit price (`usd` / `eur`).
2. **24h Price Change**: Percentage price movement over the last 24 hours (`usd_24h_change`).
3. **Market Capitalization**: Total dollar market capitalization (`usd_market_cap`).

## Features & Error Handling
- Robust request handling using standard `requests.exceptions.RequestException` try/except blocks.
- Validates HTTP response status codes and logs target request URLs (`response.url`).
- Formats floating-point numerical outputs into readable currency strings.