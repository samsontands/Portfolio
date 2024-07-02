import streamlit as st
import requests
import json
from streamlit_timeline import timeline
import plotly.graph_objects as go
import pandas as pd

# Load configuration files
with open('timeline.json', 'r') as f:
    timeline_data = json.load(f)

with open('config/personal_info.txt', 'r') as f:
    personal_info = f.read()

with open('config/system_prompt.txt', 'r') as f:
    system_prompt = f.read()

with open('config/skills.json', 'r') as f:
    skills_data = json.load(f)

def get_groq_response(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": f"{system_prompt} {personal_info}"},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 100
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()['choices'][0]['message']['content']

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

    # Contact Information
    st.sidebar.header("Contact Information")
    st.sidebar.write("📞 +6011-1122 1128")
    st.sidebar.write("✉️ samsontands@gmail.com")
    st.sidebar.write("📍 Kuala Lumpur, Malaysia")
    st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/samsonthedatascientist/)")

    # Career Timeline
    st.subheader('Career snapshot')
    with st.spinner(text="Building timeline..."):
        timeline(timeline_data, height=400)

    # Skills & Tools
    st.subheader('Skills & Tools ⚒️')
    create_skill_buttons(skills_data['skills'])

    # Experience
    st.header("Work Experience")

    st.subheader("Alliance Bank Malaysia Berhad")
    st.write("**Data Scientist | June, 2022 - Present**")
    st.write("""
    - Spearheaded on-premise deployment of AI-powered chatbot for housing discount checks
    - Leveraged AI computer vision techniques to extract data from unstructured sources
    - Developed user-friendly Python applications for cross-departmental PDF customization
    - Conducted training on Tableau and Python for various teams
    """)

    st.subheader("GoGet.my")
    st.write("**Data Scientist | May, 2021 - June, 2022**")
    st.write("""
    - Built rider-job-claiming machine learning model improving timeliness
    - Set up and managed Amazon Quicksight visualization dashboard
    - Utilized ARIMA models for forecasting peak season rider demand
    """)

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

    # LLM Models
    st.subheader("LLM Models")
    st.write("""
    **Local Offline:**
    Mistral, Mixtral, Meta Llama2, Microsoft Phi2, Google Gemma

    **Cloud API:**
    OpenAI ChatGPT, GPT-4, GPT-vision, GPT-3.5, GPT-2, GROQ API
    """)

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
