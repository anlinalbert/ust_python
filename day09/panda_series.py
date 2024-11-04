import pandas as pd

series_a = pd.Series([1, 2, 3, 4, 5], index=list("abcde"))
series_b = pd.Series([1, 4, 5], index=list("abc"))

print(series_a.add(series_b, fill_value=0))
print(series_a.head(2))
