import streamlit as st
import pandas as pd
import pygwalker as pyg

def show_pygwalker():
    st.title("PyGWalker Visualization")
    st.write("Upload a CSV file to explore and visualize your data interactively with PyGWalker.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
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
            st.write("If the issue persists, please try with a different CSV file or check if PyGWalker is properly installed.")
    else:
        st.write("Upload a CSV file to visualize it with PyGWalker.")
