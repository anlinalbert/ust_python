import pandas as pd

df_one = pd.DataFrame({"Name": ["Joy", "Alice", "Sam"], "Age": [26, 22, 32]})
df_two = pd.DataFrame({"Name": ["Jack", "Tom"], "Age": [30, 18]})

# Two ways to modify data
df_one.loc[df_one["Name"] == "Alice", "Age"] = 25
df_one.at[1, "Age"] = 30

# Print concatenated dataframe
print(pd.concat([df_one, df_two], ignore_index=True))
