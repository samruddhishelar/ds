import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

data = {
    'Customer_ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Netflix': [1, 1, 1, 0, 0, 1, 0, 1],
    'Amazon_Prime': [1, 0, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

print("Customer Data:")
print(df)





both = ((df['Netflix'] == 1) & (df['Amazon_Prime'] == 1)).sum()
only_netflix = ((df['Netflix'] == 1) & (df['Amazon_Prime'] == 0)).sum()
only_amazon = ((df['Netflix'] == 0) & (df['Amazon_Prime'] == 1)).sum()

print("\nOnly Netflix:", only_netflix)
print("Only Amazon Prime:", only_amazon)
print("Both:", both)




venn2(
    subsets=(only_netflix, only_amazon, both),
    set_labels=('Netflix', 'Amazon Prime')
)

plt.title("Netflix and Amazon Prime Customers")
plt.show()




labels = ['Only Netflix', 'Only Amazon Prime', 'Both']
values = [only_netflix, only_amazon, both]

plt.pie(
    values,
    labels=labels,
    autopct='%1.1f%%'
)

plt.title("Customer Subscription Distribution")
plt.show()
