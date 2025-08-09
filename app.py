import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("paris_model.pkl")

st.title("🏠 Paris Housing Price Prediction")

# Collect user inputs
squareMeters = st.number_input("Square meters", min_value=10, max_value=1000000, value=50)
numberOfRooms = st.number_input("Number of rooms", min_value=1, max_value=20, value=3)
hasYard = st.selectbox("Has yard?", [0, 1])
hasPool = st.selectbox("Has pool?", [0, 1])
floors = st.number_input("Floors", min_value=1, max_value=50, value=1)
cityCode = st.number_input("City code", value=1000)
cityPartRange = st.number_input("City part range", min_value=1, max_value=10, value=5)
numPrevOwners = st.number_input("Number of previous owners", min_value=0, max_value=10, value=0)
hasStormProtector = st.selectbox("Has storm protector?", [0, 1])
basement = st.selectbox("Has basement?", [0, 1])
attic = st.selectbox("Has attic?", [0, 1])
garage = st.selectbox("Has garage?", [0, 1])
hasStorageRoom = st.selectbox("Has storage room?", [0, 1])
hasGuestRoom = st.selectbox("Has guest room?", [0, 1])
HouseAge = st.number_input("House age (years)", min_value=0, max_value=200, value=10)

if st.button("Predict Price"):
    features = np.array([[squareMeters, numberOfRooms, hasYard, hasPool, floors,
                          cityCode, cityPartRange, numPrevOwners, hasStormProtector,
                          basement, attic, garage, hasStorageRoom, hasGuestRoom, HouseAge]])
    prediction = model.predict(features)
    st.success(f"Estimated Price: €{prediction[0]:,.2f}")
