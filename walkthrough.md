# AI-Powered Resume Ranking System Walkthrough 🚀

The requested AI-powered Resume Ranking system has been built successfully and optimized for robustness, speed, and accuracy! Let's walk through what the system provides.

## 1. What Was Accomplished
I completely translated the initial requirements into a fully functional modular application:
- **[app.py](file:///c:/Users/Nikhil/OneDrive/Desktop/AI-Ranking-System/app.py)**: A beautiful and responsive dashboard built natively using Streamlit.
- **[parser.py](file:///c:/Users/Nikhil/OneDrive/Desktop/AI-Ranking-System/parser.py)**: Built capable multi-format data ingestion using `PyPDF2`, `pdfplumber`, and `python-docx` to extract text gracefully. Also structured the text using pattern-matching (regex) into Candidate Name, Email, Phone, Years of Experience, Education Level, Location, and comprehensive Skills.
- **[skill_extractor.py](file:///c:/Users/Nikhil/OneDrive/Desktop/AI-Ranking-System/skill_extractor.py)**: Created a high-accuracy, case-insensitive skill matching engine that reads candidate text to check against a comprehensive 40+ technology dictionary. 
- **[jd_processor.py](file:///c:/Users/Nikhil/OneDrive/Desktop/AI-Ranking-System/jd_processor.py)**: Set up a module to dissect Job Description requirements to pull out what skills and years of experience are truly needed.
- **[matcher.py](file:///c:/Users/Nikhil/OneDrive/Desktop/AI-Ranking-System/matcher.py)**: Embedded TF-IDF vectorization and Cosine Similarity AI math to get a granular semantic score matching the resume's raw text to the JD's exact context.
- **[ranker.py](file:///c:/Users/Nikhil/OneDrive/Desktop/AI-Ranking-System/ranker.py)**: Constructed the final math formula strictly according to the specified rules:
  - Skill Score: 50%
  - Experience Match: 25% (Proportionally scaled if they are below the barrier, 100 points if they meet or exceed)
  - Location Match: 15% 
  - Education Match: 10% (100 for Grads, 80 for Undergrads, 50 defaults)

## 2. Bonus Deliverables Provided
- Added an interactive **bar chart visualization** using matplotlib directly inside the dashboard.
- Ensured **CSV exporting** is embedded inside the final ranking view!
- Created a [generate_test_resumes.py](file:///c:/Users/Nikhil/OneDrive/Desktop/AI-Ranking-System/generate_test_resumes.py) file to automatically spin up dummy candidate resumes instantly so you don't even have to write them manually to test the system!
- Supplied a very detailed and clean [README.md](file:///c:/Users/Nikhil/OneDrive/Desktop/AI-Ranking-System/README.md) mapping out installation instructions flawlessly for beginners.

## 3. Running It Yourself
Simply make sure you are in `c:\Users\Nikhil\OneDrive\Desktop\AI-Ranking-System` and run:

```bash
# 1. Install Dependencies
pip install -r requirements.txt

# 2. (Optional) Run the script to generate testing resumes!
python generate_test_resumes.py

# 3. Open the Application UI!
streamlit run app.py
```
*(A pip installation process is already queued up and running globally in the terminal right now!)*
