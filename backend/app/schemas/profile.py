from pydantic import BaseModel, EmailStr
from typing import Optional


class ProfileResponse(BaseModel):
    full_name: str
    professional_title: str
    short_bio: str
    location: str
    email: Optional[EmailStr] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None