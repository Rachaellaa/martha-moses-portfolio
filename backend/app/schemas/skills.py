from typing import List
from pydantic import BaseModel, ConfigDict


class SkillCategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    category: str
    skills: List[str]