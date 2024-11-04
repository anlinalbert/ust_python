import pandas as pd

student_series = pd.Series({"Anlin": 97, "Alice": 85, "Jock": 44, "RRR": 68})

print(student_series.iloc[2])   # Based on values
print(student_series.loc["RRR"])    # Based on index
print(student_series[student_series > 80])  # Students whose marks greater than 80
