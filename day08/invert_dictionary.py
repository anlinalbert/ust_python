def invert_dictionary(user_dictionary):
    """Function to invert a dictionary."""
    inverted_dictionary = {}
    for key, value in user_dictionary.items():
        inverted_dictionary.setdefault(value, []).append(key)   # Deals with duplicate items also
    return inverted_dictionary


simple_dictionary = {1: "Anlin", 2: "Geo"}
print(f"Inverted dictionary: {invert_dictionary(simple_dictionary)}")
