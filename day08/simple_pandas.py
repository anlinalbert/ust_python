import pandas as pd

# Initializing a dictionary template
data = {"Name": [], "Age": []}


def add_data():
    """Function to add new data to dictionary."""
    name = input("Enter a name: ")
    age = int(input("Enter the age: "))

    data["Name"].append(name)
    data["Age"].append(age)


def return_dataframe():
    """Function to return a dataframe."""
    return pd.DataFrame(data)


menu = {
    "1": add_data,
    "2": return_dataframe
}

while True:
    print("MENU DRIVEN PGM\n1. Add data to dictionary\n2. Print dataframe\n3. Exit")
    user_choice = input("Select an option: ")
    function_name = menu.get(user_choice)

    if user_choice == "1":
        try:
            function_name()
        except Exception as _:
            print("Error occurred.")
    elif user_choice == "2":
        print(f"Dataframe:\n{function_name()}\n")
    elif user_choice == "3":
        print("Program exit.")
        break
    else:
        print("Invalid choice. Retry")
