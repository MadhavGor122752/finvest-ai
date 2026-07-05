from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from app.authentication.dependencies import get_current_user
from app.authentication.models import User
from sqlalchemy.orm import Session

from app.authentication.schemas import (
    LoginRequest,
    RegisterRequest,
    RegisterResponse,
    TokenResponse,
)

from app.authentication.service import (
    login_user,
    register_user,
)
from app.core.database import get_db

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=RegisterResponse,
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):

    try:
        user = register_user(db, request)

        return RegisterResponse(
            message="Registration successful.",
            email=user.email,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
    

@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):

    try:
        token = login_user(db, request)

        return TokenResponse(
            access_token=token,
            token_type="bearer",
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )

@router.get(
    "/me",
)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return {
        "id": str(current_user.id),
        "email": current_user.email,
        "is_email_verified": current_user.is_email_verified,
        "created_at": current_user.created_at,
        "updated_at": current_user.updated_at,
    }