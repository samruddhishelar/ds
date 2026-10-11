import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    'Customer_ID': [1, 2, 3, 4, 5],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Mumbai'],
    'Membership_Type': ['Gold', 'Silver', 'Gold', 'Bronze', 'Silver']
}

customer_DataFrame = pd.DataFrame(data)

print("Before Encoding:")
print(customer_DataFrame)



encoder = LabelEncoder()

customer_DataFrame['Gender'] = encoder.fit_transform(
    customer_DataFrame['Gender']
)

customer_DataFrame['City'] = encoder.fit_transform(
    customer_DataFrame['City']
)

customer_DataFrame['Membership_Type'] = encoder.fit_transform(
    customer_DataFrame['Membership_Type']
)

print("\nAfter Label Encoding:")
print(customer_DataFrame)