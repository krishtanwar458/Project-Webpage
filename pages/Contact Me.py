import streamlit as st
from send_email1 import send_email

st.header('Contact Me')

with st.form(key='email_form'):
    user_email = st.text_input('Your Email')
    raw_message = st.text_area('Your Message')
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
""" 
    button = st.form_submit_button('Submit')
    if button:
        send_email(message)
        st.info('Your email was sent successfully!')