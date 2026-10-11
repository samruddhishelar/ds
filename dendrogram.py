import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Price': [100, 120, 500, 520, 150],
    'Rating': [4.2, 4.5, 4.8, 4.7, 4.1],
    'Sales': [200, 220, 500, 480, 250]
}


df = pd.DataFrame(data)

print("Product Data:")
print(df)


X = df[['Price', 'Rating', 'Sales']]


linked = linkage(X, method='ward')


plt.figure(figsize=(8, 5))
dendrogram(linked, labels=df['Product'].values)

plt.title("Dendrogram of Products")
plt.xlabel("Products")
plt.ylabel("Distance")

plt.show()