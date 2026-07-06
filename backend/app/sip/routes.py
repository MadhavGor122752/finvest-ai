from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.authentication.dependencies import get_current_user
from app.authentication.models import User
from app.core.database import get_db

from app.sip.models import SIP
from app.sip.schemas import (
    SIPCreateRequest,
    SIPResponse,
    SIPStatusUpdateRequest,
)
from app.sip.service import (
    create_sip,
    get_user_sips,
    update_sip_status,
)

router = APIRouter(
    prefix="/api/v1/sip",
    tags=["SIP"],
)


@router.post(
    "/",
    response_model=SIPResponse,
)
def create_sip_api(
    request: SIPCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    sip = create_sip(
        db=db,
        user=current_user,
        request=request,
    )

    return SIPResponse.model_validate(sip)


@router.get(
    "/",
    response_model=list[SIPResponse],
)
def get_sips_api(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    sips = get_user_sips(
        db=db,
        user=current_user,
    )

    return [
        SIPResponse.model_validate(sip)
        for sip in sips
    ]


@router.patch(
    "/{sip_id}",
    response_model=SIPResponse,
)
def update_sip_api(
    sip_id: str,
    request: SIPStatusUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    sip = (
        db.query(SIP)
        .filter(
            SIP.id == sip_id,
            SIP.user_id == current_user.id,
        )
        .first()
    )

    if not sip:
        raise HTTPException(
            status_code=404,
            detail="SIP not found",
        )

    sip = update_sip_status(
        db=db,
        sip=sip,
        status=request.status,
    )

    return SIPResponse.model_validate(sip)