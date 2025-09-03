from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# Profile schemas
class ProfileBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    location: Optional[str] = None
    bio: Optional[str] = None
    resume_link: Optional[str] = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    bio: Optional[str] = None
    resume_link: Optional[str] = None

class ProfileResponse(ProfileBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Education schemas
class EducationBase(BaseModel):
    institution: str
    degree: str
    field_of_study: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    grade: Optional[str] = None
    description: Optional[str] = None

class EducationCreate(EducationBase):
    pass

class EducationResponse(EducationBase):
    id: int
    profile_id: int

    class Config:
        orm_mode = True

# Skill schemas
class SkillBase(BaseModel):
    name: str
    category: Optional[str] = None
    proficiency_level: int = 1
    years_of_experience: Optional[float] = None

class SkillCreate(SkillBase):
    pass

class SkillResponse(SkillBase):
    id: int
    profile_id: int

    class Config:
        orm_mode = True

# Project schemas
class ProjectBase(BaseModel):
    title: str
    description: str
    technologies: Optional[str] = None
    github_link: Optional[str] = None
    live_link: Optional[str] = None
    demo_link: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    status: str = "completed"

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int
    profile_id: int

    class Config:
        orm_mode = True

# Work Experience schemas
class WorkExperienceBase(BaseModel):
    company: str
    position: str
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None
    technologies: Optional[str] = None

class WorkExperienceCreate(WorkExperienceBase):
    pass

class WorkExperienceResponse(WorkExperienceBase):
    id: int
    profile_id: int

    class Config:
        orm_mode = True

# Link schemas
class LinkBase(BaseModel):
    platform: str
    url: str
    display_name: Optional[str] = None

class LinkCreate(LinkBase):
    pass

class LinkResponse(LinkBase):
    id: int
    profile_id: int

    class Config:
        orm_mode = True