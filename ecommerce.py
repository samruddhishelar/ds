import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("Ecommerce_Customers.csv")

print("Dataset:")
print(df.head())



print("\nMissing Values:")
print(df.isnull().sum())




X = df[['Avg. Session Length',
        'Time on App',
        'Time on Website',
        'Length of Membership']]

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

df['Cluster'] = kmeans.fit_predict(X)

print("\nCustomer Clusters:")
print(df[['Avg. Session Length',
          'Time on App',
          'Time on Website',
          'Length of Membership',
          'Cluster']].head(20))