from sqlalchemy.orm import Session

from app.authentication.models import User
from app.transaction.models import Transaction
from app.transaction.schemas import TransactionCreateRequest


def create_transaction(
    db: Session,
    user: User,
    request: TransactionCreateRequest,
) -> Transaction:

    transaction = Transaction(
        user_id=user.id,
        scheme_code=request.scheme_code,
        scheme_name=request.scheme_name,
        transaction_type=request.transaction_type,
        amount=request.amount,
        nav=request.nav,
        units=request.units,
    )

    db.add(transaction)

    db.commit()

    db.refresh(transaction)

    return transaction