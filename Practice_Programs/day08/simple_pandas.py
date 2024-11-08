import pandas as pd

# Initializing a dictionary template
data = {"Name": [], "Age": []}


def add_data():
    """Function to add new data to dictionary."""
    name = input("Enter a name: ")
    age = int(input("Enter the age: "))

    data["Name"].append(name)
    data["Age"].append(age)


def print_dataframe():
    """Function to return a dataframe."""
    print(f"Dataframe: {pd.DataFrame(data)}")


menu = {
    "1": add_data,
    "2": print_dataframe
}

while True:
    print("MENU DRIVEN PGM\n1. Add data to dictionary\n2. Print dataframe\n3. Exit")
    user_choice = input("Select an option: ")
    function_name = menu.get(user_choice)

    if user_choice == "3":
        print("Program exit.")
        break

    try:
        function_name()
    except Exception as _:
        print("Invalid Input.\n")
