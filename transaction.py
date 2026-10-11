import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules


transactions = [
    ['Basmati Rice', 'Toor Dal', 'Turmeric Powder', 'Cooking Oil'],
    ['Atta', 'Sugar', 'Tea', 'Milk'],
    ['Rice', 'Moong Dal', 'Salt', 'Cooking Oil'],
    ['Wheat Flour', 'Chickpeas', 'Turmeric Powder', 'Cumin Seeds'],
    ['Poha', 'Peanuts', 'Onions', 'Cooking Oil'],
    ['Basmati Rice', 'Paneer', 'Garam Masala', 'Tomatoes'],
    ['Atta', 'Potatoes', 'Onions', 'Cooking Oil']
]

te = TransactionEncoder()
data = te.fit(transactions).transform(transactions)
df = pd.DataFrame(data, columns=te.columns_)

print("Transaction Data:")
print(df)




print("\nMissing Values:")
print(df.isnull().sum())



frequent_03 = apriori(df, min_support=0.3, use_colnames=True)

print("\nFrequent Itemsets - Support 0.3:")
print(frequent_03)

rules_03 = association_rules(
    frequent_03,
    metric="confidence",
    min_threshold=0.5
)

print("\nAssociation Rules - Support 0.3:")
print(rules_03[['antecedents', 'consequents',
                'support', 'confidence']])






frequent_04 = apriori(df, min_support=0.4, use_colnames=True)

print("\nFrequent Itemsets - Support 0.4:")
print(frequent_04)

rules_04 = association_rules(
    frequent_04,
    metric="confidence",
    min_threshold=0.5
)

print("\nAssociation Rules - Support 0.4:")
print(rules_04[['antecedents', 'consequents',
                'support', 'confidence']])
