import streamlit as st

st.write("Hello ")
st.write("## This is a sai hima girish")
x = st.text_input("Movie", "Star Wars")

if st.button("Click Me"):
    st.write(f"Your favorite movie is `{x}`")
