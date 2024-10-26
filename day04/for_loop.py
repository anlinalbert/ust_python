def print_username(input_username, no_of_times):
    """Function to print username multiple times."""
    for _ in range(no_of_times):
        print(input_username)


username = input("Enter username: ")
times = int(input("Enter no.of times: "))
print(f"\nPrinting username for {times} times:")

print_username(username, times)
