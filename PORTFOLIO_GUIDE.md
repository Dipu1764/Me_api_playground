# 🚀 Dynamic Portfolio Management Guide

Your **Me-API Playground** is now fully dynamic! You can easily update your portfolio content without touching any complex code.

## 📝 Quick Update Process

### Method 1: Simple Update (Recommended)
```bash
# 1. Edit your content in seed_data.py (see configuration sections)
# 2. Run the update script
python update_portfolio.py

# 3. Follow the prompts to deploy your changes
```

### Method 2: Manual Update
```bash
# 1. Edit your content in seed_data.py
# 2. Update the database
python seed_data.py

# 3. Deploy to live site
git add .
git commit -m "Update portfolio content"
git push
```

## ⚙️ Configuration Sections

Edit these sections in `seed_data.py` to update your portfolio:

### 🧑‍💼 Profile Information (`PROFILE_CONFIG`)
```python
PROFILE_CONFIG = {
    "name": "Your Name",
    "email": "your.email@example.com",
    "phone": "+1-234-567-8900",
    "location": "Your City, Country",
    "bio": "Your professional bio...",
    "resume_link": "https://link-to-your-resume.com"
}
```

### 🎓 Education (`EDUCATION_CONFIG`)
```python
EDUCATION_CONFIG = [
    {
        "institution": "University Name",
        "degree": "Degree Type",
        "field_of_study": "Field of Study",
        "start_date": "MM/YYYY",
        "end_date": "MM/YYYY",
        "grade": "GPA/Grade",
        "description": "Description of your studies..."
    }
]
```

### 💪 Skills (`SKILLS_CONFIG`)
```python
SKILLS_CONFIG = [
    {
        "name": "Skill Name",
        "category": "Category (e.g., Programming Languages)",
        "proficiency_level": 5,  # 1-5 scale
        "years_of_experience": 2.0
    }
]
```

### 🚀 Projects (`PROJECTS_CONFIG`)
```python
PROJECTS_CONFIG = [
    {
        "title": "Project Name",
        "description": "What your project does...",
        "technologies": "Python,React,PostgreSQL",  # Comma-separated
        "github_link": "https://github.com/username/repo",
        "live_link": "https://your-project.com",  # Optional
        "demo_link": "https://demo-video-link.com",  # Optional
        "start_date": "YYYY",
        "end_date": "YYYY",
        "status": "completed"  # completed, ongoing, planned
    }
]
```

### 💼 Work Experience (`WORK_CONFIG`)
```python
WORK_CONFIG = [
    {
        "company": "Company Name",
        "position": "Job Title",
        "location": "City, Country",
        "start_date": "MM/YYYY",
        "end_date": "MM/YYYY or Present",
        "description": "What you did in this role...",
        "technologies": "Technologies,Used,Here"
    }
]
```

### 🔗 Social Links (`LINKS_CONFIG`)
```python
LINKS_CONFIG = [
    {
        "platform": "Platform Name",
        "url": "https://your-profile-url.com",
        "display_name": "Display Name"
    }
]
```

## 🛠️ Advanced Features

### Add New Content Quickly
```python
# Add a new project
add_new_project(
    title="My New Project",
    description="Description of what it does",
    technologies="Python,FastAPI,React",
    github_link="https://github.com/user/repo",
    live_link="https://project.com"
)

# Add a new skill
add_new_skill("React", "Frontend Frameworks", 4, 1.5)

# Update your bio
update_profile_bio("New and improved bio description")
```

### Check Portfolio Statistics
```bash
python seed_data.py stats
```

### Available Commands
```bash
python seed_data.py         # Update database with current config
python seed_data.py seed    # Same as above
python seed_data.py stats   # Show portfolio statistics
python seed_data.py help    # Show help information

python update_portfolio.py  # Interactive update with git integration
python update_portfolio.py help  # Show detailed help
```

## 🌐 Your Live URLs

- **Portfolio**: https://me-api-playground-1-sutg.onrender.com/static/index.html
- **API Docs**: https://me-api-playground-1-sutg.onrender.com/docs
- **Health Check**: https://me-api-playground-1-sutg.onrender.com/health

## 📊 Content Categories

Your portfolio dynamically displays:

1. **Profile Information** - Bio, contact details, resume
2. **Education** - Academic background and certifications
3. **Skills** - Technical skills with proficiency levels (1-5 stars)
4. **Projects** - Portfolio projects with GitHub/live links
5. **Work Experience** - Professional background
6. **Social Links** - GitHub, LinkedIn, etc.
7. **Search** - Dynamic search across all content
8. **Filtering** - Filter projects by technology

## 🔄 Auto-Deployment

When you push changes to your GitHub repository:
1. Render automatically detects the changes
2. Runs the build process with your updated seed data
3. Your portfolio is live with new content in ~2-3 minutes

## 💡 Tips

1. **Keep it updated**: Regular updates show you're actively developing
2. **Use specific technologies**: Help visitors filter your projects
3. **Add live links**: Show working projects when possible
4. **Professional bio**: Keep it concise but impactful
5. **Skill levels**: Be honest about your proficiency levels

## 🆘 Need Help?

- Check the console output for any errors
- Verify your configuration syntax in `seed_data.py`
- Test locally first: `python seed_data.py stats`
- Check the live API docs: https://me-api-playground-1-sutg.onrender.com/docs

Your portfolio is now truly dynamic and easy to maintain! 🎉