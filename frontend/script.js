// API Configuration
// Auto-detect environment: use current domain in production, localhost in development
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' 
    ? 'http://localhost:8001' 
    : window.location.origin;

// Global state
let allProjects = [];
let allSkills = [];

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    checkApiHealth();
    loadProfileData();
    setupEventListeners();
});

// Setup event listeners
function setupEventListeners() {
    // Search input enter key
    document.getElementById('search-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });
}

// Check API health
async function checkApiHealth() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        const data = await response.json();
        
        if (data.status === 'ok') {
            updateApiStatus(true, 'API Online');
        } else {
            updateApiStatus(false, 'API Issues');
        }
    } catch (error) {
        updateApiStatus(false, 'API Offline');
    }
}

// Update API status indicator
function updateApiStatus(isOnline, message) {
    const indicator = document.getElementById('status-indicator');
    const text = document.getElementById('status-text');
    
    indicator.className = `status-indicator ${isOnline ? 'online' : 'offline'}`;
    text.textContent = message;
}

// Load all profile data when page loads
async function loadProfileData() {
    await Promise.all([
        loadProfile(),
        loadEducation(),
        loadWorkExperience(),
        loadLinks(),
        loadProjects(),
        loadSkills()
    ]);
}

// Load profile information
async function loadProfile() {
    try {
        const response = await fetch(`${API_BASE_URL}/profile`);
        const profile = await response.json();
        
        document.getElementById('profile-info').innerHTML = `
            <h3>${profile.name}</h3>
            <p><strong>Email:</strong> ${profile.email}</p>
            ${profile.phone ? `<p><strong>Phone:</strong> ${profile.phone}</p>` : ''}
            ${profile.location ? `<p><strong>Location:</strong> ${profile.location}</p>` : ''}
            ${profile.bio ? `<p><strong>Bio:</strong> ${profile.bio}</p>` : ''}
            ${profile.resume_link ? `<p><strong>Resume:</strong> <a href="${profile.resume_link}" target="_blank">View Resume</a></p>` : ''}
        `;
    } catch (error) {
        document.getElementById('profile-info').innerHTML = '<div class="error">Failed to load profile information</div>';
    }
}

// Load education
async function loadEducation() {
    try {
        const response = await fetch(`${API_BASE_URL}/education`);
        const education = await response.json();
        
        const educationHtml = education.map(edu => `
            <div class="list-item">
                <h3>${edu.degree} in ${edu.field_of_study || 'General Studies'}</h3>
                <div class="meta">${edu.institution} • ${edu.start_date} - ${edu.end_date}</div>
                ${edu.grade ? `<p><strong>Grade:</strong> ${edu.grade}</p>` : ''}
                ${edu.description ? `<div class="description">${edu.description}</div>` : ''}
            </div>
        `).join('');
        
        document.getElementById('education-list').innerHTML = educationHtml || '<p>No education information available.</p>';
    } catch (error) {
        document.getElementById('education-list').innerHTML = '<div class="error">Failed to load education information</div>';
    }
}

// Load work experience
async function loadWorkExperience() {
    try {
        const response = await fetch(`${API_BASE_URL}/work`);
        const work = await response.json();
        
        const workHtml = work.map(w => `
            <div class="list-item">
                <h3>${w.position}</h3>
                <div class="meta">${w.company} • ${w.location || ''} • ${w.start_date} - ${w.end_date}</div>
                ${w.description ? `<div class="description">${w.description}</div>` : ''}
                ${w.technologies ? `
                    <div class="project-tech">
                        <strong>Technologies:</strong><br>
                        ${w.technologies.split(',').map(tech => `<span class="tech-tag">${tech.trim()}</span>`).join('')}
                    </div>
                ` : ''}
            </div>
        `).join('');
        
        document.getElementById('work-list').innerHTML = workHtml || '<p>No work experience available.</p>';
    } catch (error) {
        document.getElementById('work-list').innerHTML = '<div class="error">Failed to load work experience</div>';
    }
}

