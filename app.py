import streamlit as st

st.write("Calculator Application")
num1 = st.number_input("Enter first number", placeholder="first number")
num2 = st.number_input("Enter second number", placeholder="second number")

operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

ret=st.button("Calculate")
if ret:
    if operation == "Addition":
        result = num1 + num2
        st.write("Result:", result)
    elif operation == "Subtraction":
        result = num1 - num2
        st.write("Result:", result)
    elif operation == "Multiplication":
        result = num1 * num2
        st.write("Result:", result)
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.write("Result:", result)
        else:
            st.write("Error: Division by zero is not allowed.")