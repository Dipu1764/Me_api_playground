from sqlalchemy.orm import sessionmaker
from database import engine
import models
from datetime import datetime
import os

# Create tables
models.Base.metadata.create_all(bind=engine)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# ============================
# PORTFOLIO CONFIGURATION
# ============================
# Edit this section to update your portfolio content

# Profile Information
PROFILE_CONFIG = {
    "name": "Deepak Kumhar",
    "email": "deepakkumhar129@gmail.com",
    "phone": "+91-9521218887",
    "location": "Mansarovar, Jaipur (RAJ.)",
    "bio": "Python Developer and Data Scientist skilled in building scalable applications and extracting insights from data. Experienced with Django, Flask, Pandas, NumPy, and machine learning.",
    "resume_link": "https://drive.google.com/file/d/1AV2qpI7uvlAkbvFNAl7bLX3-R8wBvuDp/view?usp=sharing"
}

# Education Records
EDUCATION_CONFIG = [
    {
        "institution": "Govind Guru Tribal University, Banswara",
        "degree": "Bachelor of Science",
        "field_of_study": "Mathematics",
        "start_date": "07/2018",
        "end_date": "06/2021",
        "grade": "69.90%",
        "description": "Focused on core Mathematics concepts including Algebra, Calculus, and Statistics"
    },
    {
        "institution": "AlmaBetter, Bengaluru (Remote)",
        "degree": "Professional Program",
        "field_of_study": "Data Science",
        "start_date": "2024",
        "end_date": "2025",
        "description": "Completed a 1-year intensive Data Science program covering Python, SQL, Machine Learning, Deep Learning, and Data Analytics with hands-on projects"
    }
]

# Skills (1-5 proficiency scale)
SKILLS_CONFIG = [
    {"name": "Python", "category": "Programming Languages", "proficiency_level": 5, "years_of_experience": 2.0},
    {"name": "SQL", "category": "Databases", "proficiency_level": 4, "years_of_experience": 1.5},
    {"name": "Pandas", "category": "Data Analysis", "proficiency_level": 5, "years_of_experience": 2.0},
    {"name": "NumPy", "category": "Data Analysis", "proficiency_level": 5, "years_of_experience": 2.0},
    {"name": "Matplotlib", "category": "Data Visualization", "proficiency_level": 4, "years_of_experience": 1.5},
    {"name": "Seaborn", "category": "Data Visualization", "proficiency_level": 4, "years_of_experience": 1.5},
    {"name": "Scikit-learn", "category": "Machine Learning", "proficiency_level": 4, "years_of_experience": 1.5},
    {"name": "TensorFlow", "category": "Deep Learning", "proficiency_level": 3, "years_of_experience": 1.0},
    {"name": "PyTorch", "category": "Deep Learning", "proficiency_level": 3, "years_of_experience": 1.0},
    {"name": "Django", "category": "Backend Frameworks", "proficiency_level": 4, "years_of_experience": 1.5},
    {"name": "Flask", "category": "Backend Frameworks", "proficiency_level": 4, "years_of_experience": 1.5},
    {"name": "FastAPI", "category": "Backend Frameworks", "proficiency_level": 4, "years_of_experience": 1.0},
    {"name": "MySQL", "category": "Databases", "proficiency_level": 4, "years_of_experience": 1.5},
    {"name": "MongoDB", "category": "Databases", "proficiency_level": 3, "years_of_experience": 1.0},
    {"name": "Git", "category": "Version Control", "proficiency_level": 5, "years_of_experience": 2.0},
    {"name": "Docker", "category": "DevOps", "proficiency_level": 3, "years_of_experience": 0.5},
    {"name": "AWS", "category": "Cloud Platforms", "proficiency_level": 2, "years_of_experience": 0.5},
    {"name": "Excel", "category": "Data Analysis Tools", "proficiency_level": 4, "years_of_experience": 2.0},
    {"name": "Power BI", "category": "Data Visualization", "proficiency_level": 3, "years_of_experience": 1.0},
    {"name": "Tableau", "category": "Data Visualization", "proficiency_level": 3, "years_of_experience": 1.0},
]

