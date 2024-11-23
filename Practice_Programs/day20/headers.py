import requests

URL = "https://httpbin.org/headers"
custom_header = {"username": "anlinalbert"}

response = requests.get(URL, headers=custom_header)

if response.status_code == 200:
    print("Success")
