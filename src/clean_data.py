import pandas as pd

df = pd.read_csv("data/student_dataset_v2.csv")

print("ORIGINAL DATA")
print(df.head())

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]

df = df[df["StudyHours"] >= 0]
df.to_csv("output/cleaned_data.csv", index=False)

print("\nDATA CLEANED SUCCESSFULLY")
print(df.head())
