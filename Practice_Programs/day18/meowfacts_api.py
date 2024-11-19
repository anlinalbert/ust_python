import requests

URL = "https://meowfacts.herokuapp.com/"


def get_one_random_fact():
    return requests.get(URL)


def get_multiple_facts(number):
    new_url = URL + f"?count={number}"
    return requests.get(new_url)


def get_fact_in_new_language(language):
    new_url = URL + f"?{language}"
    return requests.get(new_url)


# Getting one random cat fact
response = get_one_random_fact()
if response.status_code == 200:
    print(response.json()["data"][0])

# Getting multiple cat facts
user_input = int(input("Enter the fact count: "))
response = get_multiple_facts(user_input)
if response.status_code == 200:
    cat_facts = response.json()["data"]
    for index, fact in enumerate(cat_facts):
        print(f"{index + 1}: {fact}")

# Cat fact in another language
user_input = input("Enter a language code: ")
response = get_fact_in_new_language(user_input)
if response.status_code == 200:
    print(f"{user_input}: {response.json()['data'][0]}")
