"""
Netflix Data Analysis

Author: Sikandar Khan

Description:
This project analyzes the Netflix Movies and TV Shows dataset using Python, Pandas, Matplotlib, and Seaborn.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/netflix_titles.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

print("\n" + "="*50)

# Number of rows and columns
print("Shape of Dataset:")
print(df.shape)

print("\n" + "="*50)

# Column names
print("Column Names:")
print(df.columns)

print("\n" + "="*50)

# Information about the dataset
print("Dataset Information:")
print(df.info())

print("\n" + "="*50)

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())

print("\n" + "="*50)

# Statistical summary (for numerical columns)
print("Statistical Summary:")
print(df.describe())

print("\n" + "=" * 50)
print("Number of Duplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)

print("\n" + "=" * 50)

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["date_added"] = df["date_added"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")

print("Missing Values After Cleaning:")
print(df.isnull().sum())

print("\n" + "=" * 50)
print("Movies vs TV Shows")
print(df["type"].value_counts())

print("\n" + "=" * 50)
print("Top 10 Countries")
print(df["country"].value_counts().head(10))

print("\n" + "=" * 50)
print("Top 10 Ratings")
print(df["rating"].value_counts().head(10))

print("\n" + "=" * 50)
print("Top 10 Release Years")
print(df["release_year"].value_counts().head(10))

print("\nCreating Movie vs TV Show Chart...")

plt.figure(figsize=(6,4))

sns.countplot(x="type", data=df)

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

plt.savefig("images/movie_vs_tvshow.png")

plt.show()

print("\nCreating Top 10 Countries Chart...")

top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10,6))

top_countries.plot(kind="bar")

plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("images/top_10_countries.png")

plt.show()

print("\nCreating Ratings Distribution Chart...")

plt.figure(figsize=(10,6))

sns.countplot(
    y="rating",
    data=df,
    order=df["rating"].value_counts().index
)

plt.title("Netflix Content Ratings")
plt.xlabel("Count")
plt.ylabel("Rating")

plt.tight_layout()

plt.savefig("images/ratings_distribution.png")

plt.show()

print("\nCreating Release Year Distribution Chart...")

plt.figure(figsize=(12,6))

sns.histplot(df["release_year"], bins=30)

plt.title("Distribution of Netflix Content by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("images/release_year_distribution.png")

plt.show()