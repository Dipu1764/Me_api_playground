<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Profile(Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20))
    location = Column(String(100))
    bio = Column(Text)
    resume_link = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Education(Base):
    __tablename__ = "education"
    
    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String(200), nullable=False)
    degree = Column(String(100), nullable=False)
    field_of_study = Column(String(100))
    start_date = Column(String(20))  # Using string for flexibility (MM/YYYY format)
    end_date = Column(String(20))
    grade = Column(String(20))
    description = Column(Text)
    profile_id = Column(Integer, ForeignKey("profiles.id"), default=1)

class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50))  # e.g., "Programming Languages", "Frameworks", "Tools"
    proficiency_level = Column(Integer, default=1)  # 1-5 scale
    years_of_experience = Column(Float)
    profile_id = Column(Integer, ForeignKey("profiles.id"), default=1)

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    technologies = Column(String(500))  # Comma-separated list
    github_link = Column(String(255))
    live_link = Column(String(255))
    demo_link = Column(String(255))
    start_date = Column(String(20))
    end_date = Column(String(20))
    status = Column(String(20), default="completed")  # completed, ongoing, planned
    profile_id = Column(Integer, ForeignKey("profiles.id"), default=1)

class WorkExperience(Base):
    __tablename__ = "work_experience"
    
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(200), nullable=False)
    position = Column(String(100), nullable=False)
    location = Column(String(100))
    start_date = Column(String(20))
    end_date = Column(String(20))  # Can be "Present"
    description = Column(Text)
    technologies = Column(String(500))  # Comma-separated list
    profile_id = Column(Integer, ForeignKey("profiles.id"), default=1)

class Link(Base):
    __tablename__ = "links"
    
    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String(50), nullable=False)  # github, linkedin, portfolio, twitter, etc.
    url = Column(String(255), nullable=False)
    display_name = Column(String(100))
=======
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Profile(Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20))
    location = Column(String(100))
    bio = Column(Text)
    resume_link = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Education(Base):
    __tablename__ = "education"
    
    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String(200), nullable=False)
    degree = Column(String(100), nullable=False)
    field_of_study = Column(String(100))
    start_date = Column(String(20))  # Using string for flexibility (MM/YYYY format)
    end_date = Column(String(20))
    grade = Column(String(20))
    description = Column(Text)
    profile_id = Column(Integer, ForeignKey("profiles.id"), default=1)

class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50))  # e.g., "Programming Languages", "Frameworks", "Tools"
    proficiency_level = Column(Integer, default=1)  # 1-5 scale
    years_of_experience = Column(Float)
    profile_id = Column(Integer, ForeignKey("profiles.id"), default=1)

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    technologies = Column(String(500))  # Comma-separated list
    github_link = Column(String(255))
    live_link = Column(String(255))
    demo_link = Column(String(255))
    start_date = Column(String(20))
    end_date = Column(String(20))
    status = Column(String(20), default="completed")  # completed, ongoing, planned
    profile_id = Column(Integer, ForeignKey("profiles.id"), default=1)

class WorkExperience(Base):
    __tablename__ = "work_experience"
    
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(200), nullable=False)
    position = Column(String(100), nullable=False)
    location = Column(String(100))
    start_date = Column(String(20))
    end_date = Column(String(20))  # Can be "Present"
    description = Column(Text)
    technologies = Column(String(500))  # Comma-separated list
    profile_id = Column(Integer, ForeignKey("profiles.id"), default=1)

class Link(Base):
    __tablename__ = "links"
    
    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String(50), nullable=False)  # github, linkedin, portfolio, twitter, etc.
    url = Column(String(255), nullable=False)
    display_name = Column(String(100))
>>>>>>> ac3d1a1848664a93ad8763713f315124e9e6f55e
    profile_id = Column(Integer, ForeignKey("profiles.id"), default=1)