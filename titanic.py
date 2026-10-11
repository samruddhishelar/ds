import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("titanic.csv")

print("Titanic Dataset:")
print(df.head())


plt.hist(df['Pclass'], bins=3, edgecolor='black')

plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.title("Number of Passengers in Each Passenger Class")
plt.show()





survival = df['Survived'].value_counts()

plt.pie(
    survival,
    labels=['Did Not Survive', 'Survived'],
    autopct='%1.1f%%'
)

plt.title("Titanic Survival Distribution")
plt.show()