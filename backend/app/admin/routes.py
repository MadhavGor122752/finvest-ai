from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.authentication.dependencies import require_admin
from app.authentication.models import User
from app.core.database import get_db

from app.admin.schemas import AdminDashboardResponse

from app.profile.models import UserProfile
from app.sip.models import SIP
from app.transaction.models import Transaction


router = APIRouter(
    prefix="/api/v1/admin",
    tags=["Admin"],
)


@router.get(
    "/dashboard",
    response_model=AdminDashboardResponse,
)
def admin_dashboard(
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):

    total_users = db.query(User).count()

    total_profiles = db.query(UserProfile).count()

    total_sips = db.query(SIP).count()

    total_transactions = db.query(Transaction).count()

    return AdminDashboardResponse(
        total_users=total_users,
        total_profiles=total_profiles,
        total_sips=total_sips,
        total_transactions=total_transactions,
    )
