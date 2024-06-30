import streamlit as st
from about_me import show_about_me, personal_info
from chatbot import init_chatbot, process_chat_message
# Import the data science tools page when it's ready
# from data_science_tools import show_data_science_tools

st.set_page_config(page_title="Samson Tan - Data Scientist", layout="wide")

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
        if st.sidebar.button(question):
            st.session_state.user_question = question
            st.experimental_rerun()

def main():
    # Initialize the chatbot
    init_chatbot()

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

    # Display suggested questions
    display_suggested_questions()

    # Single chat input and processing
    if 'user_question' not in st.session_state:
        st.session_state.user_question = ""

    user_question = st.text_input("Ask me anything about Samson:", key="chat_input")
    
    if user_question:
        process_chat_message(personal_info, user_question)
        st.session_state.user_question = ""  # Clear the input after processing

if __name__ == "__main__":
    main()
