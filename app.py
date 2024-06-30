# File: app.py (Main app file)

import streamlit as st
from about_me import show_about_me
# Import the data science tools page when it's ready
# from data_science_tools import show_data_science_tools

st.set_page_config(page_title="Samson Tan - Data Scientist", layout="wide")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["About Me", "Data Science Tools"])

    if page == "About Me":
        show_about_me()
    elif page == "Data Science Tools":
        # Placeholder for the data science tools page
        st.title("Data Science Tools")
        st.write("This page will contain various data science tools.")
        # Uncomment the line below when the data_science_tools.py file is ready
        # show_data_science_tools()

if __name__ == "__main__":
    main()

# File: about_me.py

import streamlit as st
import requests
import json

# Your personal information as a string (this will be used as context for the AI)
personal_info = """
Samson Tan Jia Sheng is a skilled Data Scientist with expertise in Large Language Models (LLM) and the latest AI/ML advancements. 
He is currently working at Alliance Bank Malaysia Berhad as a Data Scientist since June 2022. 
His key achievements include:
- Spearheaded on-premise deployment of AI-powered chatbot for housing discount checks
- Leveraged AI computer vision techniques to extract data from unstructured sources
- Developed user-friendly Python applications for cross-departmental PDF customization
- Conducted training on Tableau and Python for various teams

Previously, he worked at GoGet.my as a Data Scientist from May 2021 to June 2022, where he:
- Built rider-job-claiming machine learning model improving timeliness
- Set up and managed Amazon Quicksight visualization dashboard
- Utilized ARIMA models for forecasting peak season rider demand

Samson has a Masters in Data Science and Business Analytics (Data Engineering) from Asia Pacific University of Technology and Innovation,
and a Bachelor of Psychology and Business (Psychology and Econometrics) from Monash University.

His skills include:
- AI Skills: LLM fine-tuning, Retrieval Augmented Generation (RAG), Machine Learning, Natural Language Processing (NLP), Computer Vision, API integrations and BERT embeddings
- Languages and Databases: Python, R, SQL, PostgreSQL
- Frameworks and Tools: RAG, VScode, Anaconda, RStudio, Google Colab, LM Studio, Ollama, Jan, MLX, CUDA, PyTorch
- LLM Models: Mistral, Mixtral, Meta Llama2, Microsoft Phi2, Google Gemma (Local Offline), OpenAI ChatGPT, GPT-4, GPT-vision, GPT-3.5, GPT-2, GROQ API (Cloud API)

Samson is based in Kuala Lumpur, Malaysia and can be contacted at +6011-1122 1128 or samsontands@gmail.com.
His LinkedIn profile is https://www.linkedin.com/in/samsonthedatascientist/
"""

def get_groq_response(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": f"You are an AI assistant that answers questions about Samson Tan based on the following information: {personal_info} Your responses should be short, concise, and to the point, typically no more than 2-3 sentences."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 100
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()['choices'][0]['message']['content']

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

    # Skills
    st.header("Skills")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("AI Skills")
        st.write("""
        - LLM fine-tuning
        - Retrieval Augmented Generation (RAG)
        - Machine Learning
        - Natural Language Processing (NLP)
        - Computer Vision
        - API integrations and BERT embeddings
        """)

    with col2:
        st.subheader("Languages and Databases")
        st.write("Python, R, SQL, PostgreSQL")

        st.subheader("Frameworks and Tools")
        st.write("""
        RAG, VScode, Anaconda, RStudio, Google Colab, 
        LM Studio, Ollama, Jan, MLX, CUDA, PyTorch
        """)

    with col3:
        st.subheader("LLM Models")
        st.write("""
        **Local Offline:**
        Mistral, Mixtral, Meta Llama2, Microsoft Phi2, Google Gemma

        **Cloud API:**
        OpenAI ChatGPT, GPT-4, GPT-vision, GPT-3.5, GPT-2, GROQ API
        """)

    # Education
    st.header("Education")
    st.write("""
    - **Masters in Data Science and Business Analytics (Data Engineering)**
      Asia Pacific University of Technology and Innovation

    - **Bachelor of Psychology and Business (Psychology and Econometrics)**
      Monash University
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
