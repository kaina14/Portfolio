import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Kaina Shaikh - Portfolio", page_icon=":star:", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Go to", ["Home", "About Me", "Skills", "Experience", "Projects", "Contact"])

# Home Section
if pages == "Home":
    st.title("Kaina Shaikh")
    st.subheader("Data Scientist & Machine Learning Engineer")
    st.image("https://example.com/your-image-url.jpg", width=300)  # Add your image URL
    st.write("""
    Welcome to my portfolio website! I'm Kaina Shaikh, a passionate Data Scientist and Machine Learning Engineer with expertise in AI, Quantum Machine Learning, and Data Science.
    """)

# About Me Section
elif pages == "About Me":
    st.header("About Me")
    st.write("""
    I am a Data Scientist and Machine Learning Engineer with a passion for developing innovative solutions using AI and ML techniques.
    With a strong background in AI, data science, and quantum machine learning, I have hands-on experience in multiple projects and internships.
    """)

# Skills Section
elif pages == "Skills":
    st.header("Skills")
    st.write("Here are some of my technical skills:")
    skills = ["C++", "Python", "SQL", "Git", "Numpy", "Matplotlib", "Sklearn", "Pandas", 
              "Tensorflow", "Pytorch", "OpenCV", "Streamlit", "Data Science", "Artificial Intelligence",
              "Machine Learning", "Deep Learning", "Quantum AI", "PowerBI", "Tableau"]

    for skill in skills:
        st.button(skill)

# Experience Section
elif pages == "Experience":
    st.header("Experience")
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
elif pages == "Projects":
    st.header("Projects")
    project_data = {
        "Cyclone Intensity Estimation": "Developed a Quantum Machine Learning Algorithm achieving 93% accuracy.",
        "Superstore Sales Analysis": "Designed a PowerBI dashboard to forecast sales, identify KPIs, and analyze trends.",
        "Crop Recommendation System": "Developed a recommendation system using Random Forest and Naive Bayes, achieving 99% accuracy.",
        "Chronic Disease Prediction": "Implemented Graph Neural Networks for disease prediction, achieving 98% accuracy."
    }

    for project, description in project_data.items():
        with st.expander(f"{project}"):
            st.write(description)

# Contact Section
elif pages == "Contact":
    st.header("Contact")
    st.write("Feel free to reach out to me via email or connect with me on LinkedIn.")
    st.markdown("📧 Email: kainashaikh@gmail.com")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/kaina-s-351101225/)")
    st.markdown("🖥️ [GitHub](https://github.com/kaina14)")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2024 Kaina Shaikh")
