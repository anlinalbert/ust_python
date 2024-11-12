# Create a program to read a file which contains large set of some noval.
# Get the frequencies of all words in the file and finally show the frequencies
# for each word in a pandas dataframe.

import pandas as pd
import re
from collections import Counter


def filter_only_characters(data):
    """Function to filter out words only."""
    return re.findall(r"\b[\w’-]+\b", data.lower())


def word_count(data):
    """Function to get each word count."""
    return Counter(data)


try:
    with open("novel.csv", "r", encoding="utf8") as file:
        file_data = file.read()
except FileNotFoundError:
    print("'noval.txt' file not found.")

file_data = filter_only_characters(file_data)
word_count_data = word_count(file_data)

# Final dataframe
print(pd.DataFrame(list(word_count_data.items()), columns=["Word", "Count"]))
