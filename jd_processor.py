from skill_extractor import extract_skills
from parser import extract_experience # Will be created in parser.py

def process_jd(jd_text):
    """Process Job Description text to extract requirements."""
    required_skills = extract_skills(jd_text)
    required_experience = extract_experience(jd_text)
    
    # If no explicit experience found in JD, default to 0
    if not required_experience:
        required_experience = 0
        
    return {
        "required_skills": required_skills,
        "required_experience": required_experience,
        "raw_text": jd_text
    }
