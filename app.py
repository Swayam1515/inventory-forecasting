import streamlit as st

# Title and Description
st.title("Inventory Forecasting Dashboard")
st.write("This app showcases inventory forecasting insights.")

# Sample Input
user_input = st.number_input("Enter inventory demand:", min_value=0)

# Sample Output
st.write(f"Predicted inventory needed: {user_input * 1.1}")

# Upload File Option
uploaded_file = st.file_uploader("Upload your forecasting dataset")

if uploaded_file:
    st.write("File uploaded successfully!")