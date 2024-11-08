def find_middle_char(s):
    """Function to find the middle character of a string."""
    middle_index = len(s) // 2
    return s[middle_index]


def reverse_string(s):
    """Function to reverse a string."""
    return s[::-1]


print(find_middle_char("Superman"))
print(reverse_string("Batman"))
