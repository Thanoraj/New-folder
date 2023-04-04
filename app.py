import streamlit as st

# Define a text input field
text_input = st.text_input('Enter your name')

# Define a slider
slider_val = st.slider('Select a value', 1, 5, 1)

# Define a submit button
submit_button = st.button('Submit')

# Handle button click event
if submit_button:
    prompt = 'Hello, {}! You selected {} on the slider.'.format(text_input, slider_val)
    st.write(prompt)