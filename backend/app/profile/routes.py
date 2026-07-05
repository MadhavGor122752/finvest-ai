from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.authentication.dependencies import get_current_user
from app.authentication.models import User
from app.core.database import get_db

from app.profile.schemas import (
    ProfileCreateRequest,
    ProfileResponse,
)
from app.profile.service import (
    create_profile,
    get_profile,
)


router = APIRouter(
    prefix="/api/v1/profile",
    tags=["Profile"],
)


@router.post(
    "/",
    response_model=ProfileResponse,
)
@router.get(
    "/",
    response_model=ProfileResponse,
)
def read_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:
        profile = get_profile(
            db=db,
            user=current_user,
        )

        return ProfileResponse.model_validate(profile)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
def create_user_profile(
    request: ProfileCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:
        profile = create_profile(
            db=db,
            user=current_user,
            request=request,
        )

        return ProfileResponse.model_validate(profile)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )