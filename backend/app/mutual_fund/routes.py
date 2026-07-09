from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.authentication.dependencies import require_admin

from app.authentication.models import User
from app.mutual_fund.service import (
    create_mutual_fund,
    delete_mutual_fund,
    get_all_mutual_funds,
    get_mutual_fund_by_scheme_code,
    search_mutual_funds,
    update_mutual_fund,
)
from app.mutual_fund.schemas import (
    MutualFundCreateRequest,
    MutualFundResponse,
    MutualFundUpdateRequest,
)

router = APIRouter(
    prefix="/api/v1/mutual-funds",
    tags=["Mutual Fund"],
)


@router.post(
    "",
    response_model=MutualFundResponse,
)
def create(
    request: MutualFundCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):

    return create_mutual_fund(db, request)


@router.get(
    "",
    response_model=list[MutualFundResponse],
)
def list_all(
    db: Session = Depends(get_db),
):

    return get_all_mutual_funds(db)


@router.get(
    "/search",
    response_model=list[MutualFundResponse],
)
def search(
    query: str,
    db: Session = Depends(get_db),
):

    return search_mutual_funds(db, query)


@router.get(
    "/{scheme_code}",
    response_model=MutualFundResponse,
)
def get_one(
    scheme_code: int,
    db: Session = Depends(get_db),
):

    fund = get_mutual_fund_by_scheme_code(
        db,
        scheme_code,
    )

    if fund is None:
        raise HTTPException(
            status_code=404,
            detail="Mutual fund not found.",
        )

    return fund


@router.put(
    "/{scheme_code}",
    response_model=MutualFundResponse,
)
def update(
    scheme_code: int,
    request: MutualFundUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):

    fund = get_mutual_fund_by_scheme_code(
        db,
        scheme_code,
    )

    if fund is None:
        raise HTTPException(
            status_code=404,
            detail="Mutual fund not found.",
        )

    return update_mutual_fund(
        db,
        fund,
        request,
    )


@router.delete(
    "/{scheme_code}",
)
def delete(
    scheme_code: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):

    fund = get_mutual_fund_by_scheme_code(
        db,
        scheme_code,
    )

    if fund is None:
        raise HTTPException(
            status_code=404,
            detail="Mutual fund not found.",
        )

    delete_mutual_fund(
        db,
        fund,
    )

    return {
        "message": "Mutual fund deleted successfully."
    }