# Projects
PROJECTS_CONFIG = [
    {
        "title": "Me-API Playground (This Portfolio)",
        "description": "Built a full-stack personal portfolio API with FastAPI backend and vanilla JavaScript frontend. Features dynamic content management, search functionality, and RESTful API design. Deployed on Render with automated CI/CD.",
        "technologies": "Python,FastAPI,SQLAlchemy,SQLite,HTML,CSS,JavaScript,Render,Git",
        "github_link": "https://github.com/Dipu1764/Me_api_playground",
        "live_link": "https://me-api-playground-1-sutg.onrender.com/static/index.html",
        "start_date": "2024",
        "end_date": "2024",
        "status": "completed"
    },
    {
        "title": "Global Terrorism Analysis",
        "description": "Explored and visualized terrorism-related data to identify global patterns, high-risk regions, and attack trends. Applied data cleaning, EDA, and machine learning techniques to derive insights.",
        "technologies": "Python,Pandas,NumPy,Matplotlib,Seaborn,Scikit-learn",
        "github_link": "https://github.com/Dipu1764/Global-Terrorism-project",
        "start_date": "2024",
        "end_date": "2024",
        "status": "completed"
    },
    {
        "title": "Airbnb Listings Analysis",
        "description": "Performed data analysis on Airbnb dataset to study pricing trends, demand patterns, and customer preferences. Built visual dashboards to present insights effectively.",
        "technologies": "Python,Pandas,Seaborn,Matplotlib,Power BI",
        "github_link": "https://github.com/Dipu1764/airbnb-analysis-project",
        "start_date": "2024",
        "end_date": "2024",
        "status": "completed"
    },
    {
        "title": "Flipkart Customer Sentiment Analysis",
        "description": "Analyzed customer reviews from Flipkart to classify sentiments and understand customer satisfaction levels. Implemented NLP techniques like TF-IDF and classification models.",
        "technologies": "Python,NLTK,Scikit-learn,Pandas,Flask",
        "github_link": "https://github.com/Dipu1764/Classification---Flipkart-Customer-Service-Satisfaction",
        "start_date": "2024",
        "end_date": "2024",
        "status": "completed"
    },
    {
        "title": "YouTube Data Analysis & Dashboard",
        "description": "Cleaned, transformed, and analyzed YouTube dataset to study viewership, engagement, and trends. Built an interactive dashboard for storytelling and insights.",
        "technologies": "Python,Pandas,Matplotlib,Seaborn,SQL,Tableau",
        "github_link": "https://github.com/Dipu1764/Trending-YouTube-Video-Internship-Project",
        "start_date": "2024",
        "end_date": "2024",
        "status": "completed"
    }
]

# Work Experience
WORK_CONFIG = [
    {
        "company": "AlmaBetter",
        "position": "Data Science Trainee",
        "location": "Remote (Bengaluru)",
        "start_date": "2024",
        "end_date": "2025",
        "description": "Completed an intensive 1-year Data Science program with hands-on industry projects. Worked on data cleaning, exploratory data analysis, visualization, and applied machine learning algorithms for real-world datasets.",
        "technologies": "Python,Pandas,NumPy,Matplotlib,Seaborn,Scikit-learn,TensorFlow,SQL,Power BI"
    },
    {
        "company": "Elevate Labs (Internship Project)",
        "position": "Python Developer & Data Analyst Intern",
        "location": "Remote",
        "start_date": "2024",
        "end_date": "2024",
        "description": "Developed and deployed data-driven projects including YouTube Data Analysis, Flipkart Sentiment Analysis, and Airbnb Listings Analysis. Built dashboards and APIs using Python frameworks.",
        "technologies": "Python,Django,Flask,FastAPI,SQL,Tableau,Power BI"
    }
]

# Social Links
LINKS_CONFIG = [
    {"platform": "GitHub", "url": "https://github.com/Dipu1764", "display_name": "GitHub Profile"},
    {"platform": "LinkedIn", "url": "https://www.linkedin.com/in/deepakkumhar129", "display_name": "LinkedIn Profile"},
    {"platform": "Portfolio", "url": "https://me-api-playground-1-sutg.onrender.com/static/index.html", "display_name": "Live Portfolio"},
    {"platform": "Instagram", "url": "https://www.instagram.com/dipu1764k?igsh=MWttZ3hwb3R1ZHhydA==", "display_name": "@Dipu1764k"},
    {"platform": "API Docs", "url": "https://me-api-playground-1-sutg.onrender.com/docs", "display_name": "API Documentation"},
]

