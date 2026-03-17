import re

# Predefined skill dictionary based on requirements
SKILL_DICTIONARY = [
    "Python", "Java", "SQL", "Machine Learning", "AWS", "Docker", "React", "Node.js",
    "Azure", "GCP", "C++", "C#", "JavaScript", "TypeScript", "HTML", "CSS", "Angular",
    "Vue.js", "Spring Boot", "Django", "Flask", "FastAPI", "TensorFlow", "PyTorch",
    "Scikit-Learn", "Pandas", "NumPy", "NLP", "Computer Vision", "Git", "CI/CD",
    "Kubernetes", "Linux", "Bash", "Agile", "Scrum", "Data Analysis", "Data Science",
    "Big Data", "Spark", "Hadoop", "Tableau", "PowerBI", "Excel", ".NET", "REST API"
]

def extract_skills(text):
    """Extract skills from text by matching against the predefined dictionary."""
    text_lower = text.lower()
    extracted_skills = []
    
    for skill in SKILL_DICTIONARY:
        # Use regex with word boundaries to avoid partial matches (e.g., 'C' matching 'React')
        # Escape skill name to handle C++, C# etc
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            extracted_skills.append(skill)
            
    return list(set(extracted_skills))
