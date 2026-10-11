#!pip install squarify


import pandas as pd
import matplotlib.pyplot as plt
import squarify


data = {
    "City": ["Mumbai", "Delhi", "Pune", "Bangalore", "Chennai"],
    "Population": [20.7, 19.5, 7.0, 12.3, 11.2],
    "GDP": [310, 293, 69, 110, 78],
    "Literacy Rate": [89.7, 86.2, 89.4, 88.7, 90.2]
}

df = pd.DataFrame(data)

print("City Data:")
print(df)





plt.figure(figsize=(8, 6))

squarify.plot(
    sizes=df["Population"],
    label=df["City"],
    alpha=0.8
)

plt.title("City-wise Population Distribution")
plt.axis("off")
plt.show()




fig = plt.figure(figsize=(9, 6))

ax = fig.add_subplot(111, projection="3d")

ax.scatter(
    df["Population"],
    df["GDP"],
    df["Literacy Rate"],
    s=80
)

ax.set_xlabel("Population (Million)")
ax.set_ylabel("GDP")
ax.set_zlabel("Literacy Rate (%)")

ax.set_title("3D Scatter Plot of City Data")

plt.show()