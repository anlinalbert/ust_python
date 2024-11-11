import pandas as pd

titanic = pd.read_csv(r"../datasets/titanic.csv")

# Compare the average of age of passengers based on "Survived"
print(titanic.groupby("Survived")["Age"].agg(["mean"]).reset_index())

# Calculate survival rate by gender
gender_survival = titanic.groupby("Sex")["Survived"].agg(["mean"]).reset_index()
gender_survival["mean"] = gender_survival["mean"] * 100
print(gender_survival)

