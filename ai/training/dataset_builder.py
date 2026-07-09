from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import time
from unicodedata import name
from datetime import datetime
import pandas as pd

from ai.data_sources.mfapi.client import MFAPIClient
from ai.training.feature_engineering import (
    calculate_return,
    calculate_cagr,
    calculate_daily_returns,
    calculate_volatility,
    calculate_max_drawdown,
    calculate_sharpe_ratio,
    calculate_risk_level,
    get_nav_for_years,
)

INPUT_FILE = Path("ai/dataset/processed/filtered_schemes.csv")

client = MFAPIClient()


def build_dataset(
    limit=None,
    output_file="ai/dataset/processed/sample_dataset.csv",
):
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT_FILE)
    # Keep only unique Growth schemes
    df = df.drop_duplicates(subset=["schemeCode"])

        # Remove rows without scheme names
    df = df[df["schemeName"].notna()]

        # Remove blank names
    df = df[df["schemeName"].str.strip() != ""]

    print(f"Eligible schemes after filtering: {len(df)}")
    IMPORTANT_KEYWORDS = [
    "Equity",
    "Hybrid",
    "Debt",
    "ELSS",
    "Index",
    "Flexi",
    "Large",
    "Mid",
    "Small",
    "Multi",
]
    
    if limit is not None:
        df = df.head(limit)

    print("=" * 70)
    print("FINVEST AI DATASET BUILDER")
    print("=" * 70)
    print(f"\nProcessing {len(df)} schemes...\n")

    dataset = []

    if output_path.exists():
        dataset = pd.read_csv(output_path).to_dict("records")
        print(f"📂 Loaded {len(dataset)} existing records")
    
    processed = 0
    skipped = 0
    processed_codes = {
    row["scheme_code"]
    for row in dataset
    }

    for index, (_, row) in enumerate(df.iterrows(), start=1):

        print(f"\n[{index}/{len(df)}]")

        scheme_code = int(row["schemeCode"])
        if scheme_code in processed_codes:
            print(f"⏩ Already processed: {scheme_code}")
            continue

        try:

            history = None

            for attempt in range(2):
                try:
                    history = client.get_scheme_history(scheme_code)
                    break
                except Exception:
                    print(
                        f"Retry {attempt + 1}/3 for scheme {scheme_code}"
                    )
                    time.sleep(0.2)

            if history is None:
                raise Exception("Failed after 3 retries")

            meta = history["meta"]
            category = meta["scheme_category"]

            if not any(keyword in category for keyword in IMPORTANT_KEYWORDS):
                skipped += 1
                print(f"⚠️ Skipping {scheme_code}: {category}")
                continue
            nav_history = history["data"]

            valid_history = []

            for item in nav_history:

                try:

                    nav = float(item["nav"])

                    if nav > 0:
                        valid_history.append(item)

                except Exception:
                    continue

            if len(valid_history) < 300:
                skipped += 1
                processed_codes.add(meta["scheme_code"])
                print(
                    f"⚠ Skipping {scheme_code}: "
                    f"insufficient history ({len(valid_history)} records)"
                )

                continue

            nav_history = valid_history
            latest_date = datetime.strptime(
                nav_history[0]["date"],
                "%d-%m-%Y",
            )

            oldest_date = datetime.strptime(
                nav_history[-1]["date"],
                "%d-%m-%Y",
            )

            years = (latest_date - oldest_date).days / 365.25

            if years < 3:
                skipped += 1
                processed_codes.add(meta["scheme_code"])
                print(
                    f"⚠ Skipping {scheme_code}: only {years:.1f} years of history"
                )
                continue
            nav_values = [
                float(item["nav"])
                for item in nav_history
            ]

            latest_nav = nav_values[0]

            one_year_return = None
            three_year_cagr = None
            five_year_cagr = None
            ten_year_cagr = None

           # -----------------------------
            # Calculate Returns & CAGR
            # -----------------------------

            try:
                nav_1y = get_nav_for_years(nav_history, 1)
                one_year_return = calculate_return(
                    latest_nav,
                    nav_1y,
                )
            except Exception:
                pass

            try:
                nav_3y = get_nav_for_years(nav_history, 3)
                three_year_cagr = calculate_cagr(
                    nav_3y,
                    latest_nav,
                    3,
                )
            except Exception:
                pass

            try:
                nav_5y = get_nav_for_years(nav_history, 5)
                five_year_cagr = calculate_cagr(
                    nav_5y,
                    latest_nav,
                    5,
                )
            except Exception:
                pass

            try:
                nav_10y = get_nav_for_years(nav_history, 10)
                ten_year_cagr = calculate_cagr(
                    nav_10y,
                    latest_nav,
                    10,
                )
            except Exception:
                pass

            # -----------------------------
            # Financial Metrics
            # -----------------------------

            daily_returns = calculate_daily_returns(
                nav_values
            )

            volatility = calculate_volatility(
                daily_returns
            )

            sharpe_ratio = calculate_sharpe_ratio(
                daily_returns
            )

            max_drawdown = calculate_max_drawdown(
                nav_values
            )

            risk_level = calculate_risk_level(
                volatility
            )

            # -----------------------------
            # Dataset Row
            # -----------------------------

            dataset.append(
                {
                    "scheme_code": meta["scheme_code"],
                    "scheme_name": meta["scheme_name"],
                    "fund_house": meta["fund_house"],
                    "category": meta["scheme_category"],
                    "current_nav": round(latest_nav, 4),
                    "history_records": len(nav_values),
                    "one_year_return": (
                        round(one_year_return, 2)
                        if one_year_return is not None
                        else None
                    ),
                    "three_year_cagr": (
                        round(three_year_cagr, 2)
                        if three_year_cagr is not None
                        else None
                    ),
                    "five_year_cagr": (
                        round(five_year_cagr, 2)
                        if five_year_cagr is not None
                        else None
                    ),
                    "ten_year_cagr": (
                        round(ten_year_cagr, 2)
                        if ten_year_cagr is not None
                        else None
                    ),
                    "volatility": (
                        round(volatility, 2)
                        if volatility is not None
                        else None
                    ),
                    "max_drawdown": round(
                        max_drawdown,
                        2,
                    ),
                    "sharpe_ratio": (
                        round(sharpe_ratio, 2)
                        if sharpe_ratio is not None
                        else None
                    ),
                    "risk_level": risk_level,
                }
            )

            processed += 1
            processed_codes.add(meta["scheme_code"])
            print(f"✓ {meta['scheme_name']}")

            # -----------------------------
            # Auto Checkpoint
            # -----------------------------

            if len(dataset) % 10 == 0:

                pd.DataFrame(dataset).to_csv(
                    output_path,
                    index=False,
                )

                print(
                    f"💾 Checkpoint Saved "
                    f"({len(dataset)} funds)"
                )
                    
                

        except Exception as e:

            skipped += 1
            processed_codes.add(scheme_code)

            print(
                f"⚠️ Skipping {scheme_code}: {e}"
            )

        output = pd.DataFrame(dataset)

        output.to_csv(
        output_path,
        index=False,
    )

    print("\n" + "=" * 70)
    print("DATASET CREATED SUCCESSFULLY")
    print("=" * 70)

    print(f"\nTotal Funds Processed : {len(df)}")
    print(f"Dataset Size          : {len(output)}")
    print(f"Funds Skipped         : {skipped}")

    if len(output) > 0:
        print("\nPreview:\n")
        print(output.head())

    print(f"\nSaved to: {output_path}")
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Processed : {processed}")
    print(f"Skipped   : {skipped}")
    print(f"Saved     : {len(dataset)}")

    client.close()


if __name__ == "__main__":
    
    build_dataset(
        limit=None,
        output_file="ai/dataset/final/mutual_fund_dataset.csv",
    )
    # ----------------------------
    # PRODUCTION MODE
    # Uncomment when ready
    # -----------------------------
    # build_dataset(
    #     limit=None,
    #     output_file="ai/dataset/final/mutual_fund_dataset.csv",
    # )