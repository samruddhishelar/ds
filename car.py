import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Car_Model': ['Car A', 'Car B', 'Car C', 'Car D', 'Car E'],
    'Engine_Size': [1.2, 1.5, 1.8, 2.0, 2.5],
    'Fuel_Efficiency': [20, 18, 16, 14, 11]
}

df = pd.DataFrame(data)

print("Car Data:")
print(df)




plt.scatter(
    df['Engine_Size'],
    df['Fuel_Efficiency'],
    c=['red', 'blue', 'green', 'orange', 'purple']
)

plt.title("Engine Size vs Fuel Efficiency")
plt.xlabel("Engine Size (Litres)")
plt.ylabel("Fuel Efficiency (km/L)")

plt.show()