from pathlib import Path
import pandas as pd

DATASET = Path("ai/dataset/raw/scheme_list.csv")

df = pd.read_csv(DATASET)

print("=" * 50)
print("Dataset Shape")
print("=" * 50)
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nFirst 10 Rows")
print(df.head(10))

print("\nMissing Values")
print(df.isnull().sum())