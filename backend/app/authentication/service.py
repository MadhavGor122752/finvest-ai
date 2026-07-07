from sqlalchemy.orm import Session

from app.authentication.models import (
    User,
    UserRole,
)
from app.authentication.schemas import RegisterRequest

from app.core.jwt import create_access_token

from app.core.security import (
    hash_password,
    verify_password,
)


def register_user(
    db: Session,
    request: RegisterRequest,
) -> User:

    existing_user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    if existing_user:
        raise ValueError("Email is already registered.")

    user = User(
        email=request.email,
        password_hash=hash_password(request.password),
        role=UserRole.USER,
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def login_user(
    db: Session,
    email: str,
    password: str,
) -> str:

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        raise ValueError("Invalid email or password.")

    if not verify_password(
        password,
        user.password_hash,
    ):
        raise ValueError("Invalid email or password.")

    return create_access_token(
        {
            "sub": str(user.id),
            "email": user.email,
        }
    )