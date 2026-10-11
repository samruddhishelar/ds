import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


df = pd.read_csv("sport_performance.csv")

print("Dataset Information:")
print(df.info())

print("\nFirst 5 Records:")
print(df.head())



X = df[['Training_Hours_Per_Week']]
y = df['Performance_Score']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)




model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

prediction = model.predict([[6]])

print("prediction:",prediction)

r2 = r2_score(y_test, y_pred)

print("\nR2 Score:", r2)




plt.scatter(X, y)

plt.plot(X, model.predict(X))

plt.title("Training Hours vs Performance Score")
plt.xlabel("Training Hours Per Week")
plt.ylabel("Performance Score")

plt.show()