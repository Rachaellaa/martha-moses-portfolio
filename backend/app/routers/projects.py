from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.project import Project
from app.schemas.projects import ProjectResponse


router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"]
)


@router.get("/", response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):

    projects = (
        db.query(Project)
        .order_by(Project.id.asc())
        .all()
    )

    return projects