import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


data = {
    "Product_name": [
        "Laptop", "Mobile", "Tablet", "Headphones",
        "Smartwatch", "Camera", "Speaker", "Monitor"
    ],
    "Price": [60000, 25000, 30000, 5000, 8000, 45000, 7000, 20000],
    "Rating": [4.5, 4.3, 4.2, 4.0, 4.1, 4.6, 3.9, 4.4],
    "Number_of_Sales": [500, 1200, 800, 2000, 1500, 400, 1800, 900]
}

df = pd.DataFrame(data)

print("Product DataFrame:")
print(df)





X = df[["Price", "Rating", "Number_of_Sales"]]

linked = linkage(X, method="ward")

plt.figure(figsize=(10, 6))

dendrogram(
    linked,
    labels=df["Product_name"].values
)

plt.title("Dendrogram of Similar Products")
plt.xlabel("Products")
plt.ylabel("Distance")

plt.show()