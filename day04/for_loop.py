def print_username(username, times):
    """Function to print username multiple times."""
    print(f"\nPrinting username for {times} times:")
    for _ in range(0, times):
        print(username)


print_username(input("Enter username: "), int(input("Enter no.of times: ")))
