import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=350)

with col2:
    st.title("Whydoes")
    content = """
    Hi am here to show you what I learned about Phyton it is begining of my journey, but more things to come..
    Happy to share what I made.
    """
    st.info(content)

