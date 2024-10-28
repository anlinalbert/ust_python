def process_data(number_one, number_two, user_choice):
    if user_choice == "1":
        return number_one + number_two
    elif user_choice == "2":
        return number_one * number_two


def calculator():
    while True:
        print("Calculator\n1. Add\n2. Multiply\n3.Exit")
        user_choice = input("Enter a choice: ")
        if user_choice in ("1", "2"):
            try:
                number_one = float(input("Enter number 1: "))
                number_two = float(input("Enter number 2: "))
            except Exception as _:
                print("Error!")
                continue

            if user_choice == "1":
                print(f"Add: {process_data(number_one, number_two, user_choice)}")
            elif user_choice == "2":
                print(f"Multiply: {process_data(number_one, number_two, user_choice)}")
        elif user_choice == "3":
            print("Program exit.")
            break
        else:
            print("Invalid choice.")


calculator()
