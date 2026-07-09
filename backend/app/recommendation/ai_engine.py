from pathlib import Path
import pandas as pd

# Load dataset only once
from pathlib import Path

DATASET_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "clean_mutual_funds.csv"
)

df = pd.read_csv(DATASET_PATH)

# Convert numeric columns
numeric_columns = [
    "rating",
    "expense_ratio",
    "fund_size_cr",
    "fund_age_yr",
    "sharpe",
    "returns_1yr",
    "returns_3yr",
    "returns_5yr",
    "min_sip",
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)


RISK_MAPPING = {
    "CONSERVATIVE": [1, 2],
    "MODERATE": [3, 4],
    "AGGRESSIVE": [5, 6],
}


def recommend_funds(
    risk_tolerance: str,
    investment_level: str,
    monthly_income: float,
):
    funds = df.copy()

    # Filter by risk
    funds = funds[
        funds["risk_level"].isin(
            RISK_MAPPING[risk_tolerance]
        )
    ]

    # Affordable SIP
    sip_budget = max(500, monthly_income * 0.20)

    funds = funds[
        funds["min_sip"] <= sip_budget
    ]

    # Personalized score
    funds["score"] = (
        funds["rating"] * 20
        + funds["sharpe"] * 15
        + funds["returns_5yr"] * 15
        - funds["expense_ratio"] * 5
        + funds["fund_age_yr"] * 2
    )

    funds = funds.sort_values(
        "score",
        ascending=False,
    )

    return funds.head(5)