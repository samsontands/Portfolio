import streamlit as st
import streamlit.components.v1 as components
import requests
import json

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

def chatbot_html():
    return """
    <style>
        #chatbot {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 300px;
            height: 400px;
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 10px;
            display: none;
            flex-direction: column;
            z-index: 1000;
        }
        #chatHeader {
            background-color: #f1f1f1;
            padding: 10px;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            cursor: pointer;
        }
        #chatMessages {
            flex-grow: 1;
            overflow-y: auto;
            padding: 10px;
        }
        #chatInput {
            padding: 10px;
            border-top: 1px solid #ddd;
        }
        #chatButton {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #4CAF50;
            color: white;
            padding: 15px;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            z-index: 1000;
        }
    </style>
    <div id="chatbot">
        <div id="chatHeader">Chat with AI</div>
        <div id="chatMessages"></div>
        <div id="chatInput">
            <input type="text" id="userInput" placeholder="Type your message...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>
    <button id="chatButton" onclick="toggleChat()">Chat</button>
    <script>
        function toggleChat() {
            var chatbot = document.getElementById('chatbot');
            var chatButton = document.getElementById('chatButton');
            if (chatbot.style.display === 'none' || chatbot.style.display === '') {
                chatbot.style.display = 'flex';
                chatButton.style.display = 'none';
            } else {
                chatbot.style.display = 'none';
                chatButton.style.display = 'block';
            }
        }
        
        function sendMessage() {
            var userInput = document.getElementById('userInput');
            var message = userInput.value;
            userInput.value = '';
            
            var chatMessages = document.getElementById('chatMessages');
            chatMessages.innerHTML += '<p><strong>You:</strong> ' + message + '</p>';
            
            // Send message to Streamlit
            parent.postMessage({type: 'chat_message', message: message}, '*');
        }
        
        function receiveMessage(message) {
            var chatMessages = document.getElementById('chatMessages');
            chatMessages.innerHTML += '<p><strong>AI:</strong> ' + message + '</p>';
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        // Listen for messages from Streamlit
        window.addEventListener('message', function(event) {
            if (event.data.type === 'chat_response') {
                receiveMessage(event.data.message);
            }
        });
    </script>
    """

def init_chatbot():
    components.html(chatbot_html(), height=0)
    
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []

def process_chat_message(personal_info):
    message = st.session_state.get('chat_input')
    if message:
        st.session_state.chat_messages.append(('user', message))
        response = get_groq_response(message, personal_info)
        st.session_state.chat_messages.append(('ai', response))
        
        # Send response back to the JavaScript component
        st.components.v1.html(f"""
        <script>
            window.parent.postMessage({{
                type: 'chat_response',
                message: {json.dumps(response)}
            }}, '*');
        </script>
        """, height=0)

def render_chat_messages():
    for role, message in st.session_state.chat_messages:
        if role == 'user':
            st.write(f"You: {message}")
        else:
            st.write(f"AI: {message}")
