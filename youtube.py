import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df = pd.read_csv("USvideos.csv")
df


X = df[['likes']]
y = df['views']

model = LinearRegression()

model.fit(X, y)

y_pred = model.predict(X)

print("Actual Views:")
print(y.head())

print("\nPredicted Views:")
print(y_pred[:5])





plt.scatter(X, y)

plt.plot(X, y_pred)

plt.title("Likes vs Video Views")
plt.xlabel("Likes")
plt.ylabel("Views")

plt.show()