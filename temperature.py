import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize


data = {
    "Temperature": [25, 28, 30, 32, 35],
    "Humidity": [60, 65, 70, 75, 80],
    "Wind-Speed": [10, 12, 15, 18, 20],
    "Pressure": [1010, 1012, 1015, 1018, 1020],
    "Rainfall": [5, 10, 15, 20, 25]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


minmax = MinMaxScaler()
minmax_data = minmax.fit_transform(df)

df_minmax = pd.DataFrame(
    minmax_data,
    columns=df.columns
)

print("\nMin-Max Scaling:")
print(df_minmax)





standard = StandardScaler()
standard_data = standard.fit_transform(df)

df_standard = pd.DataFrame(
    standard_data,
    columns=df.columns
)

print("\nStandardization:")
print(df_standard)




normal_data = normalize(df)

df_normal = pd.DataFrame(
    normal_data,
    columns=df.columns
)

print("\nNormalization:")
print(df_normal)