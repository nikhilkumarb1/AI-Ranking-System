from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_text_similarity(text1, text2):
    """Calculate TF-IDF cosine similarity between two texts."""
    if not text1 or not text2:
        return 0.0
        
    vectorizer = TfidfVectorizer(stop_words='english')
    try:
        tfidf_matrix = vectorizer.fit_transform([text1, text2])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return float(similarity)
    except:
        return 0.0

def get_skill_overlap(candidate_skills, required_skills):
    """Calculate percentage overlap of candidate skills with required skills."""
    if not required_skills:
        return 1.0 # If no skills required, perfect match
    if not candidate_skills:
        return 0.0
        
    candidate_set = set(s.lower() for s in candidate_skills)
    required_set = set(s.lower() for s in required_skills)
    
    overlap = candidate_set.intersection(required_set)
    return len(overlap) / len(required_set)
