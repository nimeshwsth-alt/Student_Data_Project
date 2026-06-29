import pandas as pd

# Load cleaned data
df = pd.read_csv("output/cleaned_data.csv")

# Create grade column
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"

df["Grade"] = df["Marks"].apply(get_grade)

# Save transformed data
df.to_csv("output/transformed_data.csv", index=False)

print("Transformation completed!")
print(df.head())