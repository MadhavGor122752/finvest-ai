from datetime import date

from sqlalchemy.orm import Session

from app.authentication.models import User
from app.sip.models import SIP
from app.sip.schemas import SIPCreateRequest


def create_sip(
    db: Session,
    user: User,
    request: SIPCreateRequest,
) -> SIP:

    today = date.today()

    next_investment_date = date(
        today.year,
        today.month,
        request.sip_date,
    )

    if next_investment_date < today:

        if today.month == 12:
            next_investment_date = date(
                today.year + 1,
                1,
                request.sip_date,
            )
        else:
            next_investment_date = date(
                today.year,
                today.month + 1,
                request.sip_date,
            )

    sip = SIP(
        user_id=user.id,
        scheme_code=request.scheme_code,
        scheme_name=request.scheme_name,
        monthly_amount=request.monthly_amount,
        sip_date=request.sip_date,
        next_investment_date=next_investment_date,
        status="ACTIVE",
    )

    db.add(sip)
    db.commit()
    db.refresh(sip)

    return sip


def get_user_sips(
    db: Session,
    user: User,
) -> list[SIP]:

    return (
        db.query(SIP)
        .filter(SIP.user_id == user.id)
        .all()
    )


def update_sip_status(
    db: Session,
    sip: SIP,
    status: str,
) -> SIP:

    sip.status = status

    db.commit()

    db.refresh(sip)

    return sip