import pandas as pd
from sklearn.preprocessing import MinMaxScaler


data = {
    'Product_ID': [101, 102, 103, 104, 105],
    'Price': [100, 200, 150, 300, 250],
    'Quantity_Sold': [20, 15, 30, 10, 25],
    'Discount': [5, 10, 8, 15, 12],
    'Revenue': [1900, 2700, 4140, 2550, 5500]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)





scaler = MinMaxScaler()

df_scaled = pd.DataFrame(
    scaler.fit_transform(df),
    columns=df.columns
)

print("\nData After Min-Max Scaling:")
print(df_scaled)