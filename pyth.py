import pandas as pd

# Load CSV file
df = pd.read_csv("data.csv")

# View first rows
print(df.head())

# Basic info
print(df.info())

# Summary statistics
print(df.describe())
