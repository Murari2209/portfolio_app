import streamlit as st

st.title("🚀 Projects")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://via.placeholder.com/300")
    st.subheader("GitHub Analyzer")
    st.write("Analyze GitHub profiles and repositories.")
    st.markdown("[🔗 View Project](https://github.com/Murari2209/Github-Analyzer)")

with col2:
    st.image("https://via.placeholder.com/300")
    st.subheader("Job Market Intelligence")
    st.write("Analyze job trends using datasets.")
    st.markdown("[🔗 View Project](https://github.com/Murari2209)")

with col3:
    st.image("https://via.placeholder.com/300")
    st.subheader("Pension Sanction System")
    st.write("Generate E-PPOs For Indian AirForce Pensioners.")
    st.markdown("[🔗 View Project](https://github.com/Murari2209)")