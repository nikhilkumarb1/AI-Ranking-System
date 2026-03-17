from matcher import get_skill_overlap, get_text_similarity

def calculate_score(parsed_resume, jd_info):
    """
    Calculate the final ranking score based on:
    - Skills Match -> 50%
    - Experience -> 25%
    - Education -> 10%
    - Location -> 15%
    """
    # 1. Skill Score (50%)
    skill_overlap = get_skill_overlap(parsed_resume['skills'], jd_info['required_skills'])
    skill_score = skill_overlap * 100
    
    # Combine with TF-IDF similarity for a richer score (70% overlap, 30% semantic text match)
    text_sim = get_text_similarity(parsed_resume['raw_text'], jd_info['raw_text'])
    combined_skill_score = (skill_score * 0.7) + (text_sim * 100 * 0.3)
    
    # 2. Experience Score (25%)
    req_exp = jd_info['required_experience']
    cand_exp = parsed_resume['experience']
    
    if req_exp == 0:
        exp_score = 100 # If no experience required, any experience is good
    elif cand_exp >= req_exp:
        exp_score = 100
    else:
        exp_score = (cand_exp / req_exp) * 100
        
    # 3. Education Score (10%)
    education = parsed_resume['education']
    # Simple heuristic
    if "PhD" in education or "Master's" in education:
        edu_score = 100
    elif "Bachelor's" in education:
        edu_score = 80
    else:
        edu_score = 50 # Default score if not specified or lower degree
        
    # 4. Location Score (15%)
    location = parsed_resume['location']
    if location != "Not Specified":
        loc_score = 100
    else:
        loc_score = 50 # Penalize slightly if not specified
        
    # Final Weighted Score
    final_score = (combined_skill_score * 0.50) + (exp_score * 0.25) + (edu_score * 0.10) + (loc_score * 0.15)
    
    return {
        "final_score": round(final_score, 2),
        "skill_score": round(combined_skill_score, 2),
        "exp_score": round(exp_score, 2),
        "edu_score": round(edu_score, 2),
        "loc_score": round(loc_score, 2)
    }
