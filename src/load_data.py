import pandas as pd

# Load CSV file
df = pd.read_csv("data/student_dataset_v2.csv")

# Display first 5 rows
print("FIRST 5 RECORDS")
print(df.head())

# Display last 5 rows
print("\nLAST 5 RECORDS")
print(df.tail())

# Shape
print("\nDATASET SHAPE")
print(df.shape)

# Column names
print("\nCOLUMN NAMES")
print(df.columns)

# Data types
print("\nDATA TYPES")
print(df.dtypes)