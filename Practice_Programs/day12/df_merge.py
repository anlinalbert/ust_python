import pandas as pd


def odd_even(data):
    """Function to check if number is odd or even."""
    return True if data % 2 == 0 else False


pd_one = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Joe"], "Birth City": ["NY", "IND", "COC"]})
pd_two = pd.DataFrame({"ID": [1, 2, 3, 4], "Work City": ["TVM", "TVM", "TVM", "TVM"], "Experience": [12, 23, pd.NA, 3]})

pd_one = pd.concat([pd_one, pd.DataFrame({"ID": [4], "Name": ["Catie"], "Birth City": ["JPN"]})], ignore_index=True)

final_data = pd.merge(pd_one, pd_two, on="ID")

final_data.at[2, "Experience"] = final_data["Experience"].mean()

# Apply usage
final_data["Is Even"] = final_data["Experience"].apply(odd_even)

print(final_data)
