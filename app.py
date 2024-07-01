import streamlit as st
from about_me import show_about_me, personal_info
from chatbot import init_chatbot, process_chat_message

try:
    from pandasai_analysis import show_pandasai_analysis
    pandasai_available = True
except ImportError as e:
    st.error(f"Error importing PandasAI analysis module: {e}")
    pandasai_available = False

st.set_page_config(page_title="Samson Tan - Data Scientist", layout="wide")

# ... (rest of your app.py code)

def main():
    # ... (your existing main function code)

    st.sidebar.title("Navigation")
    pages = ["About Me", "Ask me anything"]
    if pandasai_available:
        pages.append("Data Analysis")
    page = st.sidebar.radio("Go to", pages)

    if page == "About Me":
        show_about_me()
    elif page == "Ask me anything":
        show_ask_me_anything()
    elif page == "Data Analysis" and pandasai_available:
        show_pandasai_analysis()

    # ... (rest of your main function)

if __name__ == "__main__":
    main()
    
