import re


def match_numbers(text):
    """Function to capture all numbers."""
    return re.findall(r'\d+', text, re.IGNORECASE)


def find_with_starting_letter(text, letter):
    """Function to capture words starting with input letter."""
    return re.findall(rf"\b{letter}\w*", text, re.IGNORECASE)


def capture_date(text):
    """Function to capture dates from a string. Format: yyyy-mm-dd or yyyy/mm/dd."""
    return re.findall(r"\d{4}[-/]\d{2}[-/]\d{2}", text)


user_input = input("Enter a string: ")
starting_letter = input("Enter starting letter: ")
print(f"Matches: {match_numbers(user_input)}")
print(f"Matches: {find_with_starting_letter(user_input, starting_letter)}")
print(f"Matches: {capture_date(user_input)}")