// Load links
async function loadLinks() {
    try {
        const response = await fetch(`${API_BASE_URL}/links`);
        const links = await response.json();
        
        const linksHtml = links.map(link => `
            <div class="link-card">
                <div class="link-platform">${link.platform}</div>
                <a href="${link.url}" target="_blank">${link.display_name || link.url}</a>
            </div>
        `).join('');
        
        document.getElementById('links-list').innerHTML = linksHtml || '<p>No links available.</p>';
    } catch (error) {
        document.getElementById('links-list').innerHTML = '<div class="error">Failed to load links</div>';
    }
}

// Load projects
async function loadProjects() {
    try {
        const response = await fetch(`${API_BASE_URL}/projects`);
        allProjects = await response.json();
        
        displayProjects(allProjects);
        populateSkillFilter();
    } catch (error) {
        document.getElementById('projects-list').innerHTML = '<div class="error">Failed to load projects</div>';
    }
}

// Display projects
function displayProjects(projects) {
    const projectsHtml = projects.map(project => `
        <div class="project-card">
            <div class="project-title">${project.title}</div>
            <div class="project-meta">${project.start_date} - ${project.end_date} • Status: ${project.status}</div>
            <div class="project-description">${project.description}</div>
            ${project.technologies ? `
                <div class="project-tech">
                    <strong>Technologies:</strong><br>
                    ${project.technologies.split(',').map(tech => `<span class="tech-tag">${tech.trim()}</span>`).join('')}
                </div>
            ` : ''}
            <div class="project-links">
                ${project.github_link ? `<a href="${project.github_link}" target="_blank" class="project-link">GitHub</a>` : ''}
                ${project.live_link ? `<a href="${project.live_link}" target="_blank" class="project-link">Live Demo</a>` : ''}
                ${project.demo_link ? `<a href="${project.demo_link}" target="_blank" class="project-link">Video Demo</a>` : ''}
            </div>
        </div>
    `).join('');
    
    document.getElementById('projects-list').innerHTML = projectsHtml || '<p>No projects available.</p>';
}

// Populate skill filter dropdown
function populateSkillFilter() {
    const technologies = new Set();
    allProjects.forEach(project => {
        if (project.technologies) {
            project.technologies.split(',').forEach(tech => {
                technologies.add(tech.trim());
            });
        }
    });
    
    const select = document.getElementById('skill-filter');
    select.innerHTML = '<option value="">All Projects</option>';
    
    Array.from(technologies).sort().forEach(tech => {
        select.innerHTML += `<option value="${tech}">${tech}</option>`;
    });
}

// Filter projects by skill
function filterProjects() {
    const selectedSkill = document.getElementById('skill-filter').value;
    
    if (!selectedSkill) {
        displayProjects(allProjects);
        return;
    }
    
    const filteredProjects = allProjects.filter(project => 
        project.technologies && project.technologies.includes(selectedSkill)
    );
    
    displayProjects(filteredProjects);
}

// Load skills
async function loadSkills() {
    try {
        const response = await fetch(`${API_BASE_URL}/skills`);
        allSkills = await response.json();
        
        displayAllSkills(allSkills);
        loadTopSkills();
    } catch (error) {
        document.getElementById('skills-list').innerHTML = '<div class="error">Failed to load skills</div>';
    }
}

// Display all skills
function displayAllSkills(skills) {
    const skillsHtml = skills.map(skill => `
        <div class="skill-card">
            <div class="skill-name">${skill.name}</div>
            <div class="skill-category">${skill.category || 'General'}</div>
            <div class="skill-level">
                ${Array.from({length: 5}, (_, i) => 
                    `<div class="skill-dot ${i < skill.proficiency_level ? 'filled' : ''}"></div>`
                ).join('')}
            </div>
            ${skill.years_of_experience ? `<div class="skill-experience">${skill.years_of_experience} years</div>` : ''}
        </div>
    `).join('');
    
    document.getElementById('skills-list').innerHTML = skillsHtml || '<p>No skills available.</p>';
}

