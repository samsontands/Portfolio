import streamlit as st
import pandas as pd
import pygwalker as pyg
from about_me import show_about_me, personal_info
from chatbot import init_chatbot, process_chat_message

# Set page configuration
st.set_page_config(page_title="Samson Tan - Data Scientist", layout="wide")

# Function to handle suggested questions
def handle_suggested_question(question):
    st.session_state.user_question = question
    st.session_state.run_query = True

# Function to display suggested questions
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

# Function to show "Ask me anything" page
def show_ask_me_anything():
    st.title("Ask me anything about Samson")
    st.write("Feel free to ask any questions about Samson's background, skills, or experience.")

# Function to show data visualization page
def show_data_visualization():
    st.title("Interactive Data Visualization with PyGWalker")
    st.write("Upload a CSV file to explore and visualize your data interactively.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file, encoding='utf-8')  # Ensure UTF-8 encoding
            st.write("Data Preview:")
            st.dataframe(df.head())
            
            # Use PyGWalker for visualization
            pyg.walk(df, env='Streamlit')
        except pd.errors.EmptyDataError:
            st.error("The uploaded file is empty. Please upload a file with data.")
        except pd.errors.ParserError:
            st.error("Unable to parse the file. Please ensure it's a valid CSV file.")
        except Exception as e:
            st.error(f"An error occurred while processing the file: {str(e)}")
            st.write("If the issue persists, please try with a different CSV file.")
    else:
        st.write("Upload a CSV file to visualize it with PyGWalker.")

# Main function to control the app flow
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
            question_to_process = user_input if user_input else st.session_state.user_question
            if question_to_process:
                process_chat_message(personal_info, question_to_process)
                st.session_state.user_question = ""  # Clear the stored question
                st.session_state.run_query = False  # Reset the run flag

        # Clear the input field after processing
        if st.session_state.run_query:
            st.session_state.user_question = ""
            st.experimental_rerun()

# Entry point of the script
if __name__ == "__main__":
    main()
