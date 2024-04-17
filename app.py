from openai import OpenAI
import streamlit as st

f=open(r'GenAI\api.txt')
OPEN_API_KEY=f.read()

client=OpenAI(api_key=OPEN_API_KEY)

st.title("AI Code Reviewer")
st.subheader("Test Run")

prompt=st.text_input("enter code to be checked")

#if button clicked generate and print response

if st.button("Generate")==True:

    response=client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[{'role':"system",'content':'''you are a helpful AI Assistant who is an expert in python.
               Given a code, you always point out the errors and bugs in the code and give the error free code'''},{'role':"user","content":prompt}]
)

    st.write(response.choices[0].message.content)




