import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Create dataset
data = {
    'Age': [25, 32, 45, 28, 40, 35, 50, 29, 38, 42],
    'Income': [30000, 45000, 70000, 35000, 65000, 50000, 80000, 40000, 60000, 75000],
    'Credit_Score': [650, 720, 780, 680, 750, 700, 800, 660, 740, 770],
    'Loan_Amount': [100000, 150000, 250000, 120000, 200000,
                    180000, 300000, 130000, 220000, 270000],
    'Employment_Years': [2, 5, 15, 3, 10, 7, 20, 4, 8, 12],
    'Debt_Ratio': [0.45, 0.30, 0.20, 0.50, 0.25,
                   0.35, 0.15, 0.48, 0.28, 0.22],
    'Loan_Status': [0, 1, 1, 0, 1, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)



print("Loan Application Data:")
print(df)

print("\nSelected Important Features:")

selected = df[['Income', 'Credit_Score', 'Loan_Amount']]

print(selected)





features = df[['Age', 'Income', 'Credit_Score',
               'Loan_Amount', 'Employment_Years', 'Debt_Ratio']]

scaler = StandardScaler()
scaled_data = scaler.fit_transform(features)

pca = PCA(n_components=2)
result = pca.fit_transform(scaled_data)

print("\nPCA Reduced Data:")
print(result)

