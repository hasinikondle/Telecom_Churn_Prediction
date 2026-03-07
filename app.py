# Streamlit UI for Churn Prediction

import numpy as np
import pickle
import streamlit as st
import pandas as pd

# ------------------ LOAD MODEL ------------------ #

with open("SVM_model.pkl","rb") as file:
    model = pickle.load(file)

# ------------------ PAGE SETTINGS ------------------ #

st.set_page_config(
    page_title="Telecom Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

# ------------------ SIDEBAR ------------------ #

with st.sidebar:
    st.title("Telecom Churn App")
    st.image("https://www.seedsetgroup.com/wp-content/uploads/2019/04/000-2.jpg")
    st.write("Predict whether a telecom customer will churn.")

# ------------------ MAIN TITLE ------------------ #

st.title("📊 Customer Churn Prediction System")
st.write("Enter customer details to predict churn.")

st.divider()

# ------------------ INPUT FIELDS ------------------ #

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male","Female"])
    senior = st.selectbox("Senior Citizen", [0,1])
    partner = st.selectbox("Partner", ["Yes","No"])
    dependents = st.selectbox("Dependents", ["Yes","No"])
    tenure = st.slider("Tenure (Months)",1,72)

    phone = st.selectbox("Phone Service", ["Yes","No"])
    multiple = st.selectbox("Multiple Lines", ["No","Yes","No phone service"])
    internet = st.selectbox("Internet Service", ["DSL","Fiber optic","No"])
    security = st.selectbox("Online Security", ["No","Yes","No internet service"])
    backup = st.selectbox("Online Backup", ["No","Yes","No internet service"])

with col2:
   
    device = st.selectbox("Device Protection", ["No","Yes","No internet service"])
    tech = st.selectbox("Tech Support", ["No","Yes","No internet service"])
    tv = st.selectbox("Streaming TV", ["No","Yes","No internet service"])
    movies = st.selectbox("Streaming Movies", ["No","Yes","No internet service"])

    contract = st.selectbox("Contract Type", ["Month-to-month","One year","Two year"])
    paperless = st.selectbox("Paperless Billing", ["Yes","No"])
    payment = st.selectbox("Payment Method",
                           ["Electronic check","Mailed check",
                            "Bank transfer (automatic)",
                            "Credit card (automatic)"])

    monthly = st.number_input("Monthly Charges",10.0,200.0)
    total = st.number_input("Total Charges",10.0)

st.divider()

# ------------------ ENCODING ------------------ #

gender = 1 if gender=="Male" else 0
partner = 1 if partner=="Yes" else 0
dependents = 1 if dependents=="Yes" else 0
phone = 1 if phone=="Yes" else 0
paperless = 1 if paperless=="Yes" else 0

# Multiple Lines
multiple_map = {"No":0,"Yes":1,"No phone service":2}
multiple = multiple_map[multiple]

# Internet
internet_map = {"DSL":0,"Fiber optic":1,"No":2}
internet = internet_map[internet]

# Online Services
service_map = {"No":0,"Yes":1,"No internet service":2}

security = service_map[security]
backup = service_map[backup]
device = service_map[device]
tech = service_map[tech]
tv = service_map[tv]
movies = service_map[movies]

# Contract
contract_map = {"Month-to-month":0,"One year":1,"Two year":2}
contract = contract_map[contract]

# Payment
payment_map = {
    "Electronic check":0,
    "Mailed check":1,
    "Bank transfer (automatic)":2,
    "Credit card (automatic)":3
}
payment = payment_map[payment]

# ------------------ PREPARE INPUT DATA ------------------ #

new_data = np.array([[

gender,
senior,
partner,
dependents,
tenure,
phone,
multiple,
internet,
security,
backup,
device,
tech,
tv,
movies,
contract,
paperless,
payment,
monthly,
total

]])

# ------------------ PREDICTION ------------------ #



col1, col2 = st.columns([1,2])

if col2.button("🔍 Predict Churn"):
    
    prediction = model.predict(new_data)[0]

    if prediction == 1:
        st.subheader("⚠️ Customer is likely to CHURN")

    else:
        st.subheader("✅ Customer will STAY")
        