import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import os

def show_eda_tool():
    st.title('Data Profiling with YData Profiling')
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        with st.spinner('Reading CSV file...'):
            df = pd.read_csv(uploaded_file)
            st.write(df)
            
        with st.spinner('Generating profiling report...'):
            profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
            
            # Save the report to an HTML file
            report_path = "profiling_report.html"
            profile.to_file(report_path)
            
        st.success('Report generated successfully!')

        # Provide a link to open the report in a new tab
        st.markdown(f'<a href="file://{os.path.abspath(report_path)}" target="_blank">Click here to view the full report</a>', unsafe_allow_html=True)

        # Provide a download button for the HTML file
        with open(report_path, "rb") as file:
            btn = st.download_button(
                label="Download Profiling Report",
                data=file,
                file_name="profiling_report.html",
                mime="text/html"
            )
