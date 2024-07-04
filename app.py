import streamlit as st
import pandas as pd
import plotly.express as px
from about_me import show_about_me, personal_info
from chatbot import init_chatbot, process_chat_message
from eda_tool import show_eda_tool  # Import the EDA tool function

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

def show_data_visualization():
    st.title("Interactive Data Visualization")
    st.write("Upload a CSV file to explore and visualize your data interactively.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Data Preview:")
            st.dataframe(df.head())
            
            # Data summary
            st.subheader("Data Summary")
            st.write(df.describe())
            
            # Column selection for visualization
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
            categorical_columns = df.select_dtypes(include=['object', 'bool']).columns
            
            # Scatter plot
            if len(numeric_columns) >= 2:
                st.subheader("Scatter Plot")
                x_axis = st.selectbox("Choose x-axis", options=numeric_columns, key="scatter_x")
                y_axis = st.selectbox("Choose y-axis", options=numeric_columns, key="scatter_y")
                color_column = st.selectbox("Choose color (optional)", options=['None'] + list(categorical_columns), key="scatter_color")
                
                if color_column == 'None':
                    fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
                else:
                    fig = px.scatter(df, x=x_axis, y=y_axis, color=color_column, title=f"{y_axis} vs {x_axis}, colored by {color_column}")
                st.plotly_chart(fig)
            
            # Histogram
            st.subheader("Histogram")
            hist_column = st.selectbox("Choose column for histogram", options=numeric_columns, key="hist")
            fig = px.histogram(df, x=hist_column, title=f"Histogram of {hist_column}")
            st.plotly_chart(fig)
            
            # Bar chart for categorical data
            if len(categorical_columns) > 0:
                st.subheader("Bar Chart")
                cat_column = st.selectbox("Choose categorical column", options=categorical_columns, key="bar")
                fig = px.bar(df[cat_column].value_counts().reset_index(), x='index', y=cat_column, title=f"Bar Chart of {cat_column}")
                st.plotly_chart(fig)
            
            # Correlation heatmap
            if len(numeric_columns) > 1:
                st.subheader("Correlation Heatmap")
                corr = df[numeric_columns].corr()
                fig = px.imshow(corr, title="Correlation Heatmap")
                st.plotly_chart(fig)

        except pd.errors.EmptyDataError:
            st.error("The uploaded file is empty. Please upload a file with data.")
        except pd.errors.ParserError:
            st.error("Unable to parse the file. Please ensure it's a valid CSV file.")
        except Exception as e:
            st.error(f"An error occurred while processing the file: {str(e)}")
            st.write("If the issue persists, please try with a different CSV file.")

def main():
    # Initialize the chatbot
    init_chatbot()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["About Me", "Ask me anything", "Data Visualization", "EDA Tool"])

    if page == "About Me":
        show_about_me()
    elif page == "Ask me anything":
        show_ask_me_anything()
    elif page == "Data Visualization":
        show_data_visualization()
    elif page == "EDA Tool":
        show_eda_tool()

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
