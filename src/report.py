import pandas as pd

# Load transformed data
df = pd.read_csv("output/transformed_data.csv")

# Generate report
report = {
    "Total Students": len(df),
    "Average Marks": round(df["Marks"].mean(), 2),
    "Highest Marks": df["Marks"].max(),
    "Lowest Marks": df["Marks"].min()
}

print("\nFINAL REPORT")
for key, value in report.items():
    print(f"{key}: {value}")