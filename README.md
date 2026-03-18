# AI-Powered Resume Ranking System 📄

An AI-driven application that parses multiple candidate resumes (PDF/DOCX), extracts their skills, experience, and education using NLP, and ranks them against a provided Job Description. Built entirely in Python using Streamlit, and scikit-learn.

## Features
- **Multi-Format Parsing:** Support for PDF and DOCX files.
- **NLP Data Extraction:** Identifies technical skills, tools, and platforms. Extracts standard info (Name, Email, Phone, Experience in Years).
- **AI Matching Engine:** Uses TF-IDF and Cosine Similarity alongside direct skill overlapping to calculate an accurate match score.
- **Weighted Ranking Algorithm:**
  - Skills Match: 50%
  - Experience: 25%
  - Location: 15%
  - Education: 10%
- **Interactive Dashboard:** Beautiful Streamlit UI to view leaderboards, detailed extraction info, and interactive bar charts.
- **Data Export:** Download the ranked candidate results natively as a CSV file.

## Project Structure
- `app.py`: Main Streamlit frontend and application lifecycle.
- `parser.py`: PDF/DOCX handling using `PyPDF2`, `pdfplumber`, and `python-docx`. Information parsing using regular expressions.
- `jd_processor.py`: Structures the Job Description text.
- `skill_extractor.py`: Custom skill mapping logic.
- `matcher.py`: TF-IDF cosine similarity model.
- `ranker.py`: Final weighted score mathematical calculations.
- `utils.py`: Text cleaning and basic regex utility functions.

## Setup Instructions

**1. Create a Virtual Environment (Optional but Recommended):**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
```

**2. Install Requirements:**
```bash
pip install -r requirements.txt
```
*(Note: This includes the lightweight English spaCy model `en_core_web_sm` required for Location extraction)*

**3. Run the Application:**
```bash
streamlit run app.py
```
The application will start immediately and automatically open in your default browser at `http://localhost:8501`.

## Ranking Logic Explained

1. **Skill Match (50%):** We calculate the direct percentage overlap of candidate skills against JD required skills. We optionally mix this with semantic text similarity using TF-IDF for context matching.
2. **Experience Score (25%):** We parse "X years of experience" strings from both JD and resumes. If the candidate meets or surpasses the experience requirement, they get 100% of this weight. Otherwise, it is scaled proportionately.
3. **Location (15%):** Extracted using spaCy's GPE entities or matched against major tech hub lists.
4. **Education (10%):** A simple heuristic rewards graduate degrees (PhD, Master's) slightly higher than standard Bachelor's degrees.
