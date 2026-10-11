import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Fuel_Efficiency': [20, 22, 21, 23, 50],
    'Engine_Power': [100, 110, 105, 115, 250],
    'Vehicle_Weight': [1200, 1300, 1250, 1350, 1400],
    'Engine_Size': [1.5, 1.6, 1.5, 1.7, 2.0],
    'Acceleration': [10, 9, 9.5, 8.5, 7]
}

df = pd.DataFrame(data)

print("Vehicle Data:")
print(df)



plt.boxplot(df['Fuel_Efficiency'])
plt.title("Fuel Efficiency Box Plot")
plt.ylabel("Fuel Efficiency")
plt.show()


plt.boxplot(df['Engine_Power'])
plt.title("Engine Power Box Plot")
plt.ylabel("Engine Power")
plt.show()