import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Transport': ["Train", "Bicycle", "Bike", "Car", "Bus"],
    'Employees': [220, 60, 70, 80, 40]
}

df = pd.DataFrame(data)

print(df)



plt.pie(
    df['Employees'],
    labels=df['Transport'],
    autopct='%1.1f%%',
    colors=['red', 'blue', 'green', 'orange', 'purple']
)

plt.title("Preferred Mode of Transportation")
plt.show()



