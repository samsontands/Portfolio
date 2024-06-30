import streamlit as st
import requests
import json
from streamlit_timeline import timeline
import plotly.graph_objects as go
import pandas as pd

# Load timeline data from JSON file
with open('timeline.json', 'r') as f:
    timeline_data = json.load(f)

# Your personal information as a string (keep this for the chatbot context)
personal_info = """
Samson Tan Jia Sheng is a skilled Data Scientist with expertise in Large Language Models (LLM) and the latest AI/ML advancements. 
...
"""

def get_groq_response(prompt):
    # ... (keep the existing get_groq_response function)

def create_skill_buttons(skills):
    cols = st.columns(4)  # Adjust the number of columns as needed
    for i, skill in enumerate(skills):
        cols[i % 4].button(skill)

def show_about_me():
    st.title("Samson Tan Jia Sheng")
    st.subheader("Data Scientist")

    # About Me
    st.header("About Me")
    st.write("""
    Skilled Data Scientist with expertise in Large Language Models (LLM) and the latest AI/ML advancements. 
    Exceptional at applying current technologies for impactful solutions and staying agile in a rapidly evolving field.
    """)

    # Career Timeline
    st.subheader('Career snapshot')
    with st.spinner(text="Building timeline..."):
        timeline(timeline_data, height=400)

    # Skills & Tools
    st.subheader('Skills & Tools ⚒️')
    skills = [
        "LLM fine-tuning", "RAG", "Machine Learning", "NLP", "Computer Vision", 
        "API integrations", "BERT embeddings", "Python", "R", "SQL", "PostgreSQL",
        "VScode", "Anaconda", "RStudio", "Google Colab", "PyTorch"
    ]
    create_skill_buttons(skills)

    # Experience
    st.header("Work Experience")
    # ... (keep your existing work experience content)

    # Education
    st.subheader('Education 📖')
    education_data = pd.DataFrame({
        'Degree': ['Masters in Data Science and Business Analytics (Data Engineering)', 
                   'Bachelor of Psychology and Business (Psychology and Econometrics)'],
        'Institution': ['Asia Pacific University of Technology and Innovation', 'Monash University'],
        'Year': ['2020-2022', '2016-2020']
    })

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(education_data.columns),
                    fill_color='paleturquoise',
                    align='left', height=65, font_size=20),
        cells=dict(values=education_data.transpose().values.tolist(),
                   fill_color='lavender',
                   align='left', height=40, font_size=15))])

    fig.update_layout(width=750, height=200)
    st.plotly_chart(fig)

    # Chatbot
    st.header("Quick Q&A about Samson")
    st.write("Ask a question to get a brief response about Samson's background, skills, or experience.")
    user_question = st.text_input("What would you like to know?")
    if user_question:
        with st.spinner('Getting a quick answer...'):
            response = get_groq_response(user_question)
        st.write(response)
    st.caption("Note: Responses are kept brief. For more detailed information, please refer to the sections above.")

# Make sure to export personal_info for use in other parts of your app
personal_info = personal_info
