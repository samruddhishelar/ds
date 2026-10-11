import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    "Age": [22, 25, 28, 30, 35],
    "Salary": [25000, 30000, 35000, 40000, 50000],
    "Experience": [1, 3, 5, 7, 10],
    "Working_Hours": [8, 8, 9, 9, 10],
    "Performance_Score": [60, 70, 75, 85, 90]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)



scaler = StandardScaler()

standardized_data = scaler.fit_transform(df)

df_standardized = pd.DataFrame(
    standardized_data,
    columns=df.columns
)

print("\nStandardized Data:")
print(df_standardized)