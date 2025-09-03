# Database Schema Documentation

This document describes the database schema used in the Me-API Playground project.

## Database Type
SQLite (for simplicity and portability)

## Tables

### 1. profiles
Stores the main profile information.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier |
| name | VARCHAR(100) | NOT NULL | Full name |
| email | VARCHAR(100) | NOT NULL, UNIQUE | Email address |
| phone | VARCHAR(20) | NULL | Phone number |
| location | VARCHAR(100) | NULL | Current location |
| bio | TEXT | NULL | Short biography |
| resume_link | VARCHAR(255) | NULL | Link to resume/CV |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Record creation time |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP ON UPDATE | Last update time |

### 2. education
Stores educational background information.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier |
| institution | VARCHAR(200) | NOT NULL | School/University name |
| degree | VARCHAR(100) | NOT NULL | Degree type (Bachelor's, Master's, etc.) |
| field_of_study | VARCHAR(100) | NULL | Major/Field of study |
| start_date | VARCHAR(20) | NULL | Start date (MM/YYYY format) |
| end_date | VARCHAR(20) | NULL | End date (MM/YYYY format) |
| grade | VARCHAR(20) | NULL | Grade/GPA |
| description | TEXT | NULL | Additional details |
| profile_id | INTEGER | FOREIGN KEY, DEFAULT 1 | References profiles.id |

### 3. skills
Stores technical and soft skills.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier |
| name | VARCHAR(100) | NOT NULL | Skill name |
| category | VARCHAR(50) | NULL | Skill category (Programming, Tools, etc.) |
| proficiency_level | INTEGER | DEFAULT 1 | Skill level (1-5 scale) |
| years_of_experience | FLOAT | NULL | Years of experience with this skill |
| profile_id | INTEGER | FOREIGN KEY, DEFAULT 1 | References profiles.id |

### 4. projects
Stores project information.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier |
| title | VARCHAR(200) | NOT NULL | Project title |
| description | TEXT | NOT NULL | Project description |
| technologies | VARCHAR(500) | NULL | Comma-separated list of technologies |
| github_link | VARCHAR(255) | NULL | GitHub repository link |
| live_link | VARCHAR(255) | NULL | Live deployment link |
| demo_link | VARCHAR(255) | NULL | Demo video/presentation link |
| start_date | VARCHAR(20) | NULL | Project start date |
| end_date | VARCHAR(20) | NULL | Project end date |
| status | VARCHAR(20) | DEFAULT 'completed' | Project status |
| profile_id | INTEGER | FOREIGN KEY, DEFAULT 1 | References profiles.id |

### 5. work_experience
Stores work experience information.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier |
| company | VARCHAR(200) | NOT NULL | Company name |
| position | VARCHAR(100) | NOT NULL | Job title/position |
| location | VARCHAR(100) | NULL | Work location |
| start_date | VARCHAR(20) | NULL | Employment start date |
| end_date | VARCHAR(20) | NULL | Employment end date (or "Present") |
| description | TEXT | NULL | Job responsibilities and achievements |
| technologies | VARCHAR(500) | NULL | Technologies used in this role |
| profile_id | INTEGER | FOREIGN KEY, DEFAULT 1 | References profiles.id |

### 6. links
Stores social media and portfolio links.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier |
| platform | VARCHAR(50) | NOT NULL | Platform name (github, linkedin, etc.) |
| url | VARCHAR(255) | NOT NULL | Link URL |
| display_name | VARCHAR(100) | NULL | Display name for the link |
| profile_id | INTEGER | FOREIGN KEY, DEFAULT 1 | References profiles.id |

## Relationships

- All tables (except profiles) have a foreign key relationship with the profiles table
- One profile can have multiple education records, skills, projects, work experiences, and links
- This design assumes a single-user application (profile_id defaults to 1)

## Indexes

The following indexes are automatically created:
- Primary key indexes on all id columns
- Unique index on profiles.email
- Foreign key indexes on all profile_id columns

## Notes

1. Date fields use VARCHAR instead of DATE for flexibility (allows formats like "MM/YYYY")
2. Technologies are stored as comma-separated strings for simplicity
3. The schema is designed for a single-user application but can be extended for multi-user scenarios
4. SQLite is used for simplicity and portability, but the schema can easily be adapted for PostgreSQL or MySQL