import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("books_dataset.csv")

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)


# ==========================================
# 2. BASIC DATASET INFORMATION
# ==========================================

print("\n1. DATASET SHAPE")
print("-" * 40)

rows, columns = df.shape

print("Number of rows:", rows)
print("Number of columns:", columns)


# ==========================================
# 3. COLUMN INFORMATION
# ==========================================

print("\n2. DATASET COLUMNS")
print("-" * 40)

print(df.columns.tolist())


# ==========================================
# 4. DATA TYPES
# ==========================================

print("\n3. DATA TYPES")
print("-" * 40)

print(df.dtypes)


# ==========================================
# 5. FIRST FIVE RECORDS
# ==========================================

print("\n4. FIRST FIVE RECORDS")
print("-" * 40)

print(df.head())


# ==========================================
# 6. MISSING VALUES
# ==========================================

print("\n5. MISSING VALUES")
print("-" * 40)

missing_values = df.isnull().sum()

print(missing_values)


# ==========================================
# 7. DUPLICATE RECORDS
# ==========================================

print("\n6. DUPLICATE RECORDS")
print("-" * 40)

duplicates = df.duplicated().sum()

print("Number of duplicate rows:", duplicates)


# ==========================================
# 8. DESCRIPTIVE STATISTICS
# ==========================================

print("\n7. DESCRIPTIVE STATISTICS")
print("-" * 40)

print(df[["price_gbp", "rating"]].describe())


# ==========================================
# 9. PRICE ANALYSIS
# ==========================================

print("\n8. PRICE ANALYSIS")
print("-" * 40)

print("Average price:", round(df["price_gbp"].mean(), 2))

print("Median price:", round(df["price_gbp"].median(), 2))

print("Minimum price:", round(df["price_gbp"].min(), 2))

print("Maximum price:", round(df["price_gbp"].max(), 2))


# ==========================================
# 10. RATING ANALYSIS
# ==========================================

print("\n9. RATING ANALYSIS")
print("-" * 40)

print(
    df["rating"].value_counts().sort_index()
)


# ==========================================
# 11. MOST EXPENSIVE BOOKS
# ==========================================

print("\n10. TOP 10 MOST EXPENSIVE BOOKS")
print("-" * 40)

expensive_books = df.nlargest(
    10,
    "price_gbp"
)[
    ["title", "price_gbp", "rating"]
]

print(expensive_books.to_string(index=False))


# ==========================================
# 12. CHEAPEST BOOKS
# ==========================================

print("\n11. TOP 10 CHEAPEST BOOKS")
print("-" * 40)

cheap_books = df.nsmallest(
    10,
    "price_gbp"
)[
    ["title", "price_gbp", "rating"]
]

print(cheap_books.to_string(index=False))


# ==========================================
# 13. PRICE DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

sns.histplot(
    df["price_gbp"],
    bins=20,
    kde=True
)

plt.title("Distribution of Book Prices")

plt.xlabel("Price (GBP)")

plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    "price_distribution.png",
    dpi=300
)

plt.show()


# ==========================================
# 14. RATING DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="rating"
)

plt.title("Distribution of Book Ratings")

plt.xlabel("Rating")

plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    "rating_distribution.png",
    dpi=300
)

plt.show()


# ==========================================
# 15. PRICE BY RATING
# ==========================================

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="rating",
    y="price_gbp"
)

plt.title("Book Price Distribution by Rating")

plt.xlabel("Rating")

plt.ylabel("Price (GBP)")

plt.tight_layout()

plt.savefig(
    "price_by_rating.png",
    dpi=300
)

plt.show()


# ==========================================
# 16. PRICE VS RATING
# ==========================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="rating",
    y="price_gbp"
)

plt.title("Relationship Between Price and Rating")

plt.xlabel("Rating")

plt.ylabel("Price (GBP)")

plt.tight_layout()

plt.savefig(
    "price_vs_rating.png",
    dpi=300
)

plt.show()


# ==========================================
# 17. CORRELATION
# ==========================================

print("\n12. CORRELATION")
print("-" * 40)

correlation = df[
    ["price_gbp", "rating"]
].corr()

print(correlation)


# ==========================================
# 18. OUTLIER DETECTION
# ==========================================

print("\n13. OUTLIER DETECTION")
print("-" * 40)

Q1 = df["price_gbp"].quantile(0.25)

Q3 = df["price_gbp"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR

upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["price_gbp"] < lower_limit) |
    (df["price_gbp"] > upper_limit)
]

print("Lower price limit:", round(lower_limit, 2))

print("Upper price limit:", round(upper_limit, 2))

print("Number of price outliers:", len(outliers))


# ==========================================
# 19. AVAILABILITY ANALYSIS
# ==========================================

print("\n14. AVAILABILITY")
print("-" * 40)

print(
    df["availability"].value_counts()
)


# ==========================================
# 20. FINAL SUMMARY
# ==========================================

print("\n" + "=" * 60)

print("EDA COMPLETED")

print("=" * 60)

print("\nGenerated visualizations:")

print("1. price_distribution.png")

print("2. rating_distribution.png")

print("3. price_by_rating.png")

print("4. price_vs_rating.png")