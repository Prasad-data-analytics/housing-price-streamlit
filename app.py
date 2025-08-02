import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('best_model.pkl','rb'))

st.title('Housing Price Prediction')

# Example feature inputs
feature_inputs = {}
for col in model.feature_names_in_:
    feature_inputs[col] = st.number_input(f'Enter value for {col}', value=0.0)

if st.button('Predict Price'):
    input_df = pd.DataFrame([feature_inputs])
    pred = model.predict(input_df)[0]
    st.success(f'Predicted Price: {pred:.2f}')
