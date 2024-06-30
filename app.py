import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Samson Tan - Data Scientist", layout="wide")

    # Header
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

    # Projects (placeholder)
    st.header("Projects")
    st.write("Here you can add some of your notable projects with descriptions and links.")

if __name__ == "__main__":
    main()
