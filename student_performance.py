import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Study Hours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Attendance": [60, 65, 70, 75, 80, 82, 85, 90, 92, 95],
    "Assignment Score": [50, 55, 60, 65, 70, 75, 78, 85, 90, 95],
    "Exam Score": [45, 50, 58, 62, 68, 72, 76, 84, 89, 94]
}

df = pd.DataFrame(data)

print("Student Performance Data:")
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

plt.title("Correlation Heat Map of Student Performance")
plt.xlabel("Attributes")
plt.ylabel("Attributes")

plt.show()