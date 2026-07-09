from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.authentication.dependencies import require_admin
from app.authentication.models import User
from app.core.database import get_db

from app.admin.schemas import (
    AdminActionResponse,
    AdminDashboardResponse,
    AdminUserDetailResponse,
    AdminUserListResponse,
    AdminUserResponse,
)
from app.admin.service import get_dashboard_statistics
from app.admin.user_service import (
    demote_user,
    get_all_users,
    get_user_by_id,
    promote_user,
)

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
    return get_dashboard_statistics(db)


@router.get(
    "/users",
    response_model=AdminUserListResponse,
)
def list_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
    role: str | None = None,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    users, total = get_all_users(
        db=db,
        page=page,
        limit=limit,
        search=search,
        role=role,
    )

    return AdminUserListResponse(
        page=page,
        limit=limit,
        total=total,
        users=[
            AdminUserResponse(
                id=user.id,
                email=user.email,
                role=user.role.value,
                is_email_verified=user.is_email_verified,
            )
            for user in users
        ],
    )


@router.get(
    "/users/{user_id}",
    response_model=AdminUserDetailResponse,
)
def get_user(
    user_id: UUID,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    user = get_user_by_id(
        db=db,
        user_id=user_id,
    )

    return AdminUserDetailResponse(
        id=user.id,
        email=user.email,
        role=user.role.value,
        is_email_verified=user.is_email_verified,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )


@router.patch(
    "/users/{user_id}/promote",
    response_model=AdminActionResponse,
)
def promote_user_to_admin(
    user_id: UUID,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    user = promote_user(
        db=db,
        user_id=user_id,
    )

    return AdminActionResponse(
        message=f"{user.email} has been promoted to ADMIN."
    )


@router.patch(
    "/users/{user_id}/demote",
    response_model=AdminActionResponse,
)
def demote_admin_to_user(
    user_id: UUID,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    user = demote_user(
        db=db,
        user_id=user_id,
    )

    return AdminActionResponse(
        message=f"{user.email} has been demoted to USER."
    )