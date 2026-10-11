import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Temperature": [25, 27, 29, 31, 30, 28, 26, 24, 23, 22],
    "Humidity": [65, 60, 55, 50, 52, 58, 63, 68, 72, 75],
    "Rainfall": [10, 5, 2, 0, 1, 4, 8, 15, 20, 25],
    "Wind Speed": [12, 14, 15, 18, 16, 13, 11, 10, 9, 8]
}

df = pd.DataFrame(data)

print("Weather DataFrame:")
print(df)

correlation = df.corr()

print("\nCorrelation Matrix:")
print(correlation)





plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heat Map of Weather Parameters")
plt.xlabel("Weather Parameters")
plt.ylabel("Weather Parameters")

plt.show()