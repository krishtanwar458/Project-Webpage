import streamlit as st #python3 -m streamlit run main.py

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.JPG', width=900)
with col2:
    st.title('Krish Tanwar')
    content = """
    Hi, my name is Krish. 
    """
    st.info(content)

content2 = 'Below you can find some of the apps I have builf in Python ' \
            'Feel free to contact me!'

st.text(content2)