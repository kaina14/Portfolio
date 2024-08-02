import streamlit as st
from PIL import Image

# Configuration
st.set_page_config(page_title="Kaina Shaikh - Portfolio", page_icon=":star:", layout="wide")

# Header Section
st.header("Kaina Shaikh")
st.subheader("Data Scientist & Machine Learning Engineer")
st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/kaina-s-351101225) | 🖥️ [GitHub](https://github.com/kaina14)")

# Add a separator
st.markdown("---")

# About Me Section
st.write("## About Me")
st.write("""
I am a Data Scientist and Machine Learning Engineer with a passion for developing innovative solutions using AI and ML techniques.
With a strong background in AI, data science, and quantum machine learning, I have hands-on experience in multiple projects and internships.
""")

# Skills Section
st.write("## Skills")
skills = ["C++", "Python", "SQL", "Git", "Numpy", "Matplotlib", "Sklearn", "Pandas", 
          "Tensorflow", "Pytorch", "OpenCV", "Streamlit", "Data Science", "Artificial Intelligence",
          "Machine Learning", "Deep Learning", "Quantum AI", "PowerBI", "Tableau"]

columns = st.columns(3)
for i, skill in enumerate(skills):
    with columns[i % 3]:
        st.button(skill)

# Experience Section
st.write("## Experience")
st.write("""
### Research Intern - DRDO
- Worked on a Defect Detection system using Deep Learning, improving model accuracy by 11%.
- Implemented and fine-tuned YOLOv8 algorithm.

### Machine Learning Apprenticeship - Amazon
- Implemented core ML concepts including Reinforcement Learning, Recommendation Systems, and Deep Learning.
- Developed practical ML applications.

### Microsoft ENGAGE Intern
- Developed a Face Recognition App using Microsoft Cognitive Services.
- Integrated features like Smart Attendance System and Emotion Recognition.
""")

# Projects Section
st.write("## Projects")
project_data = {
    "Cyclone Intensity Estimation": "Developed a Quantum Machine Learning Algorithm achieving 93% accuracy, demonstrating quantum advantage over classical models.",
    "Superstore Sales Analysis": "Designed a PowerBI dashboard to forecast sales, identify KPIs, and analyze trends by location and time.",
    "Crop Recommendation System": "Developed a recommendation system using Random Forest and Naive Bayes, achieving 99% accuracy.",
    "Chronic Disease Prediction": "Implemented Graph Neural Networks for disease prediction, achieving 98% accuracy."
}

for project, description in project_data.items():
    st.write(f"### {project}")
    st.write(description)

# Publications Section
st.write("## Publications")
st.write("""
- [Deep Learning based Defect Detection and Segmentation for High Energy Material Applications](https://www.irjet.net/archives/V11/i6/IRJET-V11I6183.pdf)
- Benchmarking Traditional and Graph Neural Network Models for Node Classification in Literature Characters
""")

# Achievements Section
st.write("## Achievements")
achievements = [
    "Harvard WECode Scholar: Received Harvard Women Engineers Scholarship.",
    "Google Women In Cloud Summit: Host-participant member.",
    "Poster Presentation at HEMCE Conference organized by ISRO and DRDO.",
    "Top 10% in Python Programming, IIT Kharagpur.",
    "Completed the International Program for Quantum Machine Learning by Microsoft."
]

st.write("\n".join([f"- {achievement}" for achievement in achievements]))

# Contact Section
st.write("## Contact")
st.write("Feel free to reach out to me via email at kainashaikh@gmail.com or connect with me on [LinkedIn](https://www.linkedin.com/in/kaina-s-351101225/).")

# Add a footer with some spacing
st.markdown("---")
st.write("© 2024 Kaina Shaikh")
