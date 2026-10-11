#!pip install wordcloud



import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_venn as venn
from wordcloud import WordCloud


df = pd.read_csv("books.csv")

print("Books Data:")
print(df[[
    "title",
    "authors",
    "original_publication_year",
    "average_rating",
    "ratings_count"
]].head())

df = df.dropna(
    subset=["authors", "original_publication_year", "title"]
)




period1 = df[df["original_publication_year"] < 2000]

period2 = df[df["original_publication_year"] >= 2000]

authors1 = set(period1["authors"])
authors2 = set(period2["authors"])


plt.figure(figsize=(7, 6))

venn.venn2(
    [authors1, authors2],
    set_labels=("Before 2000", "2000 and After")
)

plt.title("Comparison of Authors by Publication Period")
plt.show()



titles = " ".join(df["title"].astype(str))

wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color="white"
).generate(titles)

plt.figure(figsize=(12, 6))

plt.imshow(wordcloud, interpolation="bilinear")

plt.axis("off")
plt.title("Word Cloud of Book Titles")

plt.show()

