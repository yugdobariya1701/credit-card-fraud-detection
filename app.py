import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("💳 Credit Card Fraud Detection")

st.write("Enter all features:")

features = []

# Time
time = st.number_input("Time")
features.append(time)

# V1 to V28
for i in range(1, 29):
    val = st.number_input(f"V{i}")
    features.append(val)

# Amount
amount = st.number_input("Amount")
features.append(amount)

if st.button("Predict"):
    input_data = np.array([features])
    
    result = model.predict(input_data)
    
    if result[0] == 1:
        st.error("🚨 Fraud Transaction")
    else:
        st.success("✅ Legitimate Transaction")
