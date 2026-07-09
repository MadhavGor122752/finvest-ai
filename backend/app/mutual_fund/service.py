from sqlalchemy.orm import Session

from app.mutual_fund.models import MutualFund
from app.mutual_fund.schemas import (
    MutualFundCreateRequest,
    MutualFundUpdateRequest,
)


def create_mutual_fund(
    db: Session,
    request: MutualFundCreateRequest,
) -> MutualFund:

    fund = MutualFund(
        scheme_code=request.scheme_code,
        scheme_name=request.scheme_name,
        fund_house=request.fund_house,
        category=request.category,
        risk_level=request.risk_level,
        nav=request.nav,
        expense_ratio=request.expense_ratio,
        aum=request.aum,
    )

    db.add(fund)
    db.commit()
    db.refresh(fund)

    return fund


def get_all_mutual_funds(
    db: Session,
):

    return (
        db.query(MutualFund)
        .order_by(MutualFund.scheme_name)
        .all()
    )


def get_mutual_fund_by_scheme_code(
    db: Session,
    scheme_code: int,
):

    return (
        db.query(MutualFund)
        .filter(MutualFund.scheme_code == scheme_code)
        .first()
    )


def update_mutual_fund(
    db: Session,
    fund: MutualFund,
    request: MutualFundUpdateRequest,
):

    fund.scheme_name = request.scheme_name
    fund.fund_house = request.fund_house
    fund.category = request.category
    fund.risk_level = request.risk_level
    fund.nav = request.nav
    fund.expense_ratio = request.expense_ratio
    fund.aum = request.aum
    fund.is_active = request.is_active

    db.commit()
    db.refresh(fund)

    return fund


def delete_mutual_fund(
    db: Session,
    fund: MutualFund,
):

    db.delete(fund)
    db.commit()


def search_mutual_funds(
    db: Session,
    query: str,
):

    return (
        db.query(MutualFund)
        .filter(
            MutualFund.scheme_name.ilike(f"%{query}%")
        )
        .all()
    )