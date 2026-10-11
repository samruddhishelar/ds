import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules


transactions = [
    ['Video Lecture', 'Quiz'],
    ['Video Lecture', 'Assignment'],
    ['Quiz', 'Discussion Forum'],
    ['Video Lecture', 'Quiz', 'Assignment'],
    ['Assignment', 'Discussion Forum'],
    ['Video Lecture', 'Certificate'],
    ['Quiz', 'Certificate'],
    ['Video Lecture', 'Quiz'],
    ['Assignment', 'Certificate'],
    ['Video Lecture', 'Quiz', 'Certificate']
]

te = TransactionEncoder()
data = te.fit(transactions).transform(transactions)
df = pd.DataFrame(data, columns=te.columns_)

print("Transaction Data:")
print(df)




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