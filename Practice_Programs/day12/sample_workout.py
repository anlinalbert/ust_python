import pandas as pd

data = {
    "Store": ["Store1", "Store1", "Store2", "Store2", "Store3", "Store3"],
    "Region": ["North", "North", "South", "South", "East", "East"],
    "Sales": [200, 150, 300, 250, 400, 350]
}

df = pd.DataFrame(data)

# Print sum by grouping
print(df.groupby("Store")["Sales"].sum())
region_data = df.groupby("Region")["Sales"].sum().reset_index()
print(region_data)


df.merge(df, region_data, on="Region", how="left")
