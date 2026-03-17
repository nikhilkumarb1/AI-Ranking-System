import PyPDF2
import pdfplumber
import docx
import re
from utils import clean_text, extract_email, extract_phone, extract_name
from skill_extractor import extract_skills

def extract_text_from_pdf(file_obj):
    """Extract text from PDF using pdfplumber."""
    text = ""
    try:
        with pdfplumber.open(file_obj) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"pdfplumber failed: {e}. Trying PyPDF2...")
        # Fallback to PyPDF2
        file_obj.seek(0)
        try:
            reader = PyPDF2.PdfReader(file_obj)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        except Exception as e2:
            print(f"PyPDF2 also failed: {e2}")
    return text

def extract_text_from_docx(file_obj):
    """Extract text from DOCX."""
    doc = docx.Document(file_obj)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_experience(text):
    """Extract experience in years using regex."""
    text_lower = text.lower()
    # Look for patterns like "5 years of experience", "5+ years", "3 yrs"
    pattern = r'(\d+)(?:\+)?\s*(?:years?|yrs?)(?:\s+of)?\s+experience'
    matches = re.findall(pattern, text_lower)
    if matches:
        try:
            return max([int(m) for m in matches])
        except:
            pass
            
    # Fallback checking date ranges would be more complex. We simplify here.
    if "experience" in text_lower:
         return 1 # minimum 1 year assumed if experience section exists but no explicit years
    return 0

def extract_education(text):
    """Identify education level."""
    text_lower = text.lower()
    education = []
    if re.search(r'\b(phd|ph\.d|doctorate)\b', text_lower):
        education.append("PhD")
    if re.search(r'\b(master|ms|ma|m\.s|m\.a|mba|mca|mtech)\b', text_lower):
        education.append("Master's")
    if re.search(r'\b(bachelor|bs|ba|b\.s|b\.a|btech|bca|b\.e)\b', text_lower):
        education.append("Bachelor's")
    
    if not education:
        return "Not Specified"
    return ", ".join(education)

def extract_location(text):
    """Extract location using simple checks."""

    # Fallback dictionary of common locations
    common_cities = ['New York', 'San Francisco', 'London', 'Remote', 'Bangalore', 'Seattle', 'Austin', 'Boston', 'Chicago', 'Toronto', 'Delhi', 'Mumbai']
    for city in common_cities:
        if city.lower() in text.lower():
            return city
            
    return "Not Specified"

def parse_resume(file_obj, filename):
    """Parse resume and extract structured data."""
    if filename.lower().endswith('.pdf'):
        text = extract_text_from_pdf(file_obj)
    elif filename.lower().endswith('.docx'):
        text = extract_text_from_docx(file_obj)
    else:
        text = ""

    cleaned_text = clean_text(text)
    
    name = extract_name(text) # Use uncleaned text to keep formatting
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)
    experience_years = extract_experience(text)
    education = extract_education(text)
    location = extract_location(text)
    
    return {
        "filename": filename,
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "experience": experience_years,
        "education": education,
        "location": location,
        "raw_text": cleaned_text
    }
