def odd_even(number):
    """Function to check whether a number is odd or even."""
    return "even" if number % 2 == 0 else "odd"


print(f"Number 5 is {odd_even(5)}.")
print(f"Number 10 is {odd_even(10)}.")
