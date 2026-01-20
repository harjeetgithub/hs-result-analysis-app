import streamlit as st
import pandas as pd
st.title("Automatic Result Analysis Generator")
st.write("### Input Data")
col1,col2,col3,col4= st.columns(4)
f_name= col1.text_input("Enter Faculty Name")
CoC_name= col2.text_input("Enter CoC Name")
HeadAcademic_name= col3.text_input("Head Academic Name")
Dean_name= col4.text_input("Enter Dean Name")
if st.button("Store in DataFrame"):
    data = {
        "Input_No": [1, 2, 3, 4],
        "Value": [f_name, CoC_name, HeadAcademic_name, Dean_name]
    }

    df = pd.DataFrame(data)

    st.success("Data stored successfully!")
    st.dataframe(df)