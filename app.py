import streamlit as st

st.set_page_config(
  page_title="Murari Portfolio",
  layout="wide"
)

st.title("Murari Portfolio")
st.subheader("Python beckend developer")

st.write("Welcome to my portfolio!")


col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/Murari_Profile_Image.png", width=200)

with col2:
    st.title("Murari Shrivastava")
    st.subheader("Python Backend Developer")
    st.write("Building scalable backend systems.")

with open("assets/Murari Shrivastava_Senior_Software_Developer.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="Download Resume",
    data=PDFbyte,
    file_name="Murari Shrivastava_Senior_Software_Developer.pdf",
    mime="application/octet-stream"
)