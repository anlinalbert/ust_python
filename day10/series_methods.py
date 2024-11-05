import pandas as pd

series_a = pd.Series([1, 2, 3, 4, 5], index=list("abcde"))
series_b = pd.Series([1, 4, 5], index=list("abc"))

# Some important functions
print(series_a.value_counts())
print((series_b.between(2, 4)))
