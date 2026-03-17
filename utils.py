import re

def clean_text(text):
    """Clean and normalize extracted text."""
    if not text:
        return ""
    # Remove special characters but keep punctuation
    text = re.sub(r'[^\w\s\.,;:-]', ' ', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_email(text):
    """Extract email using regex."""
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    matches = re.findall(email_pattern, text)
    return matches[0] if matches else None

def extract_phone(text):
    """Extract phone number using regex."""
    phone_pattern = r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'
    matches = re.findall(phone_pattern, text)
    return matches[0] if matches else None

def extract_name(text):
    """Extract name from the first few lines of text."""
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if lines:
        # Avoid lines that look like a header or very long lines
        for line in lines[:5]:
            if 2 <= len(line.split()) <= 4 and not re.search(r'\d', line) and "resume" not in line.lower() and "curriculum" not in line.lower():
                return line
        return lines[0] # Fallback to first line
    return "Unknown Candidate"
