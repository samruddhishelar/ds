import pandas as pd


data = {
    "Book_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Book_Price": [150, 250, 300, 450, 500, 650, 700, 850, 900, 1000]
}

book_records = pd.DataFrame(data)


print("Original Data:")
print(book_records)

book_records["Price_Bin"] = pd.cut(
    book_records["Book_Price"],
    bins=3,
    labels=["Low", "Medium", "High"]
)

print("\nDiscretized Data:")
print(book_records)