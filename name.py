import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("gemini")

# Configure the Gemini API
genai.configure(api_key=api_key)

# Use the correct model name
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# Function to generate names
def generate_names(business_idea, count, language):
    prompt = (
        f"Suggest {count} unique, catchy, and creative business names "
        f"for this idea:\n\n'{business_idea}'\n\n"
        f"Return the names as a numbered list in {language} language."
    )
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Business Name Generator", page_icon="💡")
st.title("💡 Business Name Generator")
st.write("Generate creative business names using Google Gemini AI!")

user_idea = st.text_area("Enter your business idea", placeholder="e.g., A platform for renting eco-friendly camping gear.")

name_count = st.number_input("How many names to generate?", min_value=1, max_value=50, value=5, step=1)

language = st.selectbox("Select language", ["English", "Hindi", "Odia", "Hinglish"])

if st.button("Generate Business Names"):
    if not user_idea.strip():
        st.warning("Please enter a business idea.")
    else:
        with st.spinner("Thinking..."):
            result = generate_names(user_idea, name_count, language)
        st.success(f"Here are {name_count} business name ideas in {language}:")
        st.markdown(result)
