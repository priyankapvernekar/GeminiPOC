from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## function  to load the model

model=genai.GenerativeModel("gemini-pro")

chat=model.start_chat(history=[])


def get_response(question):
    response=chat.send_message(question,stream=True)
    return response
st.set_page_config(page_title="chat")
st.header("Chat app")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input=st.text_input("Input:",key="input")
submit=st.button("lets chat")

if submit and input:
    response=get_response(input)
        #add user quesry and response to session chat history
    st.session_state['chat_history'].append(("you",input))
    st.subheader("the response is ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("bot",chunk.text))
    st.subheader("the chat history is")

    for role,text in st.session_state['chat_history']:
        st.write(f"{role}:{text}")