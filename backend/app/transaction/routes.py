from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.authentication.dependencies import get_current_user
from app.authentication.models import User

from app.core.database import get_db

from app.transaction.schemas import (
    TransactionCreateRequest,
    TransactionResponse,
)

from app.transaction.service import create_transaction

router = APIRouter(
    prefix="/api/v1/transaction",
    tags=["Transaction"],
)


@router.post(
    "/",
    response_model=TransactionResponse,
)
def create_transaction_api(
    request: TransactionCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    transaction = create_transaction(
        db=db,
        user=current_user,
        request=request,
    )

    return TransactionResponse.model_validate(transaction)