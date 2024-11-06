import pandas as pd

df = pd.read_csv(r"../datasets/titanic.csv")

print(df['Age'].head())  # Print first 5 rows of "Age"
print(df[["Age", "Sex"]].head())  # Subset rows
print(df[df["Age"] < 25])  # People whose age less than 25
print(len(df.index))  # Length of dataframe
print(df["Age"].mean())  # Avg age

# Creating a filter for fare
fare_filter = df[(df["Sex"] == "male") & (df["Age"] < 25)]
print(f'{fare_filter["Fare"].mean():.2f}')
fare_filter.to_csv("output.csv", index=False)

# Percentage of survived passengers
print(f'{df["Survived"].mean() * 100:.2f}')
