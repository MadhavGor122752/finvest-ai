import pandas as pd
from pathlib import Path

DATASET = Path("ai/dataset/comprehensive_mutual_funds_data.csv")

print("=" * 60)
print("FINVEST AI - DATA PREPROCESSING")
print("=" * 60)

df = pd.read_csv(DATASET)

print("\nDataset Loaded Successfully!\n")

print(df.shape)
print(df.head())

print("\nMissing Values\n")
# ----------------------------------------
# Fill Missing Values
# ----------------------------------------

df["returns_3yr"] = df["returns_3yr"].fillna(df["returns_3yr"].median())
df["returns_5yr"] = df["returns_5yr"].fillna(df["returns_5yr"].median())

print("\nMissing Values After Cleaning\n")
print(df.isnull().sum())
# ----------------------------------------
# Select Features
# ----------------------------------------

columns = [
    "scheme_name",
    "category",
    "sub_category",
    "risk_level",
    "rating",
    "expense_ratio",
    "fund_size_cr",
    "fund_age_yr",
    "sharpe",
    "alpha",
    "beta",
    "returns_1yr",
    "returns_3yr",
    "returns_5yr",
    "min_sip",
]

df = df[columns]

print("\nSelected Features\n")
print(df.head())
# ----------------------------------------
# Save Clean Dataset
# ----------------------------------------

OUTPUT = Path("ai/dataset/processed/clean_mutual_funds.csv")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT, index=False)

print("\nDataset Saved Successfully!")
print(f"Location: {OUTPUT}")
print(f"Shape: {df.shape}")