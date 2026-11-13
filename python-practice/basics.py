import requests
url = "https://www.7timer.info/bin/api.pl"

params = {
    "lon": 7.0723,
    "lat": 6.2105,
    "product": "civillight",
    "output": "json",
    "unit": "metric"
}
try:
    response = requests.get(
    url,
    params=params,
    timeout=10
)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
          print("The API returned an error:", response.status_code)

except requests.exceptions.RequestException:
    print("Could not connect to the API.")

