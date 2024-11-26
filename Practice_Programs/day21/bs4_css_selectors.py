import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")


# Method 1
master_class = soup.find(class_="quote")
quote_obj = master_class.find(class_="text")  # Getting text class inside quote class
author_obj = master_class.find(class_="author")  # Getting author class inside quote class

print(f"{quote_obj.text.strip()}\n{author_obj.text.strip()}")

# Better method
quote_obj = soup.select(".quote .text")
author_obj = soup.select(".quote .author")

for quote, author in zip(quote_obj, author_obj):    # The zip method pairs two items together
    print(f"{quote.text.strip()} - {author.text.strip()}\n")

    # Writing quotes to a txt file
    with open("quotes.txt", "a") as file:
        file.write(f"{quote.text.strip()} - {author.text.strip()}\n")
