import streamlit as st
import pandas as pd
import pickle as pk

with open("salary.pickle", "rb") as f:
    model = pk.load(f)

st.title("Salary Predection")
age = st.number_input("Pick a number", 18, 65)
exp = st.slider("Years of experience", 0, 40)
edu = st.selectbox("Education = ", ["Bachelor's", "Master's", "PhD"])
if st.button("Submit"):
    st.success("The form is submitted successfully")
    if edu == "Bachelor's":
        b = 1; m = 0; p = 0
    elif edu == "Master's":
        b = 0; m = 1; p = 0
    else:
        b = 0; m = 0; p = 1
    data = {"Age": [age], "Years of Experience": [exp], "Bachelor's": [b], "Master's": [m], "PhD": [p]}
    df = pd.DataFrame(data)

    result = round(model.predict(df)[0],2)
    st.write(f"Predicted Salary: Rs {result}")