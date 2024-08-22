import streamlit as st
import google.generativeai as genai
from PIL import Image

st.title("Welcome to gemini")

# Display the uploaded screenshot
image_path = r"C:\Users\vmd86\OneDrive\Pictures\Screenshots\Screenshot 2024-08-22 180424.png"
screenshot = Image.open(image_path)
st.image(screenshot, caption="Screenshot of Karthik's Profile", use_column_width=True)

genai.configure(api_key="AIzaSyBJJj5qsMgeD7DdT6JcCIzMk9lJOPvHo0Q")
text = st.text_input("Enter")  # @param {type: "string"}

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
