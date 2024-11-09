import pandas as pd

df_one = pd.DataFrame({"Name": ["Joy", "Alice", "Sam"], "City": ["NYC", "IND", pd.NA]})
df_two = pd.DataFrame({"Name": ["Jack", "Tom"], "City": ["NY", "COC"]})

final_data = pd.concat([df_one, df_two], ignore_index=True)

final_data["City"].fillna("OUT", inplace=True)

print(final_data["City"].value_counts())
