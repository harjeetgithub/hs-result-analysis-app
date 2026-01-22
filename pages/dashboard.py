import streamlit as st
import pandas as pd

# Check if user is logged in
if not st.session_state.get("authentication_status"):
    st.warning("Please login first")
    st.stop()

# Get the user role
role = st.session_state.get("role", "faculty")  # default to faculty

# Restrict page access
if role != "admin":
    st.error("You do not have access to this page")
    st.stop()

# Page content for admin only
st.title("Upload Server Generated Excel Files")

uploaded_files = st.file_uploader(
    "Choose Excel files",
    type=["xlsx", "xls"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        df = pd.read_excel(file)
        st.subheader(file.name)
        st.dataframe(df)



from utils import add, multiply, greet

print(add(10, 5))
print(multiply(4, 3))
print(greet("Harjeet"))