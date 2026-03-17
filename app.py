import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from jd_processor import process_jd
from parser import parse_resume
from ranker import calculate_score

# Page settings
st.set_page_config(page_title="AI Resume Ranking System", page_icon="📄", layout="wide")

st.title("📄 AI-Powered Resume Ranking System")
st.markdown("Upload multiple resumes and rank them seamlessly against a Job Description using our AI-powered engine.")

# Sidebar for Job Description
st.sidebar.header("Job Description Details")
jd_text = st.sidebar.text_area("Paste the Job Description here:", height=300, placeholder="Requirements, technologies, experience needed...")

jd_info = None
if jd_text:
    jd_info = process_jd(jd_text)
    st.sidebar.subheader("Extracted Requirements:")
    st.sidebar.write(f"**Skills:** {', '.join(jd_info['required_skills']) if jd_info['required_skills'] else 'None automatically found'}")
    st.sidebar.write(f"**Experience:** {jd_info['required_experience']} years")
    
# Main panel for Resumes
st.header("Upload Candidate Resumes")
uploaded_files = st.file_uploader("Upload PDF or DOCX format resumes", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("Analyze & Rank Candidates", type="primary"):
    if not jd_text:
        st.error("Please provide a Job Description first.")
    elif not uploaded_files:
        st.error("Please upload at least one resume file.")
    else:
        # Initialize progress bar
        progress_text = "Parsing and matching resumes... Please wait."
        my_bar = st.progress(0, text=progress_text)
        
        results = []
        total_files = len(uploaded_files)
        
        for idx, file in enumerate(uploaded_files):
            # Parse resume file stream directly
            parsed_data = parse_resume(file, file.name)
            
            # Calculate final score
            scores = calculate_score(parsed_data, jd_info)
            
            # Combine data for DataFrame
            candidate_result = {
                "Rank": 0, # Placeholder
                "Name": parsed_data["name"],
                "Skills": ", ".join(parsed_data["skills"]) if parsed_data["skills"] else "None",
                "Experience (Yrs)": parsed_data["experience"],
                "Education": parsed_data["education"],
                "Score": scores["final_score"],
                "Skill Match": scores["skill_score"],
                "Location": parsed_data["location"],
                "Phone": parsed_data["phone"] or "N/A",
                "Email": parsed_data["email"] or "N/A"
            }
            results.append(candidate_result)
            
            # Update progress
            progress = (idx + 1) / total_files
            my_bar.progress(progress, text=f"Processed {idx+1}/{total_files} resumes...")
            
        my_bar.empty()
        
        # Display Results Dashboard
        st.header("🏆 Ranking Dashboard")
        
        # Format DataFrame
        df = pd.DataFrame(results)
        df = df.sort_values(by="Score", ascending=False).reset_index(drop=True)
        df.index += 1 # Ensure 1-based index
        df["Rank"] = df.index
        
        # Top Metrics Cards
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Candidates Processed", len(df))
        col2.metric("Highest Score", f"{df['Score'].max():.2f}")
        col3.metric("Average Score", f"{df['Score'].mean():.2f}")
        
        # Detailed Table
        st.subheader("Leaderboard")
        st.dataframe(
            df[["Rank", "Name", "Skills", "Experience (Yrs)", "Education", "Location", "Score"]],
            use_container_width=True,
            hide_index=True
        )
        
        st.markdown("---")
        
        # Visualization
        st.subheader("📊 Top Candidates Overview")
        fig, ax = plt.subplots(figsize=(10, 5))
        # Take up to top 10 for neat visualization
        top_df = df.head(10)
        bars = ax.bar(top_df["Name"], top_df["Score"], color='#4c72b0')
        ax.set_ylabel("Final Ranking Score")
        ax.set_xlabel("Candidate Name")
        ax.set_title("Scores for the Top Candidates")
        ax.set_ylim(0, 100) # Assuming score max is near 100
        plt.xticks(rotation=45, ha='right')
        
        # Add labels on top of bars
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 1), ha='center', va='bottom', fontsize=9)
            
        st.pyplot(fig)
        
        # Export to CSV Feature
        st.subheader("⬇️ Actions")
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Complete Results (CSV)",
            data=csv_data,
            file_name='resume_ranking_results.csv',
            mime='text/csv',
        )

        st.success("Successfully analyzed and ranked all resumes!")
