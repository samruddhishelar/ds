import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Day": range(1, 61),
    "Sales": [
        1200, 1350, 1100, 1450, 1500,
        1250, 1600, 1400, 1550, 1300,
        1700, 1450, 1350, 1800, 1500,
        1650, 1400, 1550, 1750, 1600,
        1300, 1450, 1500, 1700, 1550,
        1800, 1650, 1400, 1500, 1750,
        1600, 1850, 1700, 1500, 1650,
        1800, 1550, 1450, 1750, 1600,
        1900, 1700, 1550, 1800, 1650,
        1500, 1750, 1600, 1850, 1700,
        1550, 1800, 1650, 1500, 1750,
        1600, 1850, 1700, 1800, 1650,
       
    ]
}

df = pd.DataFrame(data)

print("Daily Sales Data:")
print(df)




plt.boxplot(df["Sales"])

plt.title("Daily Sales Box Plot")
plt.xlabel("Daily Sales")
plt.ylabel("Sales Amount (₹)")

plt.show()