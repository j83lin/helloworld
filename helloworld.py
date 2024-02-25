import streamlit as st
st.write("Hello World!")
x = st.slider("Select a value")
st.write(x, "squared is", x * x)