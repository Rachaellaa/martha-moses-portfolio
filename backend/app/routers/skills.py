from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.skill import Skill
from app.schemas.skills import SkillCategoryResponse


router = APIRouter(
    prefix="/api/skills",
    tags=["Skills"]
)


@router.get("/", response_model=list[SkillCategoryResponse])
def get_skills(db: Session = Depends(get_db)):

    skills = (
        db.query(Skill)
        .order_by(Skill.id.asc())
        .all()
    )

    return skills