import os
import openai
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI

load_dotenv()

openai_api_key = os.environ["OPENAI_API_KEY"]
llm = OpenAI(api_token=openai_api_key)

st.title("Your Data Analysis")

uploaded_csv_file = st.file_uploader("Upload a csv file for analysis", type=["csv"])

if uploaded_csv_file is not None:
    df = pd.read_csv(uploaded_csv_file)
    sdf = SmartDataframe(df, config={"llm": llm})
    st.write(sdf.head())

    prompt = st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating Response..."):
                response = sdf.chat(prompt)
                st.success(response)

            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
        else:
            st.warning("Please enter a prompt")
