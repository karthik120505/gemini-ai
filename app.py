import streamlit as st
import google.generativeai as genai
st.title("Welcome to gemini")
genai.configure(api_key="AIzaSyBJJj5qsMgeD7DdT6JcCIzMk9lJOPvHo0Q")
text = st.text_input("Enter") # @param {type: "string"}

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
