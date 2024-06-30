import streamlit as st
from about_me import show_about_me, personal_info
from chatbot import init_chatbot, process_chat_message
# Import the data science tools page when it's ready
# from data_science_tools import show_data_science_tools

st.set_page_config(page_title="Samson Tan - Data Scientist", layout="wide")

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

    # Process chat messages
    process_chat_message(personal_info)

if __name__ == "__main__":
    main()
