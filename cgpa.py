import streamlit as st

st.title("CGPA & Percentage Calculator")

option = st.radio("Choose Conversion:", ["CGPA to Percentage", "Percentage to CGPA"])

if option == "CGPA to Percentage":
    cgpa = st.number_input("Enter your CGPA", min_value=0.0, max_value=10.0, step=0.01)
    if st.button("Convert to Percentage"):
        percentage = cgpa * 9.5
        st.success(f"Your Percentage is: {percentage:.2f}%")

elif option == "Percentage to CGPA":
    percentage = st.number_input("Enter your Percentage", min_value=0.0, max_value=100.0, step=0.1)
    if st.button("Convert to CGPA"):
        cgpa = percentage / 9.5
        st.success(f"Your CGPA is: {cgpa:.2f}")

