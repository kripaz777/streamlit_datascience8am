import streamlit as st
import pandas as pd

st.title("Covid Predection")

Cough_symptoms = st.selectbox("Cough symptoms = ", [True, False])
Fever = st.selectbox("Fever = ", [True, False])
Sore_throat = st.selectbox("Sore throat = ", [True, False])
Shortness_of_breath = st.selectbox("Shortness of breath = ", [True, False])
Headache = st.selectbox("Headache = ", [True, False])
# Age_60_above = st.selectbox("Age 60 above = ", [True, False])
# Sex = st.selectbox("Sex = ", ["Male", "Female"])
Known_contact = st.selectbox("Known contact = ", ["Abroad", "Contact with confirmed", "Other"])
if Known_contact == "Abroad":
    Known_contact = 0
elif Known_contact == "Contact with confirmed":
    Known_contact = 1
else:
    Known_contact = 2

if st.button("Predict"):
    st.success("The form is submitted successfully")
    data = {"Cough symptoms": [Cough_symptoms], "Fever": [Fever], "Sore throat": [Sore_throat],
            "Shortness of breath": [Shortness_of_breath], "Headache": [Headache], "Known contact": [Known_contact]}
    df = pd.DataFrame(data)
    st.write(df)