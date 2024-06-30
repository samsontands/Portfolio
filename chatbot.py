import streamlit as st
import requests
import json

def init_chatbot():
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []

def process_chat_message(personal_info, user_question):
    if user_question:
        st.session_state.chat_messages.append(('user', user_question))
        response = get_groq_response(user_question, personal_info)
        st.session_state.chat_messages.append(('ai', response))
        
        for role, message in st.session_state.chat_messages:
            if role == 'user':
                st.write(f"You: {message}")
            else:
                st.write(f"AI: {message}")


def get_groq_response(prompt, personal_info):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": f"You are an AI assistant that answers questions about Samson Tan based on the following information: {personal_info} Your responses should be short, concise, and to the point, typically no more than 2-3 sentences."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 100
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()['choices'][0]['message']['content']
