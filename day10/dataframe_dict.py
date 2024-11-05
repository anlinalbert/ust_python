import pandas as pd

names = pd.Series(["James", "Jack", "Joe"])
scores = pd.Series([25, 44, 10])

df = pd.DataFrame({"Name": names, "Score": scores})

# Print by rows
for index, value in df.iterrows():
    print(f"---------------------\nIndex: {index}\nValue:\n{value}")

# Print by columns
for column, value in df.iteritems():
    print(f"---------------------\nColumn name: {column}\nValue:\n{value}")

# Accessing via loc
print(df.loc[:, "Name"])
