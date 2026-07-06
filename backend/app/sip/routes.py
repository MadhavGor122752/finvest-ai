from fastapi import APIRouter

from app.sip.schemas import (
    SIPRequest,
    SIPResponse,
)
from app.sip.service import calculate_sip

router = APIRouter(
    prefix="/api/v1/sip",
    tags=["SIP Calculator"],
)


@router.post(
    "/calculate",
    response_model=SIPResponse,
)
def calculate(
    request: SIPRequest,
):

    return calculate_sip(request)