import pandas as pd
from sklearn.preprocessing import LabelEncoder


df1 = pd.DataFrame({
    'Brand': ['Samsung', 'Apple', 'OnePlus'],
    'Model': ['S23', 'iPhone15', 'Nord'],
    'Price': [70000, 80000, 30000],
    'RAM': [8, 6, 8]
})


df2 = pd.DataFrame({
    'Model': ['S23', 'iPhone15', 'Nord'],
    'Storage': [256, 128, 128],
    'Battery_Capacity': [3900, 3349, 5000],
    'Operating_System': ['Android', 'iOS', 'Android']
})

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)



merged = pd.merge(df1, df2, on='Model')

print("\nMerged DataFrame:")
print(merged)





le = LabelEncoder()
merged['Brand'] = le.fit_transform(merged['Brand'])

merged = pd.get_dummies(
    merged,
    columns=['Operating_System'],
    dtype=int
)

print("\nTransformed DataFrame:")
print(merged)
