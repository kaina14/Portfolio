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

def get_resume_file():
    with open("Kaina Shaikh Resume.pdf", "rb") as file:
        return file.read()

# Lottie animation URLs
lottie_intro_url = "https://lottie.host/d9dd3f3d-d3df-438d-86f3-9d96f461cb90/HWLDLKChZU.json"  # Replace with your own URL
lottie_skills_url = "https://lottie.host/d1bba083-819f-4115-aff9-31cc5177fbf4/I30jy7hZt9.json" 
lottie_research_url = "https://lottie.host/6bc47916-7cf5-4afc-9228-925da0eec293/lZHWDvD03L.json"
# Load Lottie animations
lottie_intro = load_lottie_url(lottie_intro_url)
lottie_skills = load_lottie_url(lottie_skills_url)
lottie_research= load_lottie_url(lottie_research_url)

# Set page configuration
st.set_page_config(page_title="Kaina Shaikh - Portfolio", page_icon=":star:", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Merriweather', sans-serif;
            color: #E5E5E5;
            background-color: #1E1E1E;
        }
        
        .sidebar .sidebar-content {
            background-color: #2A2B2E;
            padding: 20px;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF;
            font-weight: 530;
        }
        
        .stMarkdown {
            color: #E5E5E5;
        }

        .nav-item {
            font-size: 0.5rem;
            color: #4A90E2;
            margin: 5px 0;
            position: relative; /* Ensure that the pseudo-element is positioned relative to the item */
    padding-left: 20px; /* Add padding to make space for the bullet */
        }
        
        .nav-item::before {
    content: '•'; /* Bullet character */
    position: absolute;
    left: 0; /* Position the bullet at the start of the item */
    color: #E5E5E5; /* Bullet color */
}
        .nav-item a {
            text-decoration: none;
            color: #4A90E2;
        }
        
        .nav-item a:hover {
            color: #E5E5E5;
        }
        .section-title {
            font-size: 2rem;
            margin-bottom: 0.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2.5px solid;
            border-image: linear-gradient(to right, 
    rgba(255, 0, 0, 0.8), /* Red with slight opacity */
    rgba(255, 127, 0, 0.8), /* Orange with slight opacity */
    rgba(255, 255, 0, 0.8), /* Yellow with slight opacity */
    rgba(0, 255, 0, 0.8), /* Green with slight opacity */
    rgba(0, 0, 255, 0.8), /* Blue with slight opacity */
    rgba(75, 0, 130, 0.8), /* Indigo with slight opacity */
    rgba(139, 0, 255, 0.8)  /* Violet with slight opacity */
) 1;
            display: inline-block;
            width: 100%;
            box-sizing: border-box;
        }
        
        .section-content {
            max-width: 800px
            margin-top: 20px;
        }
           
        .content-area {
            max-width: 400px;
            margin: auto;
        }
        .anchor {
            display: block;
            position: relative;
            top: -100px;
            visibility: hidden;
        }
        .social-icon {
            width: 50px;
            height: 50px;
            margin-top: 15px;
            margin: 15px 15px;
        }
        
    </style>
    """, unsafe_allow_html=True)


# Sidebar navigation
with st.sidebar:
    st.markdown("<h2 class='section-title'>🌱 Kaina Shaikh </h2>", unsafe_allow_html=True)
    st.markdown("<h3 class='nav-item'><a href='#introduction'>Introduction</a></h3>", unsafe_allow_html=True)
    st.markdown("<h3 class='nav-item'><a href='#skills'>Skills</a></h3>", unsafe_allow_html=True)
    st.markdown("<h3 class='nav-item'><a href='#experience'>Experience</a></h3>", unsafe_allow_html=True)
    st.markdown("<h3 class='nav-item'><a href='#projects'>Projects</a></h3>", unsafe_allow_html=True)
    st.markdown("<h3 class='nav-item'><a href='#research'>Research Works And Publications</a></h3>", unsafe_allow_html=True)
    st.markdown("<h3 class='nav-item'><a href='#achievements'>Achievements</a></h3>", unsafe_allow_html=True)
    st.markdown("<h3 class='nav-item'><a href='#contact'>Contact Information</a></h3>", unsafe_allow_html=True)
    #st.markdown("<h3 class='nav-item'><a href='#get_in_touch'>Get In Touch With Me!</a></h3>", unsafe_allow_html=True)

# Main content
#st.markdown("<div class='content-area'>", unsafe_allow_html=True)


# Introduction Section
st.markdown("<a id='introduction' class='anchor'></a><h2 class='section-title'>📌 Introduction</h2>", unsafe_allow_html=True)

# Use st.columns() to place the text and Lottie animation side by side
with st.container():
    #st.write("---")
    left_column, right_column = st.columns([2, 2])  # Adjust column widths as needed
    with left_column:
        st.markdown("<h6>Hello,</h6>", unsafe_allow_html=True)
        st.markdown("<h2 style='font-size: 2.5rem;'>I'm Kaina Shaikh!</h2>", unsafe_allow_html=True)
        st.markdown("<h6>Artificial Intelligence & Data Science'24</h6>", unsafe_allow_html=True)
        st.write(
            """
            I am a dedicated and ambitious data scientist with a passion for Artificial Intelligence (AI)
            and Machine Learning (ML). My expertise in AI, ML, and Data Science fuels my ambition to contribute to impactful projects 
            and advance the field through both research and development.
            """
        )
    with right_column:
        if lottie_intro:
            st_lottie(lottie_intro,width=535, key="intro_animation")

#st.button("Download Resume")
st.download_button(
    label="Download Resume",
    data=get_resume_file(),
    file_name="Kaina Shaikh Resume.pdf",
    mime="application/pdf"
)
#st.markdown("<hr style='border-top: 3px solid #565BF7;'>", unsafe_allow_html=True)
#st.write("Wants to Know More About Me?")
#st.text_input("Ask Anything About Me !!", "")


# Skills Section
st.markdown("<a id='skills' class='anchor'></a><h2 class='section-title'>🎗️Skills</h2>", unsafe_allow_html=True)

# Use st.columns() to place the text and Lottie animation side by side
with st.container():
    #st.write("---")
    left_column, right_column = st.columns([2, 2])  # Adjust column widths as needed
    with left_column:
        #st.write("##")
        st.write(
    """
    - <strong>Programming Languages :</strong><br>
      C++, Python, SQL<br>
      <br>
    - <strong>Tools & Libraries :</strong><br>
      Git, Numpy, Matplotlib, Sklearn, Pandas, Tensorflow, Pytorch, OpenCV, Streamlit<br>
      <br>
    - <strong>Visualization :</strong><br>
      PowerBI, Tableau<br>
      <br>
    - <strong>Technologies :</strong><br>
      Data Science, Artificial Intelligence, Machine Learning, Deep Learning, Quantum AI
    """,
    unsafe_allow_html=True
) 
    with right_column:
        if lottie_skills:
            st_lottie(lottie_skills, width=300, key="skills_animation")

# Experience Section
st.markdown("<a id='experience' class='anchor'></a><h2 class='section-title'>💻 Experience</h2>", unsafe_allow_html=True)

# Use st.columns() to create a layout for each job experience
with st.container():
    st.write("---")
    col1, col2 = st.columns([2.5, 0.5])  # Adjust column widths as needed

    with col1:
        st.write("##### Research Intern - Applied AI and Machine Learning ")
        st.write("**Defence Research and Development Organization (DRDO)**")
        st.markdown(
            """
            <div style="display: flex; justify-content: space-between;">
                <div>📍Pune</div>
                <div>📆7/23 - 12/23</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write(
            """
              - Led the team by working on the Defect Detection system using Deep Learning, improved the accuracy of the model to 98%.
              - Fine-tuned the YOLOv8 algorithm by implementing it by scratch and on grayscale images.
              - Compared with existing algorithms and increased accuracy in the new approach by 11%
            """
        )

    with col2:
        # Add a placeholder image or any other relevant content here if desired
        st.image("https://upload.wikimedia.org/wikipedia/mai/3/3e/DRDO-logo.png", caption="DRDO", width=100)

    st.write("---")

    col1, col2 = st.columns([2.5, 0.5])  # Repeat columns for additional experience

    with col1:
        st.write("##### Machine Learning Apprenticeship ")
        st.write("**Amazon**")
        st.markdown(
            """
            <div style="display: flex; justify-content: space-between;">
                <div>📍Remote</div>
                <div>📆7/22 - 8/22</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write(
            """
              - Implementation of core Machine Learning concepts Reinforcement Learning, Recommendation Systems, Causal Inference,
Probabilistic Graphical Models, Supervised Learning, Deep Learning, Dimensionality Reduction, Unsupervised Learning.
            """
        )

    with col2:
        # Add a placeholder image or any other relevant content here if desired
        st.image("https://cdn.vectorstock.com/i/500p/39/87/astana-kazakhstan-20-july-2020-amazon-icon-vector-34243987.jpg", caption="Amazon", width=100)

    st.write("---")
    col1, col2 = st.columns([2.5, 0.5])  # Repeat columns for additional experience

    with col1:
        st.write("##### Microsoft ENGAGE Intern ")
        st.write("**Microsoft**")
        st.markdown(
            """
            <div style="display: flex; justify-content: space-between;">
                <div>📍Remote</div>
                <div>📆5/22 - 7/22</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write(
            """
              -  Implemented Face Recognition App that works on various applications such as Smart Attendance System, Face Emotion
                recognition and Twitter-posts security feature.
              -  Focused mainly on building applications using pre-existing face recognition API by Microsoft Cognitive Services.
              -  Designed and developed android application integrating all the features using Microsoft Xamarin Forms.
            """
        )

    with col2:
        # Add a placeholder image or any other relevant content here if desired
        st.image("https://static-00.iconduck.com/assets.00/microsoft-icon-1024x1024-5w26drb6.png", caption="Microsoft", width=100)


    # Add more experiences as needed


# Projects Section
st.markdown("<a id='projects' class='anchor'></a><h2 class='section-title'>🚀 Projects</h2>", unsafe_allow_html=True)
st.write("---")

# Set up the grid layout for the projects (3 columns by 2 rows) with adjusted image width and spacing
col1, col2, col3 = st.columns([1, 1, 1])  # Equal column widths with some padding

# Project 1
with col1:
    st.image("cyclone.jpg", width=220, caption="Cyclone Intensity Estimation")
    st.markdown("""
    Developed Quantum Machine Learning Algorithm with accuracy of **93%** showing quantum advantage over classical CNN model for cyclone estimation. Deployed web app using Streamlit
    """)

# Project 2
with col2:
    st.image("proj2.png", width=220, caption="Satellite Image Segmentation")
    st.markdown("""
    Used SegNet Architecture with deptwise convolution to segement the satellite images and achieved dice loss of 0.24 for predicted images
    """)

# Project 3
with col3:
    st.image("proj3.png", width=220, caption="Crop Recommendation System")
    st.markdown("""
   Compared to multiple ML algorithms, Random
Forest and Naive Bayes achieved 99% percent accuracy which is 15% more than other Machine Learning algorithms.
    """)

# Move to the next row of the grid
col1, col2, col3 = st.columns([1, 1, 1])  # Equal column widths with some padding

# Project 4
with col1:
    st.image("proj4.png", width=220, caption="Superstore Sales Analysis")
    st.markdown("""
    Designed dashboard using PowerBI, identified important Key Factor Indicators (KPI’s) for sales
forecasting time series analysis of next 15 days, trend analysis wrt to location, profit by month and year.
    """)

# Example Project 5
with col2:
    st.image("https://analyticstraininghub.com/wp-content/uploads/2020/10/icon-tableau.png", width=220, caption="House Sales Dashboard - Tableau")
    st.markdown("""
    Designed dashboard using Tableau, advanced visualizations using Maps, conditional heatmap for ratings of house prices, analysis of daily average house sales prices.
    """)

# Example Project 6
with col3:
    st.image("respiratory-disease.png", width=220, caption="Chronic Disease Prediction")
    st.markdown("""
    Performed EDA, Implemented Graph Neural Network for classification and compared with
existing ML algorithms like RF, DT, Gradient Boosting, SVM. GNN achieved accuracy of **98%** similar to Gradient Boosting.
    """)



# Research Works and Publications Section
st.markdown("<a id='research' class='anchor'></a><h2 class='section-title'>🏷️ Research Works and Publications</h2>", unsafe_allow_html=True)
#st.write("Details about your research works and publications will go here.")
with st.container():
    st.write("---")
    left_column, right_column = st.columns([2, 2])  # Adjust column widths as needed
    with left_column:
        st.write(
            """
            - **Deep Learning based Defect Detection and Segmentation for High Energy Material Applications**  
               (Published under the guidance of Indian Scientists at DRDO)
            - **[Benchmarking Traditional and Graph Neural Network Models for Node Classification in Literature Characters](https://www.irjet.net/archives/V11/i6/IRJET-V11I6183.pdf)**
            """
        )
    with right_column:
        if lottie_intro:
            st_lottie(lottie_research, height=200, key="research_animation")


# Achievements Section
st.markdown("<a id='achievements' class='anchor'></a><h2 class='section-title'>🎗️ Achievements</h2>", unsafe_allow_html=True)
st.write('---')
st.write(
    """
    - **Harvard WECode Scholar:** Received Harvard Women Engineers Scholarship, Women in Technology Conference, Jan 2023.

    - **Google Women In Cloud Summit:** Host-participant member, Cloud Summit, Google's Women Techmakers Community.

    - **HEMCE Conference:** Poster representation of my research work at HEMCE conference, organized by ISRO and DRDO.

    - **Machine Learning Hackathon:** Successfully completed ML Hackathon by Leaps Analytica, Sept 2021.

    - **Python Programming IIT Kharagpur:** Among top **10%** from India to be selected for Python Event-All Youth Symposium.

    - **Qubit x Qubit by Microsoft:** Successfully completed the International Program for Quantum Machine Learning, Feb 2023.
"""
)


# Contact Information Section
st.markdown("<a id='contact' class='anchor'></a><h2 class='section-title'>📧 Let's Connect !!</h2>", unsafe_allow_html=True)
st.write("Feel free to reach out to me via email or connect with me on LinkedIn.")
# Social Icons
social_icons_data = {
    # Platform: [URL, Icon]
    "LinkedIn": ["https://www.linkedin.com/in/kaina-s-351101225/", "https://cdn-icons-png.flaticon.com/512/3938/3938061.png"],
    "GitHub": ["https://github.com/kaina14", "https://cdn-icons-png.flaticon.com/512/2504/2504911.png"],
    "Mail": ["kainashaikh@gmail.com", "https://cdn-icons-png.flaticon.com/512/2965/2965306.png"]
}

social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

st.write(f"""
<div style="display: flex; justify-content: center; margin-bottom: 20px;">
    {''.join(social_icons_html)}
</div>""", 
unsafe_allow_html=True)


# Get In Touch Section
#st.markdown("<a id='get-in-touch' class='anchor'></a><h2 class='section-title'>Get In Touch</h2>", unsafe_allow_html=True)
#st.write("Please fill out the form below to get in touch with me.")
#st.text_input("Your Name", "")
#st.text_input("Your Email", "")
#st.text_area("Your Message", "")
#st.button("Send Message")

# Footer
st.markdown("""
<footer>
    <p>© 2024 Kaina Shaikh</p>
</footer>
""", unsafe_allow_html=True)
