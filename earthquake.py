import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Location':["punr","mumbai","Delhi","Chennai","kolkata","Gujrat"],
    'Latitude': [19.07, 28.61, 23.02, 13.08, 22.57, 18.52],
    'Longitude': [72.87, 77.20, 72.57, 80.27, 88.36, 73.85],
    'Depth': [10, 15, 20, 12, 25, 18],
    'Magnitude': [4.2, 5.1, 3.8, 6.0, 4.7, 5.5]
}

df = pd.DataFrame(data)

print("Earthquake Data:")
print(df)



import plotly.express as px
fig = px.scatter_geo(df,
                     lat = 'Latitude',
                     lon='Longitude',
                     hover_name = 'Location',
                     color = 'Magnitude',
                     size='Magnitude',
                     title = 'Earthquake',
                     projection='natural earth'
                     )
fig.show(renderer = "browser")





plt.figure(figsize=(8, 6))

plt.scatter(
    df['Longitude'],
    df['Latitude'],
    c=df['Magnitude'],
    cmap='viridis',
    s=100
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Earthquake Locations and Magnitude")

plt.colorbar(label="Magnitude")

plt.show()