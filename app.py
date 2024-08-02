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
            display: inline-block;
        }
        
        .section-content {
            margin-top: 20px;
        }
        
        .sidebar .sidebar-content {
            background-color: #2A2B2E;
            padding: 20px;
        }

        .sidebar .sidebar-content h1 {
            text-align: center;
            margin-bottom: 20px;
        }

        .sidebar .sidebar-content .sidebar-nav {
            font-size: 1.2rem;
            color: #FFFFFF;
            list-style: none;
            padding: 0;
        }

        .sidebar .sidebar-content .sidebar-nav li {
            margin-bottom: 10px;
        }

        .sidebar .sidebar-content .sidebar-nav li a {
            color: #E5E5E5;
            text-decoration: none;
            display: block;
            padding: 10px;
            border-radius: 5px;
            background-color: #3A3B3D;
            transition: background-color 0.3s;
        }

        .sidebar .sidebar-content .sidebar-nav li a:hover {
            background-color: #565BF7;
            color: #FFFFFF;
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

# Sidebar Navigation
st.sidebar.title("Kaina Shaikh")
st.sidebar.markdown("<h3 style='color: #E5E5E5;'>Navigation</h3>", unsafe_allow_html=True)
pages = st.sidebar.radio("Go to", ["Introduction", "Skills", "Projects", "Research Works and Publications", "Achievements", "Services", "Contact Information", "Get In Touch"])

# Introduction Section
if pages == "Introduction":
    st.markdown("<h2 class='section-title'>Introduction</h2>", unsafe_allow_html=True)
    st.markdown("<h3>Hello,</h3>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 3rem;'>I'm Kaina Shaikh!</h1>", unsafe_allow_html=True)
    st.write("I am a motivated and dedicated data scientist with a strong passion for artificial intelligence (AI) and machine learning (ML). My interests include AI, ML, Quantum Machine Learning, and more.")
    st.button("Download Resume")
    st.markdown("<hr style='border-top: 3px solid #565BF7;'>", unsafe_allow_html=True)
    st.write("Wants to Know More About Me?")
    st.text_input("Ask Anything About Me !!", "")

# Skills Section
elif pages == "Skills":
    st.markdown("<h2 class='section-title'>Skills</h2>", unsafe_allow_html=True)
    st.write("Here are some of my technical skills:")
    skills = ["C++", "Python", "SQL", "Git", "Numpy", "Matplotlib", "Sklearn", "Pandas", 
              "Tensorflow", "Pytorch", "OpenCV", "Streamlit", "Data Science", "Artificial Intelligence",
              "Machine Learning", "Deep Learning", "Quantum AI", "PowerBI", "Tableau"]
    
    for skill in skills:
        st.button(skill)

# Projects Section
elif pages == "Projects":
    st.markdown("<h2 class='section-title'>Projects</h2>", unsafe_allow_html=True)
    project_data = {
        "Cyclone Intensity Estimation": "Developed a Quantum Machine Learning Algorithm achieving 93% accuracy.",
        "Superstore Sales Analysis": "Designed a PowerBI dashboard to forecast sales, identify KPIs, and analyze trends.",
        "Crop Recommendation System": "Developed a recommendation system using Random Forest and Naive Bayes, achieving 99% accuracy.",
        "Chronic Disease Prediction": "Implemented Graph Neural Networks for disease prediction, achieving 98% accuracy."
    }

    for project, description in project_data.items():
        with st.expander(f"{project}"):
            st.write(description)

# Research Works and Publications Section
elif pages == "Research Works and Publications":
    st.markdown("<h2 class='section-title'>Research Works and Publications</h2>", unsafe_allow_html=True)
    st.write("Details about your research works and publications will go here.")

# Achievements Section
elif pages == "Achievements":
    st.markdown("<h2 class='section-title'>Achievements</h2>", unsafe_allow_html=True)
    st.write("Details about your achievements will go here.")

# Services Section
elif pages == "Services":
    st.markdown("<h2 class='section-title'>Services</h2>", unsafe_allow_html=True)
    st.write("Details about services you offer will go here.")

# Contact Information Section
elif pages == "Contact Information":
    st.markdown("<h2 class='section-title'>Contact Information</h2>", unsafe_allow_html=True)
    st.write("Feel free to reach out to me via email or connect with me on LinkedIn.")
    st.markdown("📧 Email: kainashaikh@gmail.com")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/kaina-s-351101225/)")
    st.markdown("🖥️ [GitHub](https://github.com/kaina14)")

# Get In Touch Section
elif pages == "Get In Touch":
    st.markdown("<h2 class='section-title'>Get In Touch</h2>", unsafe_allow_html=True)
    st.write("Please fill out the form below to get in touch with me.")
    st.text_input("Your Name", "")
    st.text_input("Your Email", "")
    st.text_area("Your Message", "")
    st.button("Send Message")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2024 Kaina Shaikh")
