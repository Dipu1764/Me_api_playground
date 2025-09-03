# Me-API Playground

A comprehensive personal profile API with a minimal frontend interface for showcasing professional information, projects, skills, and work experience.

## 🌟 Features

- **Complete Profile Management**: Store and retrieve personal information, education, skills, projects, and work experience
- **Advanced Query Endpoints**: Filter projects by technology, get top skills, and perform full-text search
- **RESTful API**: Well-structured endpoints with proper HTTP methods and status codes
- **Interactive Frontend**: Clean, responsive web interface for exploring the API
- **Health Monitoring**: API health check endpoint for deployment monitoring
- **Database Schema**: Fully documented SQLite database with proper relationships

## 🏗️ Architecture

```
Me-API Playground/
├── backend/
│   ├── main.py              # FastAPI application and routes
│   ├── models.py            # SQLAlchemy database models
│   ├── schemas.py           # Pydantic schemas for validation
│   ├── database.py          # Database configuration
│   └── seed_data.py         # Sample data seeding script
├── frontend/
│   ├── index.html           # Main HTML interface
│   ├── style.css            # Responsive CSS styling
│   └── script.js            # JavaScript API integration
├── me_api.db                # SQLite database (generated)
├── requirements.txt         # Python dependencies
├── schema.md                # Database schema documentation
└── README.md                # This file
```

## 🛠️ Technology Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Lightweight, serverless database
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server implementation

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with Flexbox/Grid
- **Vanilla JavaScript**: No framework dependencies
- **Fetch API**: For HTTP requests

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Local Setup

1. **Clone/Download the project**
   ```bash
   # If you have the files, navigate to the project directory
   cd me-api-playground
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database with sample data**
   ```bash
   python seed_data.py
   ```

4. **Start the API server**
   ```bash
   python main.py
   ```
   
   The API will be available at: `http://localhost:8000`

5. **Access the frontend**
   Open your browser and navigate to: `http://localhost:8000/static/index.html`

6. **Explore the API documentation**
   FastAPI provides automatic documentation at: `http://localhost:8000/docs`

### Alternative: Using Uvicorn directly
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 📚 API Documentation

### Base URL
```
http://localhost:8000
```

### Health Check
```
GET /health
```
Returns API status information.

**Response:**
```json
{
  "status": "ok",
  "message": "API is running"
}
```

### Profile Endpoints

#### Get Profile
```
GET /profile
```

#### Create Profile
```
POST /profile
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1-555-0123",
  "location": "San Francisco, CA",
  "bio": "Software developer passionate about technology",
  "resume_link": "https://example.com/resume.pdf"
}
```

#### Update Profile
```
PUT /profile
Content-Type: application/json

{
  "name": "John Smith",
  "location": "New York, NY"
}
```

### Skills Endpoints

#### Get All Skills
```
GET /skills
```

#### Get Top Skills
```
GET /skills/top?limit=5
```

#### Create Skill
```
POST /skills
Content-Type: application/json

{
  "name": "Python",
  "category": "Programming Languages",
  "proficiency_level": 5,
  "years_of_experience": 6.0
}
```

### Projects Endpoints

#### Get All Projects
```
GET /projects
```

#### Filter Projects by Technology
```
GET /projects?skill=python
```

#### Get Single Project
```
GET /projects/{project_id}
```

#### Create Project
```
POST /projects
Content-Type: application/json

{
  "title": "E-Commerce Platform",
  "description": "Full-stack e-commerce platform with real-time features",
  "technologies": "Python,FastAPI,React,PostgreSQL",
  "github_link": "https://github.com/username/project",
  "live_link": "https://myproject.com",
  "start_date": "01/2023",
  "end_date": "06/2023",
  "status": "completed"
}
```

### Education Endpoints

#### Get Education
```
GET /education
```

#### Create Education
```
POST /education
Content-Type: application/json

{
  "institution": "Stanford University",
  "degree": "Master of Science",
  "field_of_study": "Computer Science",
  "start_date": "09/2018",
  "end_date": "06/2020",
  "grade": "3.8 GPA",
  "description": "Specialized in Machine Learning"
}
```

### Work Experience Endpoints

#### Get Work Experience
```
GET /work
```

#### Create Work Experience
```
POST /work
Content-Type: application/json

{
  "company": "TechCorp Inc.",
  "position": "Senior Software Engineer",
  "location": "San Francisco, CA",
  "start_date": "07/2021",
  "end_date": "Present",
  "description": "Lead development of microservices architecture",
  "technologies": "Python,FastAPI,PostgreSQL,Docker"
}
```

### Links Endpoints

#### Get Links
```
GET /links
```

#### Create Link
```
POST /links
Content-Type: application/json

{
  "platform": "github",
  "url": "https://github.com/username",
  "display_name": "GitHub Profile"
}
```

