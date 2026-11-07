from sqlalchemy import Column, Integer, String, Text, Boolean, JSON
from app.core.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    category = Column(String(150), nullable=False)
    industry = Column(String(150), nullable=True)
    description = Column(Text, nullable=False)
    problem_statement = Column(Text, nullable=False)
    solution = Column(Text, nullable=False)
    technologies = Column(JSON, nullable=False)
    key_features = Column(JSON, nullable=False)
    github_url = Column(String(500), nullable=True)
    live_url = Column(String(500), nullable=True)
    featured = Column(Boolean, default=False)