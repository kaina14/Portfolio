import streamlit as st

# Set page configuration
st.set_page_config(page_title="Kaina Shaikh - Portfolio", page_icon=":star:", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #2A2B2E;
            padding: 20px;
        }
        .main {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        .stButton>button {
            background-color: #565BF7;
            color: #FFFFFF;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #4346E0;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF;
        }
        .stMarkdown {
            color: #E5E5E5;
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Go to", ["Introduction", "Skills", "Projects", "Research Works and Publications", "Achievements", "Services", "Contact Information", "Get In Touch"])

# Introduction Section
if pages == "Introduction":
    st.title("Introduction")
    st.header("Hello,")
    st.subheader("I'm Kaina Shaikh!")
    st.write("I am a motivated and dedicated data scientist with a strong passion for artificial intelligence (AI) and machine learning (ML). My interests include AI, ML, Quantum Machine Learning, and more.")
    st.button("Download Resume")
    st.markdown("---")
    st.write("Wants to Know More About Me?")
    st.text_input("Ask Anything About Me !!", "")

# Skills Section
elif pages == "Skills":
    st.title("Skills")
    st.write("Here are some of my technical skills:")
    skills = ["C++", "Python", "SQL", "Git", "Numpy", "Matplotlib", "Sklearn", "Pandas", 
              "Tensorflow", "Pytorch", "OpenCV", "Streamlit", "Data Science", "Artificial Intelligence",
              "Machine Learning", "Deep Learning", "Quantum AI", "PowerBI", "Tableau"]
    
    for skill in skills:
        st.button(skill)

# Projects Section
elif pages == "Projects":
    st.title("Projects")
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
    st.title("Research Works and Publications")
    st.write("Details about your research works and publications will go here.")

# Achievements Section
elif pages == "Achievements":
    st.title("Achievements")
    st.write("Details about your achievements will go here.")

# Services Section
elif pages == "Services":
    st.title("Services")
    st.write("Details about services you offer will go here.")

# Contact Information Section
elif pages == "Contact Information":
    st.title("Contact Information")
    st.write("Feel free to reach out to me via email or connect with me on LinkedIn.")
    st.markdown("📧 Email: kainashaikh@gmail.com")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/kaina-s-351101225/)")
    st.markdown("🖥️ [GitHub](https://github.com/kaina14)")

# Get In Touch Section
elif pages == "Get In Touch":
    st.title("Get In Touch")
    st.write("Please fill out the form below to get in touch with me.")
    st.text_input("Your Name", "")
    st.text_input("Your Email", "")
    st.text_area("Your Message", "")
    st.button("Send Message")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2024 Kaina Shaikh")
