from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.profile import Profile
from app.schemas.profile import ProfileResponse


router = APIRouter(
    prefix="/api/profile",
    tags=["Profile"]
)


@router.get("/", response_model=ProfileResponse)
def get_profile(db: Session = Depends(get_db)):

    profile = db.query(Profile).first()

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    return profile