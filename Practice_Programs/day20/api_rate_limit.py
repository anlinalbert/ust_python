import time
import requests

URL = "https://api.open-meteo.com/v1/forecast"
parameters = {
    "latitude": 12.9719,
    "longitude": 77.5937,
    "current_weather": "true"
}

for request in range(100):
    response = requests.get(URL, params=parameters)
    print(f"{request}: {response.status_code}")

    if response.status_code == 200:
        print("Success")
    elif response.status_code == 429:   # Rate limit code
        print("API rate limit reached")
        time.sleep(60)
    else:
        print("Error")
