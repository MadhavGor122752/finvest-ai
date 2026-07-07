from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.authentication.dependencies import get_current_user
from app.authentication.models import User
from app.core.database import get_db
from app.recommendation.schemas import RecommendationResponse
from app.recommendation.service import get_recommendations

router = APIRouter(
    prefix="/api/v1/recommendations",
    tags=["Recommendations"],
)


@router.get(
    "/",
    response_model=list[RecommendationResponse],
)
def recommendations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_recommendations(
        db=db,
        user=current_user,
    )