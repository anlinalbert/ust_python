def get_schools():
    """Function to get school names and their count."""
    schools = {}
    with open("sample.csv", "r") as file:
        for line in file:
            if line.strip():
                extracted_school = line.strip().split(",")[1]
                schools[extracted_school] = schools.get(extracted_school, 0) + 1
    return schools


print(f"Details: {get_schools()}")
