# TDS GAs 8

import streamlit as st

st.title("Largest of Three")

n1 = st.number_input("Enter the first number:")
n2 = st.number_input("Enter the second number:")
n3 = st.number_input("Enter the third number:")
largest = max(n1,n2,n3)
st.write(f"The largest number is {largest}")
