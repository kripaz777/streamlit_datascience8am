import streamlit as st
import google.generativeai as genai

# ====== CONFIG ======

MODEL_NAME = "gemini-3.1-flash-lite"
# ====================

# --- Initialize ---
st.title("💬 Gemini QA App")
GOOGLE_API_KEY = st.text_input("Enter your Gemini API key:", type="password")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)
# --- User Input ---
st.write("Ask any question below:")
user_query = st.chat_input("Type your question here...")

# --- Chat Loop ---
if user_query:
    with st.spinner("Thinking..."):
        response = model.generate_content(user_query)

    # --- Display ---
    st.chat_message("user").markdown(user_query)
    st.chat_message("assistant").markdown(response.text)


