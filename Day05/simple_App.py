import streamlit as st
st.title("My first streamlit App!!!")
st.write("welcome to my AI application!")
name = st.text_input("Enter your name: ")
if st.button("submit"):
    st.write("Hello", name)