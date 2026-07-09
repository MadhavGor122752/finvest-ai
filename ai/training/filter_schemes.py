from pathlib import Path

import pandas as pd

RAW_DATA = Path("ai/dataset/raw/scheme_list.csv")
OUTPUT = Path("ai/dataset/processed/filtered_schemes.csv")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(RAW_DATA)

print(f"Original schemes: {len(df)}")

# Keep Growth plans only
growth = df[
    df["schemeName"].str.contains(
        "Growth",
        case=False,
        na=False,
    )
]

print(f"Growth schemes: {len(growth)}")

# Remove duplicate scheme names
growth = growth.drop_duplicates(
    subset="schemeName"
)

print(f"Unique Growth schemes: {len(growth)}")

growth.to_csv(
    OUTPUT,
    index=False,
)

print(f"\nSaved to {OUTPUT}")