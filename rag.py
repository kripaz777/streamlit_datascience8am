import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import google.generativeai as genai

# configure API key (must be set by user)
GOOGLE_API_KEY = st.text_input("Enter your Gemini API key:", type="password")
genai.configure(api_key=GOOGLE_API_KEY)
# load model
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# embedding model
model_embed = SentenceTransformer("all-MiniLM-L6-v2")
file = open("job.txt")
documents = file.read().split('\n\n')
file.close()
# # convert text → vectors
embeddings = model_embed.encode(documents)

# create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

st.title("RAG Application")
try:
    user_query = st.chat_input("Type your question here...")

    query_vec = model_embed.encode([user_query])

    D, I = index.search(np.array(query_vec), k=2)

    prompt = f"""Fisrt read the document or text "{documents[I[0][0]]}" then Search the user query "{user_query}". Give me in short answer."""


    if user_query:
        with st.spinner("Thinking..."):
            response = model.generate_content(prompt)

        # --- Display ---
        st.chat_message("user").markdown(user_query)
        st.chat_message("assistant").markdown(response.text)
except:
    st.success("Please enter a valid query.")