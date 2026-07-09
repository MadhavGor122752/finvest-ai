import pandas as pd

df = pd.read_csv(
    "ai/dataset/processed/clean_mutual_funds.csv"
)
df["sharpe"] = pd.to_numeric(df["sharpe"], errors="coerce")
df["alpha"] = pd.to_numeric(df["alpha"], errors="coerce")
df["beta"] = pd.to_numeric(df["beta"], errors="coerce")

df["sharpe"] = df["sharpe"].fillna(0)
df["alpha"] = df["alpha"].fillna(0)
df["beta"] = df["beta"].fillna(0)

print(df.dtypes)
print("\nUnique Risk Levels:")
print(df["risk_level"].unique())

def recommend_funds(
    risk_level,
    sip_amount,
    investment_years,
):

    funds = df.copy()

    risk_mapping = {
        "Low": [1, 2],
        "Moderate": [3, 4],
        "High": [5, 6],
    }

    funds = funds[
        funds["risk_level"].isin(
            risk_mapping[risk_level]
        )
    ]

    funds = funds[
        funds["min_sip"] <= sip_amount
    ]

    if investment_years >= 5:

        funds["score"] = (
            funds["returns_5yr"] * 0.6
            +
            funds["rating"] * 10
            +
            funds["sharpe"] * 5
        )

    elif investment_years >= 3:

        funds["score"] = (
            funds["returns_3yr"] * 0.6
            +
            funds["rating"] * 10
            +
            funds["sharpe"] * 5
        )

    else:

        funds["score"] = (
            funds["returns_1yr"] * 0.6
            +
            funds["rating"] * 10
            +
            funds["sharpe"] * 5
        )

    return funds.sort_values(
        "score",
        ascending=False,
    ).head(5)


results = recommend_funds(
    risk_level="High",
    sip_amount=500,
    investment_years=5,
)

print(results[
    [
        "scheme_name",
        "rating",
        "risk_level",
        "returns_5yr",
        "score",
    ]
])