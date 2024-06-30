import streamlit as st
from about_me import show_about_me, personal_info
from chatbot import init_chatbot, process_chat_message
from gtts import gTTS
import os
import base64

st.set_page_config(page_title="Samson Tan - Data Scientist", layout="wide")

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    with open("response.mp3", "rb") as f:
        audio_bytes = f.read()
    os.remove("response.mp3")  # Clean up the file
    return audio_bytes

def get_audio_player(audio_bytes):
    audio_base64 = base64.b64encode(audio_bytes).decode()
    return f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_base64}">'

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

def main():
    init_chatbot()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["About Me", "Ask me anything"])

    if page == "About Me":
        show_about_me()
    elif page == "Ask me anything":
        show_ask_me_anything()

    display_suggested_questions()

    if 'user_question' not in st.session_state:
        st.session_state.user_question = ""
    if 'run_query' not in st.session_state:
        st.session_state.run_query = False

    user_input = st.text_input("Ask me anything about Samson:", key="chat_input", value=st.session_state.user_question)
    
    if user_input or st.session_state.run_query:
        if user_input:
            question_to_process = user_input
        else:
            question_to_process = st.session_state.user_question
        
        if question_to_process:
            response = process_chat_message(personal_info, question_to_process)
            st.write("AI:", response)
            
            # Generate and play audio
            audio_bytes = text_to_speech(response)
            st.audio(audio_bytes, format='audio/mp3')
            
            st.session_state.user_question = ""
            st.session_state.run_query = False

    if st.session_state.run_query:
        st.session_state.user_question = ""
        st.experimental_rerun()

if __name__ == "__main__":
    main()
