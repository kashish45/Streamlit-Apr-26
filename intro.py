import streamlit as st

st.title("first streamlit application")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.write("Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps - so let's get started!")

agree = st.checkbox("I agree with kashish")

if agree:
    st.write("Great!")  


genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"]
)

if genre == "Comedy":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")


num1=st.number_input("Enter a number")
num2=st.number_input("Enter another number")

print("The sum of two numbers is:", num1+num2)

if st.button("Add"):
    st.write("The sum of two numbers is:", num1+num2)

