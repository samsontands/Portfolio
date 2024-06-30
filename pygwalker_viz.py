import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def show_data_viz():
    st.title("Data Profiling with ydata-profiling")
    st.write("Upload a CSV file to generate a comprehensive data profile report.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Data Preview:")
            st.dataframe(df.head())
            
            st.write("Generating profile report... This may take a moment.")
            profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
            
            st_profile_report(profile)
            
        except pd.errors.EmptyDataError:
            st.error("The uploaded file is empty. Please upload a file with data.")
        except pd.errors.ParserError:
            st.error("Unable to parse the file. Please ensure it's a valid CSV file.")
        except Exception as e:
            st.error(f"An error occurred while processing the file: {str(e)}")
            st.write("If the issue persists, please try with a different CSV file.")
    else:
        st.write("Upload a CSV file to generate a profile report.")
