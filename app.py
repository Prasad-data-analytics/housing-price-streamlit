import streamlit as st
import joblib
import numpy as np

# Load trained Linear Regression model
model = joblib.load("paris_model.pkl")

st.title("🏠 Paris Housing Price Prediction")
st.write("Enter property details to predict price.")

# Input fields
squareMeters = st.number_input("Square Meters", min_value=10, max_value=1000, value=50)
numberOfRooms = st.number_input("Number of Rooms", min_value=1, max_value=20, value=3)
hasYard = st.selectbox("Has Yard", [0, 1])
hasPool = st.selectbox("Has Pool", [0, 1])
floors = st.number_input("Number of Floors", min_value=1, max_value=50, value=1)
cityCode = st.number_input("City Code", min_value=10000, max_value=99999, value=75000)
cityPartRange = st.number_input("City Part Range", min_value=0, max_value=10, value=5)
numPrevOwners = st.number_input("Number of Previous Owners", min_value=0, max_value=10, value=1)
made = st.number_input("Year Built", min_value=1800, max_value=2025, value=2000)
isNewBuilt = st.selectbox("Is Newly Built", [0, 1])
hasStormProtector = st.selectbox("Has Storm Protector", [0, 1])
basement = st.selectbox("Has Basement", [0, 1])
attic = st.selectbox("Has Attic", [0, 1])
garage = st.selectbox("Has Garage", [0, 1])
hasStorageRoom = st.selectbox("Has Storage Room", [0, 1])
hasGuestRoom = st.selectbox("Has Guest Room", [0, 1])

if st.button("Predict Price"):
    features = np.array([[squareMeters, numberOfRooms, hasYard, hasPool, floors,
                          cityCode, cityPartRange, numPrevOwners, made, isNewBuilt,
                          hasStormProtector, basement, attic, garage, hasStorageRoom, hasGuestRoom]])
    prediction = model.predict(features)[0]
    st.success(f"Estimated Price: €{prediction:,.2f}")
