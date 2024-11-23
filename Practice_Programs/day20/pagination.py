import requests
import json

data_storage = []

URL = "https://jsonplaceholder.typicode.com/posts"
parameters = {"_page": 1, "_limit": 5}

for index in range(10):
    response = requests.get(URL, params=parameters)
    data_storage = json.dumps(response.json())
    parameters["_page"] += 1

with open("sample.json", "w") as file:
    json.dump(data_storage, file)
