import streamlit as st

st.set_page_config(layout="wide", page_title="Title")

# 加入css
with open('style.css') as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


