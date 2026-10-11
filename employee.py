import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106, 107, 108, 108],
    "Age": [25, 30, 28, None, 35, 42, 29, 31, 31],
    "Dept": ["IT", "HR", "Sales", "IT", "HR", None, "Sales", "IT", "IT"],
    "Years_Experience": [2, 5, 3, 7, 10, 15, 4, 6, 6],
    "Performance_Rating": [4, 5, 3, 4, 5, 4, None, 3, 3]
}

employee_data = pd.DataFrame(data)

print("Original Employee Data:")
print(employee_data)





employee_data["Age"] = employee_data["Age"].fillna(
    employee_data["Age"].mean()
)

employee_data["Dept"] = employee_data["Dept"].fillna(
    employee_data["Dept"].mode()[0]
)

employee_data["Performance_Rating"] = employee_data[
    "Performance_Rating"
].fillna(employee_data["Performance_Rating"].mean())

print("\nAfter Handling Missing Values:")
print(employee_data)





employee_data = employee_data.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(employee_data)




Q1 = employee_data["Years_Experience"].quantile(0.25)
Q3 = employee_data["Years_Experience"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = employee_data[
    (employee_data["Years_Experience"] < lower_limit) |
    (employee_data["Years_Experience"] > upper_limit)
]

print("\nOutliers:")
print(outliers)

print("\nFinal Cleaned Data:")
print(employee_data)
