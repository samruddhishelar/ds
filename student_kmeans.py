import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


df = pd.read_csv("student_1.csv")

print("Student Dataset:")
print(df.head())

X = df[["Attendance", "Marks"]]

X = X.fillna(X.mean())



scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

df["Cluster"] = kmeans.fit_predict(X_scaled)

print("\nStudents with Cluster:")
print(df[["Student_ID", "Student_Name",
          "Attendance", "Marks", "Cluster"]])

centroids = scaler.inverse_transform(kmeans.cluster_centers_)

print("\nCluster Centroids:")
print(centroids)






plt.figure(figsize=(8, 6))

plt.scatter(
    df["Attendance"],
    df["Marks"],
    c=df["Cluster"],
    s=60
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="X",
    s=200,
    label="Centroids"
)

plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.title("K-Means Clustering of Students")
plt.legend()

plt.show()