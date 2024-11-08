def odd_even(number):
    """Function to check whether a number is odd or even."""
    return "even" if number % 2 == 0 else "odd"


user_input = int(input("Enter a number: "))
print(f"Number {user_input} is {odd_even(user_input)}.")
