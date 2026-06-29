import pandas as pd

# Load dataset
df = pd.read_csv("data/student_dataset_v2.csv")

print("ORIGINAL DATA")
print(df.head())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Remove null values
df.dropna(inplace=True)

# Keep attendance between 0 and 100
df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]

# Keep study hours positive
df = df[df["StudyHours"] >= 0]

# Save cleaned dataset
df.to_csv("output/cleaned_data.csv", index=False)

print("\nDATA CLEANED SUCCESSFULLY")
print(df.head())