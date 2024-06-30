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

def show_about_me():
    st.title("Samson Tan Jia Sheng")
    st.subheader("Data Scientist")

    # About Me
    st.header("About Me")
    st.write("""
    Skilled Data Scientist with expertise in Large Language Models (LLM) and the latest AI/ML advancements. 
    Exceptional at applying current technologies for impactful solutions and staying agile in a rapidly evolving field.
    """)

    # Work Experience Timeline
    st.header("Work Experience Timeline")
    items = [
        {"id": 1, "content": "Alliance Bank Malaysia Berhad", "start": "2022-06-01", "end": "2024-06-30", "group": "Work"},
        {"id": 2, "content": "GoGet.my", "start": "2021-05-01", "end": "2022-05-31", "group": "Work"},
        {"id": 3, "content": "Masters in Data Science", "start": "2020-09-01", "end": "2022-05-31", "group": "Education"},
        {"id": 4, "content": "Bachelor's Degree", "start": "2016-09-01", "end": "2020-05-31", "group": "Education"}
    ]
    
    groups = [
        {"id": "Work", "content": "Work Experience"},
        {"id": "Education", "content": "Education"}
    ]
    
    options = {
        "stack": True,
        "showMajorLabels": True,
        "showCurrentTime": False,
        "zoomable": False,
        "height": "300px",
        "start": "2016-01-01",
        "end": "2024-12-31"
    }
    
    timeline = st_timeline(items, groups=groups, options=options)
    
    if timeline:
        st.write(f"You selected: {timeline}")

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
