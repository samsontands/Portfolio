import streamlit as st
import pandas as pd
import sys

try:
    from pandasai import PandasAI
    from pandasai.llm.openai import OpenAI
    import pandasai
    st.write(f"PandasAI version: {pandasai.__version__}")
except ImportError as e:
    st.error(f"Error importing PandasAI: {e}")
    st.write(f"Python version: {sys.version}")
    st.write(f"Pandas version: {pd.__version__}")
    st.write("Please check your installation and try again.")

def show_pandasai_analysis():
    st.title("Data Analysis with PandasAI")
    st.write("Upload a CSV file and ask questions about your data.")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        # Display the first few rows of the dataframe
        st.write("Data Preview:")
        st.dataframe(df.head())

        try:
            # Initialize PandasAI
            llm = OpenAI(api_token=st.secrets["OPENAI_API_KEY"])
            pandas_ai = PandasAI(llm)

            # User input for questions
            user_question = st.text_input("Ask a question about your data:")
            
            if user_question:
                with st.spinner("Analyzing..."):
                    try:
                        result = pandas_ai.run(df, prompt=user_question)
                        st.write("Answer:")
                        st.write(result)
                    except Exception as e:
                        st.error(f"An error occurred while processing the question: {str(e)}")

            # Display dataframe info
            st.subheader("Dataset Information")
            st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
            st.write("Columns:", ", ".join(df.columns))

            # Display basic statistics
            st.subheader("Basic Statistics")
            st.write(df.describe())
        except Exception as e:
            st.error(f"An error occurred while initializing PandasAI: {str(e)}")
