import streamlit as st
import os
import openai 

openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a text input field
text_input = st.text_input('Enter your name')

# Define a slider
slider_val = st.slider('Select a value', 1, 5, 1)

# Define a submit button
submit_button = st.button('Submit')

# Handle button click event
if submit_button:
    promp = 'Generate {} Questions with the topic of {}'.format(slider_val, text_input,)
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=promp,
    temperature=0.7,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    st.write(response.choices[0].text)
