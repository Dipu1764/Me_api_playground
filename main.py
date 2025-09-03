from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List, Optional
import os
import models
import schemas
import database
from database import get_db

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Me-API Playground - Deepak's Portfolio",
    description="A personal profile API playground showcasing Deepak's skills, projects, and experience",
    version="1.0.0"
)

# Configure CORS for production
allowed_origins = [
    "*",  # Allow all origins for now - update with your domain in production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files for frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "API is running"}

# Profile endpoints
@app.post("/profile", response_model=schemas.ProfileResponse)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    # Check if profile already exists
    existing_profile = db.query(models.Profile).first()
    if existing_profile:
        raise HTTPException(status_code=400, detail="Profile already exists. Use PUT to update.")
    
    db_profile = models.Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

@app.get("/profile", response_model=schemas.ProfileResponse)
def get_profile(db: Session = Depends(get_db)):
    profile = db.query(models.Profile).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@app.put("/profile", response_model=schemas.ProfileResponse)
def update_profile(profile_update: schemas.ProfileUpdate, db: Session = Depends(get_db)):
    profile = db.query(models.Profile).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    for field, value in profile_update.dict(exclude_unset=True).items():
        setattr(profile, field, value)
    
    db.commit()
    db.refresh(profile)
    return profile

# Education endpoints
@app.post("/education", response_model=schemas.EducationResponse)
def create_education(education: schemas.EducationCreate, db: Session = Depends(get_db)):
    db_education = models.Education(**education.dict())
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education

@app.get("/education", response_model=List[schemas.EducationResponse])
def get_education(db: Session = Depends(get_db)):
    return db.query(models.Education).all()

# Skills endpoints
@app.post("/skills", response_model=schemas.SkillResponse)
def create_skill(skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    db_skill = models.Skill(**skill.dict())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

@app.get("/skills", response_model=List[schemas.SkillResponse])
def get_skills(db: Session = Depends(get_db)):
    return db.query(models.Skill).all()

@app.get("/skills/top", response_model=List[schemas.SkillResponse])
def get_top_skills(limit: int = Query(5, ge=1, le=20), db: Session = Depends(get_db)):
    return db.query(models.Skill).order_by(models.Skill.proficiency_level.desc()).limit(limit).all()

# Projects endpoints
@app.post("/projects", response_model=schemas.ProjectResponse)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.get("/projects", response_model=List[schemas.ProjectResponse])
def get_projects(skill: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(models.Project)
    if skill:
        query = query.filter(models.Project.technologies.contains(skill))
    return query.all()

@app.get("/projects/{project_id}", response_model=schemas.ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# Work experience endpoints
@app.post("/work", response_model=schemas.WorkExperienceResponse)
def create_work_experience(work: schemas.WorkExperienceCreate, db: Session = Depends(get_db)):
    db_work = models.WorkExperience(**work.dict())
    db.add(db_work)
    db.commit()
    db.refresh(db_work)
    return db_work

@app.get("/work", response_model=List[schemas.WorkExperienceResponse])
def get_work_experience(db: Session = Depends(get_db)):
    return db.query(models.WorkExperience).all()

# Links endpoints
@app.post("/links", response_model=schemas.LinkResponse)
def create_link(link: schemas.LinkCreate, db: Session = Depends(get_db)):
    db_link = models.Link(**link.dict())
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

@app.get("/links", response_model=List[schemas.LinkResponse])
def get_links(db: Session = Depends(get_db)):
    return db.query(models.Link).all()

# Search endpoint
@app.get("/search")
def search(q: str = Query(..., min_length=2), db: Session = Depends(get_db)):
    results = {
        "projects": [],
        "skills": [],
        "work": []
    }
    
    # Search in projects
    projects = db.query(models.Project).filter(
        models.Project.title.contains(q) | 
        models.Project.description.contains(q) |
        models.Project.technologies.contains(q)
    ).all()
    results["projects"] = [{"id": p.id, "title": p.title, "description": p.description} for p in projects]
    
    # Search in skills
    skills = db.query(models.Skill).filter(models.Skill.name.contains(q)).all()
    results["skills"] = [{"id": s.id, "name": s.name, "proficiency_level": s.proficiency_level} for s in skills]
    
    # Search in work experience
    work = db.query(models.WorkExperience).filter(
        models.WorkExperience.company.contains(q) |
        models.WorkExperience.position.contains(q) |
        models.WorkExperience.description.contains(q)
    ).all()
    results["work"] = [{"id": w.id, "company": w.company, "position": w.position} for w in work]
    
    return results

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)