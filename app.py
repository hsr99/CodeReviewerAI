from openai import OpenAI
import streamlit as st

# Read API key from a file
with open(r'GenAI\api.txt') as f:
    OPEN_API_KEY = f.read()

# Initialize OpenAI client
client = OpenAI(api_key=OPEN_API_KEY)

# Set up Streamlit app
st.title("AI Code Reviewer")
st.subheader("Test Run")

# Input field for code
prompt = st.text_area("Enter code to be checked", "Paste your code here...")

# Button to generate response
if st.button("Generate", key="generate_button"):
    with st.spinner('Generating...'):
        # Call OpenAI API to generate response
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role':"system",'content':'''you are a helpful AI Assistant who is an expert in python.
                       Given a code, you always mention every error and bug in text format and also give the error free code'''},{'role':"user","content":prompt}]
        )
    # Display response
    if response and response.choices:
        st.code(response.choices[0].message.content, language='python')
    else:
        st.error("Oops! Something went wrong. Please check your code and try again.")
