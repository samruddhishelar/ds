import matplotlib.pyplot as plt
import pandas as pd

data={

'payment_methods': ["UPI", "Credit_Card", "Debit_Card", "Cash", "Net_Banking"],
'customers' : [150, 80, 60, 40, 30]

}

df = pd.DataFrame(data)
print(df)


plt.pie(
    df['customers'],
    labels=df['payment_methods'].values,
    autopct='%1.1f%%'
)

plt.title("Customer Preferred Payment Methods")

plt.show()