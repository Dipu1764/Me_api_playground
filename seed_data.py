from sqlalchemy.orm import sessionmaker
from database import engine
import models

# Create tables
models.Base.metadata.create_all(bind=engine)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

def seed_database():
    # Clear existing data
    db.query(models.Link).delete()
    db.query(models.WorkExperience).delete()
    db.query(models.Project).delete()
    db.query(models.Skill).delete()
    db.query(models.Education).delete()
    db.query(models.Profile).delete()
    
    # Create profile
    profile = models.Profile(
        name="Deepak Kumhar",
        email="deepakkumhar129@gmail.com",
        phone="+91-9521218887",
        location="Mansarovar, Jaipur (RAJ.)",
        bio="Python Developer and Data Scientist skilled in building scalable applications and extracting insights from data. Experienced with Django, Flask, Pandas, NumPy, and machine learning.",
        resume_link="https://drive.google.com/file/d/1AV2qpI7uvlAkbvFNAl7bLX3-R8wBvuDp/view?usp=sharing"
    )
    db.add(profile)
    db.commit()
    
    # Create education records
    education_data = [
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
    
    for edu in education_data:
        education = models.Education(**edu)
        db.add(education)
    
    # Create skills
    skills_data = [
    {"name": "Python", "category": "Programming Languages", "proficiency_level": 4, "years_of_experience": 1.0},
    {"name": "SQL", "category": "Databases", "proficiency_level": 3, "years_of_experience": 0.5},
    {"name": "Pandas", "category": "Data Analysis", "proficiency_level": 4, "years_of_experience": 1.0},
    {"name": "NumPy", "category": "Data Analysis", "proficiency_level": 4, "years_of_experience": 1.0},
    {"name": "Matplotlib", "category": "Data Visualization", "proficiency_level": 3, "years_of_experience": 0.5},
    {"name": "Seaborn", "category": "Data Visualization", "proficiency_level": 3, "years_of_experience": 0.5},
    {"name": "Scikit-learn", "category": "Machine Learning", "proficiency_level": 3, "years_of_experience": 0.5},
    {"name": "TensorFlow", "category": "Deep Learning", "proficiency_level": 2, "years_of_experience": 0.5},
    {"name": "PyTorch", "category": "Deep Learning", "proficiency_level": 2, "years_of_experience": 0.5},
    {"name": "Django", "category": "Backend Frameworks", "proficiency_level": 3, "years_of_experience": 0.5},
    {"name": "Flask", "category": "Backend Frameworks", "proficiency_level": 3, "years_of_experience": 0.5},
    {"name": "FastAPI", "category": "Backend Frameworks", "proficiency_level": 2, "years_of_experience": 0.5},
    {"name": "MySQL", "category": "Databases", "proficiency_level": 3, "years_of_experience": 0.5},
    {"name": "MongoDB", "category": "Databases", "proficiency_level": 2, "years_of_experience": 0.5},
    {"name": "Git", "category": "Version Control", "proficiency_level": 4, "years_of_experience": 1.0},
    {"name": "Excel", "category": "Data Analysis Tools", "proficiency_level": 3, "years_of_experience": 1.0},
    {"name": "Power BI", "category": "Data Visualization", "proficiency_level": 2, "years_of_experience": 0.5}
]

    
    for skill in skills_data:
        skill_obj = models.Skill(**skill)
        db.add(skill_obj)
    
   # Create projects
    projects_data = [
    {
        "title": "Global Terrorism Analysis",
        "description": "Explored and visualized terrorism-related data to identify global patterns, high-risk regions, and attack trends. Applied data cleaning, EDA, and machine learning techniques to derive insights.",
        "technologies": "Python,Pandas,NumPy,Matplotlib,Seaborn,Scikit-learn",
        "github_link": "https://github.com/Dipu1764/Global-Terrorism-project",
        "status": "completed"
    },
    {
        "title": "Airbnb Listings Analysis",
        "description": "Performed data analysis on Airbnb dataset to study pricing trends, demand patterns, and customer preferences. Built visual dashboards to present insights effectively.",
        "technologies": "Python,Pandas,Seaborn,Matplotlib,Power BI",
        "github_link": "https://github.com/Dipu1764/airbnb-analysis-project",
        "status": "completed"
    },
    {
        "title": "Flipkart Customer Sentiment Analysis",
        "description": "Analyzed customer reviews from Flipkart to classify sentiments and understand customer satisfaction levels. Implemented NLP techniques like TF-IDF and classification models.",
        "technologies": "Python,NLTK,Scikit-learn,Pandas,Flask",
        "github_link": "https://github.com/Dipu1764/Classification---Flipkart-Customer-Service-Satisfaction",
        "status": "completed"
    },
    {
        "title": "YouTube Data Analysis & Dashboard",
        "description": "Cleaned, transformed, and analyzed YouTube dataset to study viewership, engagement, and trends. Built an interactive dashboard for storytelling and insights.",
        "technologies": "Python,Pandas,Matplotlib,Seaborn,SQL,Tableau",
        "github_link": "https://github.com/Dipu1764/Trending-YouTube-Video-Internship-Project",
        "status": "completed"
    }
]

    
    for project in projects_data:
        project_obj = models.Project(**project)
        db.add(project_obj)
    
    # Create work experience
    work_data = [
        {
        "company": "AlmaBetter",
        "position": "Data Science Trainee",
        "location": "Remote (Bengaluru)",
        "description": "Completed an intensive 1-year Data Science program with hands-on industry projects. Worked on data cleaning, exploratory data analysis, visualization, and applied machine learning algorithms for real-world datasets.",
        "technologies": "Python,Pandas,NumPy,Matplotlib,Seaborn,Scikit-learn,TensorFlow,SQL,Power BI"
    },
    {
        "company": "Elevate Labs (Internship Project)",
        "position": "Python Developer & Data Analyst Intern",
        "location": "Remote",
        "description": "Developed and deployed data-driven projects including YouTube Data Analysis, Flipkart Sentiment Analysis, and Airbnb Listings Analysis. Built dashboards and APIs using Python frameworks.",
        "technologies": "Python,Django,Flask,FastAPI,SQL,Tableau,Power BI"
    }
    ]
    
    for work in work_data:
        work_obj = models.WorkExperience(**work)
        db.add(work_obj)
    
    # Create links
    links_data = [
        {"platform": "github", "url": "https://github.com/Dipu1764", "display_name": "GitHub Profile"},
        {"platform": "linkedin", "url": "https://www.linkedin.com/in/deepakkumhar129", "display_name": "LinkedIn Profile"},
        {"platform": "Instagram", "url": "https://www.instagram.com/dipu1764k?igsh=MWttZ3hwb3R1ZHhydA==", "display_name": "@Dipu1764k"},
        # {"platform": "medium", "url": "https://medium.com/@johndoe", "display_name": "Medium Blog"}
    ]
    
    for link in links_data:
        link_obj = models.Link(**link)
        db.add(link_obj)
    
    # Commit all changes
    db.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()