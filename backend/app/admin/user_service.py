from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.authentication.models import (
    User,
    UserRole,
)


def get_all_users(
    db: Session,
    page: int,
    limit: int,
    search: str | None,
    role: str |None,
):
    query = db.query(User)

    if search:
        query = query.filter(
            func.lower(User.email).contains(search.lower())
        )

    if role:
        query = query.filter(User.role == role)

    total = query.count()

    users = (
        query.order_by(User.created_at.desc())
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )

    return users, total


def get_user_by_id(
    db: Session,
    user_id: UUID,
) -> User:

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found.",
        )

    return user


def promote_user(
    db: Session,
    user_id: UUID,
) -> User:

    user = get_user_by_id(db, user_id)

    if user.role == UserRole.ADMIN:
        raise HTTPException(
            status_code=400,
            detail="User is already an admin.",
        )

    user.role = UserRole.ADMIN

    db.commit()
    db.refresh(user)

    return user


def demote_user(
    db: Session,
    user_id: UUID,
) -> User:

    user = get_user_by_id(db, user_id)

    if user.role == UserRole.USER:
        raise HTTPException(
            status_code=400,
            detail="User is already a normal user.",
        )

    user.role = UserRole.USER

    db.commit()
    db.refresh(user)

    return user