def remove_vowels(input_text):
    """Function to remove vowels from a string."""
    return ''.join([char for char in input_text if char not in set("aeiouAEIOU")])  # Do you know why I used a set?


print(f"New text: {remove_vowels(input('Enter a string: '))}")
