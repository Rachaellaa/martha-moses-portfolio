from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    category: str
    industry: Optional[str] = None
    description: str
    problem_statement: str
    solution: str
    technologies: List[str]
    key_features: List[str]
    github_url: Optional[str] = None
    live_url: Optional[str] = None
    featured: bool = False