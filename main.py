import streamlit as st #python3 -m streamlit run main.py
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.JPG', width=700)
with col2:
    st.title('Krish Tanwar')
    content = """
    Hi, my name is Krish. 
    """
    st.info(content)

content2 = 'Below you can find some of the apps I have builf in Python ' \
            'Feel free to contact me!'

st.text(content2)

col3, col4 = st.columns(2)

df = pd.read_csv('data.csv', sep=';')
with col3:
    for i, row in df[:10].iterrows():
        st.title(row['title'])

with col4:
    for i, row in df[10:].iterrows():
        st.title(row['title'])
        