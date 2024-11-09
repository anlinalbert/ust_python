import pandas as pd

data = {
    "Store": ["Store1", "Store1", "Store2", "Store2", "Store3", "Store3", "Store4", "Store5"],
    "Region": ["North", "North", "South", "South", "East", "East", "North", "South"],
    "Sales": [200, 150, 300, 250, 400, 350, 100, 200]
}

df = pd.DataFrame(data)

# Print sum by grouping
print(df.groupby("Store")["Sales"].sum())
region_data = df.groupby("Region")["Sales"].sum().reset_index()

# Merging
df = pd.merge(df, region_data, on="Region", how="left", suffixes=("_Store", "_Region"))
print(df)

# df["SalesByRegion"] = df[df.groupby("Store")["Sales"].sum()] / df["Sales_Region"] * 100
# print(df)