### Search Endpoint

#### Search Across All Content
```
GET /search?q=python
```

Returns matching projects, skills, and work experience.

## 🧪 Sample API Calls

### Using cURL

#### Health Check
```bash
curl -X GET "http://localhost:8000/health"
```

#### Get Profile
```bash
curl -X GET "http://localhost:8000/profile"
```

#### Search
```bash
curl -X GET "http://localhost:8000/search?q=python"
```

#### Filter Projects
```bash
curl -X GET "http://localhost:8000/projects?skill=Python"
```

#### Get Top Skills
```bash
curl -X GET "http://localhost:8000/skills/top?limit=5"
```

### Using Python Requests
```python
import requests

# Base URL
base_url = "http://localhost:8000"

# Health check
response = requests.get(f"{base_url}/health")
print(response.json())

# Get profile
response = requests.get(f"{base_url}/profile")
print(response.json())

# Search
response = requests.get(f"{base_url}/search", params={"q": "python"})
print(response.json())

# Create a new skill
skill_data = {
    "name": "Docker",
    "category": "DevOps",
    "proficiency_level": 4,
    "years_of_experience": 3.0
}
response = requests.post(f"{base_url}/skills", json=skill_data)
print(response.json())
```

## 🗄️ Database Schema

The application uses SQLite with the following tables:

- **profiles**: Main profile information
- **education**: Educational background
- **skills**: Technical and soft skills with proficiency levels
- **projects**: Project portfolio with technologies and links
- **work_experience**: Professional work history
- **links**: Social media and portfolio links

For detailed schema information, see [schema.md](schema.md).

## 🎯 Frontend Features

The web interface provides:

- **Profile Overview**: Complete profile information display
- **Project Portfolio**: Filterable project list with technology tags
- **Skills Matrix**: Visual skill representation with proficiency levels
- **Search Functionality**: Real-time search across all content
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **API Status Monitoring**: Real-time API connectivity indicator

## 🔧 Configuration

### Environment Variables
The application can be configured using the following environment variables:

- `DATABASE_URL`: Database connection string (default: SQLite)
- `API_HOST`: API host (default: 0.0.0.0)
- `API_PORT`: API port (default: 8000)

### CORS Configuration
CORS is configured to allow all origins for development. In production, update the `allow_origins` list in `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🚀 Deployment

### Production Deployment Options

1. **Heroku**
   ```bash
   # Create Procfile
   echo "web: uvicorn main:app --host=0.0.0.0 --port=\$PORT" > Procfile
   
   # Deploy
   git init
   git add .
   git commit -m "Initial commit"
   heroku create your-app-name
   git push heroku main
   ```

2. **Railway**
   ```bash
   # Install Railway CLI
   npm install -g @railway/cli
   
   # Login and deploy
   railway login
   railway init
   railway up
   ```

3. **DigitalOcean App Platform**
   - Connect your GitHub repository
   - Configure build and run commands:
     - Build: `pip install -r requirements.txt`
     - Run: `python seed_data.py && uvicorn main:app --host 0.0.0.0 --port 8080`

4. **Docker**
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   RUN python seed_data.py
   
   EXPOSE 8000
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

### Production Considerations

- Use PostgreSQL instead of SQLite for production
- Implement proper authentication for write operations
- Add rate limiting and request validation
- Set up proper logging and monitoring
- Use environment variables for sensitive configuration
- Implement proper error handling and user feedback

## ⚠️ Known Limitations

1. **Single User Design**: Currently designed for single-user profiles
2. **No Authentication**: All endpoints are publicly accessible
3. **SQLite Database**: Not suitable for high-concurrency production use
4. **Basic Search**: Simple text matching, not full-text search with ranking
5. **No Rate Limiting**: API endpoints are not rate-limited
6. **No Caching**: No caching mechanism implemented
7. **Limited Validation**: Basic input validation only

## 🔮 Future Enhancements

- Multi-user support with authentication
- Advanced search with fuzzy matching and relevance scoring
- File upload for resume and project images
- Email notification system
- Admin dashboard with analytics
- API versioning
- Comprehensive test suite
- Performance optimization and caching
- Real-time updates with WebSockets

## 📝 Resume

For John Doe's complete resume, visit: [https://example.com/resume/john-doe.pdf](https://example.com/resume/john-doe.pdf)

## 📄 License

This project is created for educational and demonstration purposes. Feel free to use it as a starting point for your own profile API.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Contact

- **GitHub**: [https://github.com/johndoe](https://github.com/johndoe)
- **LinkedIn**: [https://linkedin.com/in/johndoe](https://linkedin.com/in/johndoe)
- **Email**: john.doe@example.com

---

Built with ❤️ using FastAPI and modern web technologies.#   M e _ a p i _ p l a y g r o u n d 
 
 
