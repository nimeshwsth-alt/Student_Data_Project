import pandas as pd

df = pd.read_csv("output/cleaned_data.csv")

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

df.to_csv("output/transformed_data.csv", index=False)

print("Transformation completed!")
print(df.head())
