from sqlalchemy.orm import Session

from app.mutual_fund.api_client import MutualFundAPIClient
from app.mutual_fund.models import MutualFund


client = MutualFundAPIClient()


def sync_mutual_funds(
    db: Session,
):

    funds = client.get_all_funds()

    created = 0
    updated = 0

    for fund in funds:

        scheme_code = int(fund["schemeCode"])

        existing = (
            db.query(MutualFund)
            .filter(
                MutualFund.scheme_code == scheme_code
            )
            .first()
        )

        if existing:
            updated += 1
            continue

        created += 1

    return {
        "total": len(funds),
        "created": created,
        "updated": updated,
    }