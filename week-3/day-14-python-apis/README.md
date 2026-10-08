# Day 14 — Python Game Search API Project

## Overview
This Python script connects to the CheapShark Game Search API to query real-time game titles, pricing, and database IDs based on user input, handles HTTP status codes and network errors, and displays formatted results.

## API Details
- **API Name:** CheapShark Game Search API
- **Endpoint:** `https://www.cheapshark.com/api/1.0/games`
- **Authentication:** None required (Free public API)

## Parameters
- `title`: Query parameter string used to filter games (e.g., `Call of Duty`, `Elden Ring`).

## Information Extracted
1. **Game Title** (`external`)
2. **Cheapest Historical/Current Price** (`cheapest`)
3. **Game ID** (`gameID`)
4. **Steam App ID** (`steamAppID`)

## How to Run
```bash
python main.py