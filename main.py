from dotenv import load_dotenv
load_dotenv('../config/.env')

import os
import streamlit as st
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(
    page_title= "GPT-4o Chatbot",
    page_icon="🤖",
    layout="centered"
)

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
    
st.title("🤖 GPT-4o Chatbot")

for message in st.session_state["chat_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    
user_prompt = st.chat_input("Ask GPT-4o a question:")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state["chat_history"].append({"role": "user", "content": user_prompt})
    
    response = openai.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            *st.session_state["chat_history"],
        ]
    )
    
    assitant_response = response.choices[0].message["content"]
    st.session_state["chat_history"].append({"role": "assistant", "content": assitant_response})
    
    with st.chat_message("assistant"):
        st.markdown(assitant_response)