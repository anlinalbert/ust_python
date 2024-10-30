import re


def match_numbers(text):
    """Function to capture all numbers."""
    return re.findall(r'\d+', text, re.IGNORECASE)


def find_with_starting_letter(text, letter):
    """Function to capture words starting with input letter."""
    return re.findall(rf"\b{letter}\w*", text, re.IGNORECASE)


user_input = input("Enter a string: ")
starting_letter = input("Enter starting letter: ")
print(f"Matches: {match_numbers(user_input)}")
print(f"Matches: {find_with_starting_letter(user_input, starting_letter)}")
