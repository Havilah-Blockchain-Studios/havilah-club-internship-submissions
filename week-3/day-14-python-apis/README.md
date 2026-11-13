# Day 14 - Python and APIs

## API Selected
- **Name:** NASA Astronomy Picture of the Day (APOD)
- **Category:** Science

## What the Program Does
This program connects to the NASA APOD API, securely loads an API key using a local `.env` file, handles network requests with `requests`, checks status codes gracefully, and prints out clean, formatted space data.

## Endpoint and Parameters Used
- **Endpoint:** `https://api.nasa.gov/planetary/apod`
- **Parameters:** `api_key` (Loaded securely via `os.getenv("API_KEY")`)


## Extracted Information
The program extracts and displays:
1. Title of the astronomical entry
2. Date of publication
3. Media Type (image or video)
4. Direct URL link