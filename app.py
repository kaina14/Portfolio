import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Function to load Lottie animations
def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error loading animation")
        return None

# Lottie animation URLs
lottie_intro_url = "https://lottie.host/29848644-5017-4689-969f-c05cce493819/0SfqFN3Pwt.json"  # Replace with your own URL
lottie_skills_url = "https://lottie.host/d1bba083-819f-4115-aff9-31cc5177fbf4/I30jy7hZt9.json" 

# Load Lottie animations
lottie_intro = load_lottie_url(lottie_intro_url)
lottie_skills = load_lottie_url(lottie_skills_url)

# Set page configuration
st.set_page_config(page_title="Kaina Shaikh - Portfolio", page_icon=":star:", layout="wide")

# Custom CSS for styling
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
        
        .sidebar .sidebar-content {
            background-color: #2A2B2E;
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
            width: 100%;
            box-sizing: border-box;
        }
        
        .section-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        
        .section-text {
            flex: 1;
        }

        .section-lottie {
            flex: 1;
            display: flex;
            justify-content: flex-end;
        }
        
        footer {
            margin-top: 20px;
            padding: 20px;
            background-color: #2A2B2E;
            text-align: center;
            color: #FFFFFF;
        }

        .anchor {
            display: block;
            position: relative;
            top: -100px;
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True)


# Sidebar with navigation links
st.sidebar.markdown("<h2 class='section-title'>Navigation</h2>", unsafe_allow_html=True)
st.sidebar.markdown("[Introduction](#introduction)")
st.sidebar.markdown("[Skills](#skills)")
st.sidebar.markdown("[Projects](#projects)")
st.sidebar.markdown("[Research Works and Publications](#research-works-and-publications)")
st.sidebar.markdown("[Achievements](#achievements)")
st.sidebar.markdown("[Services](#services)")
st.sidebar.markdown("[Contact Information](#contact-information)")
st.sidebar.markdown("[Get In Touch](#get-in-touch)")

# Introduction Section
# Introduction Section
st.markdown("<a id='introduction' class='anchor'></a><h2 class='section-title'>Introduction</h2>", unsafe_allow_html=True)

# Use st.columns() to place the text and Lottie animation side by side
with st.container():
    #st.write("---")
    left_column, right_column = st.columns([2, 1])  # Adjust column widths as needed
    with left_column:
        st.markdown("<h5>Hello,</h5>", unsafe_allow_html=True)
        st.markdown("<h2 style='font-size: 3rem;'>I'm Kaina Shaikh!</h2>", unsafe_allow_html=True)
        st.write(
            """
            I am a motivated and dedicated data scientist with a strong passion for artificial intelligence (AI)
            and machine learning (ML). My interests include AI, ML, Quantum Machine Learning, and more.
            """
        )
    with right_column:
        if lottie_intro:
            st_lottie(lottie_intro, height=400, key="intro_animation")

st.button("Download Resume")
#st.markdown("<hr style='border-top: 3px solid #565BF7;'>", unsafe_allow_html=True)
#st.write("Wants to Know More About Me?")
#st.text_input("Ask Anything About Me !!", "")


# Skills Section
st.markdown("<a id='skills' class='anchor'></a><h2 class='section-title'>Skills</h2>", unsafe_allow_html=True)

# Use st.columns() to place the text and Lottie animation side by side
with st.container():
    #st.write("---")
    left_column, right_column = st.columns([2, 1])  # Adjust column widths as needed
    with left_column:
        #st.write("##")
        st.write(
            """
            Here are some of my technical skills:

            
            - **Programming Languages :** 
              C++, Python, SQL
            - **Tools & Libraries :** 
              Git, Numpy, Matplotlib, Sklearn, Pandas, Tensorflow, Pytorch, OpenCV, Streamlit
            - **Visualization :**
              PowerBI, Tableau
            - **Technologies :** 
              Data Science, Artificial Intelligence, Machine Learning, Deep Learning, Quantum AI

            """
        )
    with right_column:
        if lottie_skills:
            st_lottie(lottie_skills, height=200, key="skills_animation")


# Projects Section
st.markdown("<a id='projects' class='anchor'></a><h2 class='section-title'>Projects</h2>", unsafe_allow_html=True)
st.write("---")

# Set up the grid layout for the projects
col1, col2 = st.columns(2)

# Project 1
with col1:
    st.image("https://via.placeholder.com/300", width=300, caption="Project 1")
    st.markdown("""
    **Project 1:** A web application that provides movie recommendations based on user preferences. 
    This project involves building a machine learning model that suggests movies to users based on 
    their past viewing habits and ratings.
    """)

# Project 2
with col2:
    st.image("https://via.placeholder.com/300", width=300, caption="Project 2")
    st.markdown("""
    **Project 2:** A Streamlit-based web app that colorizes black and white images and offers image 
    manipulation features. This project explores the application of deep learning models for 
    image processing tasks.
    """)

# Project 3
with col1:
    st.image("https://via.placeholder.com/300", width=300, caption="Project 3")
    st.markdown("""
    **Project 3:** A data analysis project that uses PowerBI to analyze and forecast sales trends. 
    This project focuses on data visualization and business intelligence techniques to drive insights.
    """)

# Project 4
with col2:
    st.image("https://via.placeholder.com/300", width=300, caption="Project 4")
    st.markdown("""
    **Project 4:** A machine learning project for predicting chronic diseases using graph neural networks. 
    The project applies advanced machine learning techniques to healthcare data.
    """)

# Research Works and Publications Section
st.markdown("<a id='research-works-and-publications' class='anchor'></a><h2 class='section-title'>Research Works and Publications</h2>", unsafe_allow_html=True)
st.write("Details about your research works and publications will go here.")

# Achievements Section
st.markdown("<a id='achievements' class='anchor'></a><h2 class='section-title'>Achievements</h2>", unsafe_allow_html=True)
st.write("Details about your achievements will go here.")

# Services Section
st.markdown("<a id='services' class='anchor'></a><h2 class='section-title'>Services</h2>", unsafe_allow_html=True)
st.write("Details about services you offer will go here.")

# Contact Information Section
st.markdown("<a id='contact-information' class='anchor'></a><h2 class='section-title'>Contact Information</h2>", unsafe_allow_html=True)
st.write("Feel free to reach out to me via email or connect with me on LinkedIn.")
st.markdown("📧 Email: kainashaikh@gmail.com")
st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/kaina-s-351101225/)")
st.markdown("🖥️ [GitHub](https://github.com/kaina14)")

# Get In Touch Section
st.markdown("<a id='get-in-touch' class='anchor'></a><h2 class='section-title'>Get In Touch</h2>", unsafe_allow_html=True)
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
