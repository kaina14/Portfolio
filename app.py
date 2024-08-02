import streamlit as st

# Set page configuration
st.set_page_config(page_title="Kaina Shaikh - Portfolio", page_icon=":star:", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
        
        body {
            font-family: 'Roboto', sans-serif;
            color: #E5E5E5;
            background-color: #1E1E1E;
        }
        
        .stApp {
            margin: 0 auto;
            padding: 20px;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF;
            font-weight: 700;
        }
        
        .stMarkdown {
            color: #E5E5E5;
        }
        
        .stButton>button {
            background-color: #565BF7;
            color: #FFFFFF;
            font-size: 16px;
            font-weight: 500;
            border-radius: 8px;
            padding: 10px;
            border: none;
            cursor: pointer;
        }
        
        .stButton>button:hover {
            background-color: #4346E0;
        }
        
        .section-title {
            font-size: 2rem;
            margin-bottom: 0.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 3px solid;
            border-image: linear-gradient(to right, #565BF7, #E44D4D) 1;
            display: inline-block;
        }
        
        .section-content {
            margin-top: 20px;
        }
        
        .project-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }
        
        .project-card {
            width: 48%;
            background-color: #2A2B2E;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .project-card img {
            max-width: 100%;
            border-radius: 10px;
        }

        .project-card h4 {
            margin-top: 15px;
            color: #E5E5E5;
            font-size: 1.25rem;
        }

        .project-card p {
            margin-top: 10px;
            color: #C7C7C7;
            font-size: 1rem;
        }

        footer {
            margin-top: 20px;
            padding: 20px;
            background-color: #2A2B2E;
            text-align: center;
            color: #FFFFFF;
        }
        
    </style>
    """, unsafe_allow_html=True)

# Introduction Section
st.markdown("<h2 class='section-title'>Introduction</h2>", unsafe_allow_html=True)
st.markdown("<h3>Hello,</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='font-size: 3rem;'>I'm Kaina Shaikh!</h1>", unsafe_allow_html=True)
st.write("I am a motivated and dedicated data scientist with a strong passion for artificial intelligence (AI) and machine learning (ML). My interests include AI, ML, Quantum Machine Learning, and more.")
st.button("Download Resume")
st.markdown("<hr style='border-top: 3px solid #565BF7;'>", unsafe_allow_html=True)
st.write("Wants to Know More About Me?")
st.text_input("Ask Anything About Me !!", "")

# Skills Section
st.markdown("<h2 class='section-title'>Skills</h2>", unsafe_allow_html=True)
st.write("Here are some of my technical skills:")
skills = ["C++", "Python", "SQL", "Git", "Numpy", "Matplotlib", "Sklearn", "Pandas", 
          "Tensorflow", "Pytorch", "OpenCV", "Streamlit", "Data Science", "Artificial Intelligence",
          "Machine Learning", "Deep Learning", "Quantum AI", "PowerBI", "Tableau"]

for skill in skills:
    st.button(skill)

# Projects Section
st.markdown("<h2 class='section-title'>Projects</h2>", unsafe_allow_html=True)
    
# Project 1
st.markdown("""
<div class="project-container">
    <div class="project-card">
        <img src="https://via.placeholder.com/300" alt="Project Image">
        <h4>Project 1</h4>
        <p>A web application that provides movie recommendations based on user preferences.</p>
    </div>
    <div class="project-card">
        <img src="https://via.placeholder.com/300" alt="Project Image">
        <h4>Project 2</h4>
        <p>A Streamlit-based web app that colorizes black and white images and offers image manipulation features.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Project 2
st.markdown("""
<div class="project-container">
    <div class="project-card">
        <img src="https://via.placeholder.com/300" alt="Project Image">
        <h4>Project 3</h4>
        <p>A data analysis project that uses PowerBI to analyze and forecast sales trends.</p>
    </div>
    <div class="project-card">
        <img src="https://via.placeholder.com/300" alt="Project Image">
        <h4>Project 4</h4>
        <p>A machine learning project for predicting chronic diseases using graph neural networks.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Research Works and Publications Section
st.markdown("<h2 class='section-title'>Research Works and Publications</h2>", unsafe_allow_html=True)
st.write("Details about your research works and publications will go here.")

# Achievements Section
st.markdown("<h2 class='section-title'>Achievements</h2>", unsafe_allow_html=True)
st.write("Details about your achievements will go here.")

# Services Section
st.markdown("<h2 class='section-title'>Services</h2>", unsafe_allow_html=True)
st.write("Details about services you offer will go here.")

# Contact Information Section
st.markdown("<h2 class='section-title'>Contact Information</h2>", unsafe_allow_html=True)
st.write("Feel free to reach out to me via email or connect with me on LinkedIn.")
st.markdown("📧 Email: kainashaikh@gmail.com")
st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/kaina-s-351101225/)")
st.markdown("🖥️ [GitHub](https://github.com/kaina14)")

# Get In Touch Section
st.markdown("<h2 class='section-title'>Get In Touch</h2>", unsafe_allow_html=True)
st.write("Please fill out the form below to get in touch with me.")
st.text_input("Your Name", "")
st.text_input("Your Email", "")
st.text_area("Your Message", "")
st.button("Send Message")

# Footer
st.markdown("""
<footer>
    <p>© 2024 Kaina Shaikh</p>
</footer>
""", unsafe_allow_html=True)
