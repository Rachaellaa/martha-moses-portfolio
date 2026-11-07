from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class ExperienceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    job_title: str
    company: str
    employment_type: Optional[str] = None
    location: Optional[str] = None
    start_date: str
    end_date: Optional[str] = None
    is_current: bool = False
    responsibilities: List[str]
    technologies: List[str]