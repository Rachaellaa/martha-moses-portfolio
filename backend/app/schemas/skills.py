from typing import List
from pydantic import BaseModel


class SkillCategoryResponse(BaseModel):
    category: str
    skills: List[str]