def seed_database():
    """
    Seeds the database with portfolio data from configuration above.
    Run this function whenever you update your portfolio content.
    """
    print("🔄 Starting database seeding...")
    
    # Clear existing data
    print("🗑️  Clearing existing data...")
    db.query(models.Link).delete()
    db.query(models.WorkExperience).delete()
    db.query(models.Project).delete()
    db.query(models.Skill).delete()
    db.query(models.Education).delete()
    db.query(models.Profile).delete()
    
    # Create profile
    print("👤 Creating profile...")
    profile = models.Profile(**PROFILE_CONFIG)
    db.add(profile)
    db.commit()
    
    # Create education records
    print(f"🎓 Adding {len(EDUCATION_CONFIG)} education records...")
    for edu_data in EDUCATION_CONFIG:
        education = models.Education(**edu_data)
        db.add(education)
    
    # Create skills
    print(f"💪 Adding {len(SKILLS_CONFIG)} skills...")
    for skill_data in SKILLS_CONFIG:
        skill_obj = models.Skill(**skill_data)
        db.add(skill_obj)
    
    # Create projects
    print(f"🚀 Adding {len(PROJECTS_CONFIG)} projects...")
    for project_data in PROJECTS_CONFIG:
        project_obj = models.Project(**project_data)
        db.add(project_obj)
    
    # Create work experience
    print(f"💼 Adding {len(WORK_CONFIG)} work experiences...")
    for work_data in WORK_CONFIG:
        work_obj = models.WorkExperience(**work_data)
        db.add(work_obj)
    
    # Create links
    print(f"🔗 Adding {len(LINKS_CONFIG)} social links...")
    for link_data in LINKS_CONFIG:
        link_obj = models.Link(**link_data)
        db.add(link_obj)
    
    # Commit all changes
    db.commit()
    
    # Summary
    print("\n✅ Database seeded successfully!")
    print(f"📊 Summary:")
    print(f"   • Profile: {PROFILE_CONFIG['name']}")
    print(f"   • Education: {len(EDUCATION_CONFIG)} records")
    print(f"   • Skills: {len(SKILLS_CONFIG)} skills")
    print(f"   • Projects: {len(PROJECTS_CONFIG)} projects")
    print(f"   • Work Experience: {len(WORK_CONFIG)} positions")
    print(f"   • Social Links: {len(LINKS_CONFIG)} links")
    print(f"\n🌐 Your portfolio is now updated!")
    if os.getenv('RENDER'):
        print(f"📍 Live at: https://me-api-playground-1-sutg.onrender.com/static/index.html")
    else:
        print(f"📍 Local: http://127.0.0.1:8001/static/index.html")

def add_new_project(title, description, technologies, github_link="", live_link="", demo_link="", status="completed"):
    """
    Helper function to add a new project to the portfolio.
    
    Usage:
    add_new_project(
        title="My New Project",
        description="Description of what the project does",
        technologies="Python,Django,PostgreSQL",
        github_link="https://github.com/username/repo",
        live_link="https://myproject.com",
        status="completed"
    )
    """
    new_project = {
        "title": title,
        "description": description,
        "technologies": technologies,
        "github_link": github_link,
        "live_link": live_link,
        "demo_link": demo_link,
        "start_date": "2024",
        "end_date": "2024",
        "status": status
    }
    
    project_obj = models.Project(**new_project)
    db.add(project_obj)
    db.commit()
    print(f"✅ Added new project: {title}")

def add_new_skill(name, category, proficiency_level, years_of_experience=0.5):
    """
    Helper function to add a new skill to the portfolio.
    
    Usage:
    add_new_skill("React", "Frontend Frameworks", 4, 1.5)
    """
    new_skill = {
        "name": name,
        "category": category,
        "proficiency_level": proficiency_level,
        "years_of_experience": years_of_experience
    }
    
    skill_obj = models.Skill(**new_skill)
    db.add(skill_obj)
    db.commit()
    print(f"✅ Added new skill: {name} (Level {proficiency_level}/5)")

def update_profile_bio(new_bio):
    """
    Helper function to update your profile bio.
    
    Usage:
    update_profile_bio("New and improved bio description")
    """
    profile = db.query(models.Profile).first()
    if profile:
        profile.bio = new_bio
        db.commit()
        print(f"✅ Updated profile bio")
    else:
        print("❌ No profile found. Run seed_database() first.")

def show_portfolio_stats():
    """
    Display current portfolio statistics.
    """
    profile_count = db.query(models.Profile).count()
    skills_count = db.query(models.Skill).count()
    projects_count = db.query(models.Project).count()
    work_count = db.query(models.WorkExperience).count()
    education_count = db.query(models.Education).count()
    links_count = db.query(models.Link).count()
    
    print("\n📊 Portfolio Statistics:")
    print(f"   • Profiles: {profile_count}")
    print(f"   • Skills: {skills_count}")
    print(f"   • Projects: {projects_count}")
    print(f"   • Work Experience: {work_count}")
    print(f"   • Education: {education_count}")
    print(f"   • Social Links: {links_count}")
    
    if skills_count > 0:
        top_skills = db.query(models.Skill).order_by(models.Skill.proficiency_level.desc()).limit(5).all()
        print(f"\n🎆 Top 5 Skills:")
        for skill in top_skills:
            print(f"   • {skill.name}: {skill.proficiency_level}/5 ({skill.years_of_experience} years)")

# ============================
# MAIN EXECUTION
# ============================

if __name__ == "__main__":
    import sys
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "stats":
            show_portfolio_stats()
        elif command == "seed":
            seed_database()
        elif command == "help":
            print("📝 Portfolio Management Commands:")
            print("   python seed_data.py         - Seed database with portfolio data")
            print("   python seed_data.py seed    - Same as above")
            print("   python seed_data.py stats   - Show current portfolio statistics")
            print("   python seed_data.py help    - Show this help message")
            print("\n📝 To update your portfolio:")
            print("   1. Edit the configuration sections at the top of this file")
            print("   2. Run: python seed_data.py")
            print("   3. Your changes will be live on your portfolio!")
        else:
            print(f"❌ Unknown command: {command}")
            print("Run 'python seed_data.py help' for available commands")
    else:
        # Default action: seed the database
        seed_database()
        show_portfolio_stats()