// Load top skills
async function loadTopSkills() {
    try {
        const response = await fetch(`${API_BASE_URL}/skills/top?limit=8`);
        const topSkills = await response.json();
        
        const topSkillsHtml = topSkills.map(skill => `
            <div class="skill-card">
                <div class="skill-name">${skill.name}</div>
                <div class="skill-category">${skill.category || 'General'}</div>
                <div class="skill-level">
                    ${Array.from({length: 5}, (_, i) => 
                        `<div class="skill-dot ${i < skill.proficiency_level ? 'filled' : ''}"></div>`
                    ).join('')}
                </div>
                ${skill.years_of_experience ? `<div class="skill-experience">${skill.years_of_experience} years</div>` : ''}
            </div>
        `).join('');
        
        document.getElementById('top-skills').innerHTML = topSkillsHtml || '<p>No top skills available.</p>';
    } catch (error) {
        document.getElementById('top-skills').innerHTML = '<div class="error">Failed to load top skills</div>';
    }
}

// Perform search
async function performSearch() {
    const query = document.getElementById('search-input').value.trim();
    
    if (!query) {
        document.getElementById('search-results').innerHTML = '<p>Please enter a search term.</p>';
        return;
    }
    
    if (query.length < 2) {
        document.getElementById('search-results').innerHTML = '<p>Search term must be at least 2 characters long.</p>';
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE_URL}/search?q=${encodeURIComponent(query)}`);
        const results = await response.json();
        
        displaySearchResults(results, query);
    } catch (error) {
        document.getElementById('search-results').innerHTML = '<div class="error">Search failed. Please try again.</div>';
    }
}

// Display search results
function displaySearchResults(results, query) {
    const hasResults = results.projects.length > 0 || results.skills.length > 0 || results.work.length > 0;
    
    if (!hasResults) {
        document.getElementById('search-results').innerHTML = `<p>No results found for "${query}".</p>`;
        return;
    }
    
    let html = `<h3>Search Results for "${query}"</h3>`;
    
    if (results.projects.length > 0) {
        html += `
            <div class="search-section">
                <h3>Projects (${results.projects.length})</h3>
                ${results.projects.map(project => `
                    <div class="search-item">
                        <strong>${project.title}</strong><br>
                        ${project.description}
                    </div>
                `).join('')}
            </div>
        `;
    }
    
    if (results.skills.length > 0) {
        html += `
            <div class="search-section">
                <h3>Skills (${results.skills.length})</h3>
                ${results.skills.map(skill => `
                    <div class="search-item">
                        <strong>${skill.name}</strong> - Level ${skill.proficiency_level}/5
                    </div>
                `).join('')}
            </div>
        `;
    }
    
    if (results.work.length > 0) {
        html += `
            <div class="search-section">
                <h3>Work Experience (${results.work.length})</h3>
                ${results.work.map(work => `
                    <div class="search-item">
                        <strong>${work.position}</strong> at ${work.company}
                    </div>
                `).join('')}
            </div>
        `;
    }
    
    document.getElementById('search-results').innerHTML = html;
}

// Tab navigation
function showTab(tabName) {
    // Hide all tab contents
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all tab buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab content
    document.getElementById(tabName).classList.add('active');
    
    // Add active class to clicked button
    const clickedButton = event ? event.target : document.querySelector(`[onclick="showTab('${tabName}')"]`);
    if (clickedButton) {
        clickedButton.classList.add('active');
    }
}

// Utility function to format dates
function formatDate(dateString) {
    if (!dateString) return '';
    
    try {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric' 
        });
    } catch (error) {
        return dateString; // Return original string if parsing fails
    }
}