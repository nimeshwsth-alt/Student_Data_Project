import pandas as pd

df = pd.read_csv("output/transformed_data.csv")

print("\nSTUDENT PERFORMANCE DASHBOARD")

print("Total Students:", len(df))
print("Average Marks:", round(df["Marks"].mean(), 2))
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

print("\nGRADE DISTRIBUTION")
print(df["Grade"].value_counts())
