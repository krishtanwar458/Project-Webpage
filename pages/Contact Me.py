import streamlit as st

st.header('Contact Me')

with st.form(key='email_form'):
    user_emaiil = st.text_input('Your Email')
    message = st.text_area('Your Message')
    button = st.form_submit_button('Submit')
    if button:
        print('Email Sent')