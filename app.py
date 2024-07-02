import streamlit as st
import pandas as pd
import plotly.express as px
from about_me import show_about_me, personal_info
from chatbot import init_chatbot, process_chat_message

st.set_page_config(page_title="Samson Tan - Data Scientist", layout="wide")

def handle_suggested_question(question):
    st.session_state.user_question = question
    st.session_state.run_query = True

def display_suggested_questions():
    st.sidebar.header("Suggested Questions")
    questions = [
        "What is Samson's current job?",
        "What are Samson's key skills?",
        "Where did Samson study?",
        "What projects has Samson worked on?",
        "What is Samson's experience with LLMs?"
    ]
    for question in questions:
        st.sidebar.button(question, on_click=handle_suggested_question, args=(question,))

def show_ask_me_anything():
    st.title("Ask me anything about Samson")
    st.write("Feel free to ask any questions about Samson's background, skills, or experience.")

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

    # Work Experience
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

    # Education (simplified to normal text)
    st.header("Education")
    st.write("""
    • Masters in Data Science and Business Analytics (Data Engineering)
      Asia Pacific University of Technology and Innovation, 2020-2022

    • Bachelor of Psychology and Business (Psychology and Econometrics)
      Monash University, 2016-2020
    """)

def show_data_visualization():
    # ... (keep the existing show_data_visualization function as is)

def main():
    # Initialize the chatbot
    init_chatbot()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["About Me", "Ask me anything", "Data Visualization"])

    if page == "About Me":
        show_about_me()
    elif page == "Ask me anything":
        show_ask_me_anything()
    elif page == "Data Visualization":
        show_data_visualization()

    # Display suggested questions (only for "Ask me anything" page)
    if page == "Ask me anything":
        display_suggested_questions()

        # Initialize session states
        if 'user_question' not in st.session_state:
            st.session_state.user_question = ""
        if 'run_query' not in st.session_state:
            st.session_state.run_query = False

        # Single chat input
        user_input = st.text_input("Ask me anything about Samson:", key="chat_input", value=st.session_state.user_question)
        
        # Process the question if it's entered manually or suggested
        if user_input or st.session_state.run_query:
            if user_input:
                question_to_process = user_input
            else:
                question_to_process = st.session_state.user_question
            
            if question_to_process:
                process_chat_message(personal_info, question_to_process)
                st.session_state.user_question = ""  # Clear the stored question
                st.session_state.run_query = False  # Reset the run flag

        # Clear the input field after processing
        if st.session_state.run_query:
            st.session_state.user_question = ""
            st.experimental_rerun()

if __name__ == "__main__":
    main()
