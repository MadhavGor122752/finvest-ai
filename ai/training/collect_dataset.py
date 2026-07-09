from pathlib import Path
import pandas as pd
import httpx


RAW_DATA_DIR = Path("ai/dataset/raw")
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

MFAPI_URL = "https://api.mfapi.in/mf"


def download_scheme_list():

    print("Downloading mutual fund scheme list...")

    response = httpx.get(
        MFAPI_URL,
        timeout=60,
    )

    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data)

    output_file = RAW_DATA_DIR / "scheme_list.csv"

    df.to_csv(
        output_file,
        index=False,
    )

    print(f"Downloaded {len(df)} schemes.")
    print(f"Saved to {output_file}")


if __name__ == "__main__":
    download_scheme_list()