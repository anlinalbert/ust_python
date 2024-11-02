def get_schools():
    """Function to get school names and their count."""
    schools = {}
    with open("sample.csv", "r") as file:
        for line in file:
            extracted_school = line.split(",")[1]
            if extracted_school in schools:
                schools[extracted_school] += 1
            else:
                schools[extracted_school] = 1
    return schools


print(f"Details: {get_schools()}")
