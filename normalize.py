import pandas as pd
from sklearn.preprocessing import Normalizer


data = {
    "City": ["Pune", "Mumbai", "Delhi", "Nashik", "Nagpur"],
    "House_Type": ["1BHK", "2BHK", "3BHK", "1BHK", "2BHK"],
    "House_Area": [600, 900, 1200, 550, 850],
    "Number_of_Rooms": [2, 3, 4, 2, 3],
    "Monthly_Rent": [12000, 25000, 40000, 10000, 22000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)




numerical_data = df[
    ["House_Area", "Number_of_Rooms", "Monthly_Rent"]
]

scaler = Normalizer()
normalized_data = scaler.fit_transform(numerical_data)

# Create normalized DataFrame
df_normalized = pd.DataFrame(
    normalized_data,
    columns=["House_Area", "Number_of_Rooms", "Monthly_Rent"]
)


print("\nNormalized Data:")
print(df_normalized)



