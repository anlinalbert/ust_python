def get_line_data(target_school):
    """Function to get line data from file based on input."""
    with open("sample.csv", "r") as file:
        for line in file:
            extracted_school = line.split(",")[1]
            if target_school == extracted_school.lower():
                return line


school = input("Enter target school: ")
print(f"Details: {get_line_data(school)}")
