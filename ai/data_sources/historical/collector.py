from pprint import pprint

from ai.data_sources.mfapi.client import MFAPIClient

client = MFAPIClient()


def inspect_scheme_history():

    scheme_code = 100033

    data = client.get_scheme_history(scheme_code)

    print("=" * 80)
    print("Scheme Information")
    print("=" * 80)

    pprint(data["meta"])

    print("\n")
    print("=" * 80)
    print("Latest 5 NAV Records")
    print("=" * 80)

    for row in data["data"][:5]:
        pprint(row)


if __name__ == "__main__":
    inspect_scheme_history()