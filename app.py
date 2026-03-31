
import streamlit as st
import numpy as np
import pickle

# load model
model = pickle.load(open("model.pkl", "rb"))

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction details:")

# inputs
time = st.number_input("Transaction Time")
amount = st.number_input("Transaction Amount")
v1 = st.number_input("V1")
v2 = st.number_input("V2")

# prediction
if st.button("Predict"):
    
    input_data = np.array([[time, v1, v2, amount]])
    
    result = model.predict(input_data)
    
    if result[0] == 1:
        st.error("🚨 Fraud Transaction")
    else:
        st.success("✅ Legitimate Transaction")
