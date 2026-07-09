from pathlib import Path

from ai.training.dataset_builder import build_dataset


OUTPUT_DIR = Path("ai/dataset/final")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate():

    print("=" * 70)
    print("FINVEST AI - FINAL DATASET GENERATOR")
    print("=" * 70)

    print("\nGenerating dataset for all eligible mutual funds...\n")

    build_dataset(limit=None)

    print("\n")
    print("=" * 70)
    print("FINAL DATASET GENERATED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    generate()