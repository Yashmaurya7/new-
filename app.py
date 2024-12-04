import streamlit as st

st.title("Add Two Numbers")

# Inputs for the two numbers
num1 = st.number_input("Enter the first number:", step=1.0)
num2 = st.number_input("Enter the second number:", step=1.0)

# Button to calculate the sum
if st.button("Calculate Sum"):
    result = num1 + num2
    st.success(f"The sum of {num1} and {num2} is {result}")
