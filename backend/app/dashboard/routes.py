from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.authentication.dependencies import get_current_user
from app.authentication.models import User
from app.core.database import get_db

from app.dashboard.schemas import DashboardResponse
from app.dashboard.service import get_dashboard


router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/",
    response_model=DashboardResponse,
)
def dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_dashboard(
        db=db,
        user=current_user,
    )