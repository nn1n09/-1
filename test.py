import streamlit as st

col1, col2 = st.columns([2,3])
with col1:
    st.title('here is col1')
with col2:
    st.title('here is col2')
    st.checkbox('this is checkbox in col2')

col1.subheader('i am col1 subheader')
col2.checkbox('check in 2')
