from sqlalchemy import Column, Integer, String, Boolean, JSON
from app.core.database import Base


class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    employment_type = Column(String(100), nullable=True)
    location = Column(String(150), nullable=True)
    start_date = Column(String(50), nullable=True)
    end_date = Column(String(50), nullable=True)
    is_current = Column(Boolean, default=False)
    responsibilities = Column(JSON, nullable=True)
    technologies = Column(JSON, nullable=True)