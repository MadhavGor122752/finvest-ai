from sqlalchemy.orm import Session

from app.authentication.models import User
from app.profile.models import UserProfile
from app.profile.schemas import ProfileCreateRequest


def create_profile(
    db: Session,
    user: User,
    request: ProfileCreateRequest,
) -> UserProfile:

    existing_profile = (
        db.query(UserProfile)
        .filter(UserProfile.user_id == user.id)
        .first()
    )

    if existing_profile:
        raise ValueError("Profile already exists.")

    profile = UserProfile(
        user_id=user.id,
        first_name=request.first_name,
        last_name=request.last_name,
        phone_number=request.phone_number,
        date_of_birth=request.date_of_birth,
        occupation=request.occupation,
        monthly_income=request.monthly_income,
        investment_level=request.investment_level,
        risk_tolerance=request.risk_tolerance,
        profile_completed=True,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def get_profile(
    db: Session,
    user: User,
) -> UserProfile:

    profile = (
        db.query(UserProfile)
        .filter(UserProfile.user_id == user.id)
        .first()
    )

    if profile is None:
        raise ValueError("Profile not found.")

    return profile