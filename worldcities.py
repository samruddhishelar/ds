import pandas as pd
import matplotlib.pyplot as plt
import squarify


df = pd.read_csv("worldcities.csv")

print("World Cities Data:")
print(df.head())



map_data = df[df["population"] > 0].dropna(
    subset=["latitude", "longitude", "population"]
)

plt.figure(figsize=(12, 6))

plt.scatter(
    map_data["longitude"],
    map_data["latitude"],
    s=map_data["population"] / 100000,
    alpha=0.5
)

plt.title("World Cities - Population Visualization")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.grid()
plt.show()





top_cities = map_data.sort_values(
    "population",
    ascending=False
).head(20)

plt.figure(figsize=(12, 7))

squarify.plot(
    sizes=top_cities["population"],
    label=top_cities["city"],
    alpha=0.8
)

plt.title("Population Distribution of World Cities")
plt.axis("off")

plt.show()