import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Department': ['HR', 'Finance', 'IT', 'Sales', 'Marketing'],
    'Employees': [20, 30, 50, 40, 25]
}

df = pd.DataFrame(data)

print("Employee Data:")
print(df)



plt.bar(df['Department'], df['Employees'])

plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.title("Distribution of Employees Among Departments")

plt.show()