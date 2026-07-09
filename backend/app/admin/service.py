from sqlalchemy.orm import Session

from app.authentication.models import User
from app.profile.models import UserProfile
from app.sip.models import SIP
from app.transaction.models import Transaction

from app.admin.schemas import AdminDashboardResponse


def get_dashboard_statistics(
    db: Session,
) -> AdminDashboardResponse:

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