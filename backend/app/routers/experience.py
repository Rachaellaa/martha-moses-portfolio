from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.experience import Experience
from app.schemas.experience import ExperienceResponse


router = APIRouter(
    prefix="/api/experience",
    tags=["Experience"],
)


@router.get("/", response_model=list[ExperienceResponse])
def get_experience(db: Session = Depends(get_db)):

    experiences = (
        db.query(Experience)
        .order_by(Experience.id.asc())
        .all()
    )

    return experiences