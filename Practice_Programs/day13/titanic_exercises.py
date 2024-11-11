import pandas as pd

titanic = pd.read_csv(r"../datasets/titanic.csv")

print(titanic.groupby("Survived")["Age"].agg(["mean"]).reset_index())

