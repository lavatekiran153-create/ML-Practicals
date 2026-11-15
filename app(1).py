import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My First Streamlit App",
    page_icon="💻",
    layout="centered"
)

# App title
st.title("My First Streamlit App")
st.write("Welcome! This is a simple Streamlit application.")

# User input
name = st.text_input("Enter your name:")

# Display output
if name.strip():
    st.success(f"Hello, {name}! Welcome to your app.")
else:
    st.info("Enter your name in the box above to see a greeting.")

st.caption("Created using Python and Streamlit.")
