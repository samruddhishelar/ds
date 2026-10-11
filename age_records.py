import pandas as pd


data = {
    'Person_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [18, 22, 25, 30, 35, 40, 45, 50, 55, 60]
}

age_records = pd.DataFrame(data)


print("Original Data:")
print(age_records)



age_records['Age_Group'] = pd.cut(
    age_records['Age'],
    bins=3,
    labels=['Young', 'Middle', 'Old']
)

print("\nDiscretized Data:")
print(age_records)