import streamlit as st
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Load your trained model
model = joblib.load('model.pkl')

# Title and description
st.title('Credit Default Prediction ')
st.write('Predict whether a customer will default on their payment based on PCA-transformed features.')

# Input fields for user input - Numerical columns 'Time' and 'Amount' and PCA components 'V1' to 'V28'
Time = st.number_input('Transaction Time (Time)', min_value=0)
Amount = st.number_input('Transaction Amount (Amount)', min_value=0)

# Features from PCA (V1 to V28)
V1 = st.number_input('V1', value=0.0)
V2 = st.number_input('V2', value=0.0)
V3 = st.number_input('V3', value=0.0)
V4 = st.number_input('V4', value=0.0)
V5 = st.number_input('V5', value=0.0)
V6 = st.number_input('V6', value=0.0)
V7 = st.number_input('V7', value=0.0)
V8 = st.number_input('V8', value=0.0)
V9 = st.number_input('V9', value=0.0)
V10 = st.number_input('V10', value=0.0)
V11 = st.number_input('V11', value=0.0)
V12 = st.number_input('V12', value=0.0)
V13 = st.number_input('V13', value=0.0)
V14 = st.number_input('V14', value=0.0)
V15 = st.number_input('V15', value=0.0)
V16 = st.number_input('V16', value=0.0)
V17 = st.number_input('V17', value=0.0)
V18 = st.number_input('V18', value=0.0)
V19 = st.number_input('V19', value=0.0)
V20 = st.number_input('V20', value=0.0)
V21 = st.number_input('V21', value=0.0)
V22 = st.number_input('V22', value=0.0)
V23 = st.number_input('V23', value=0.0)
V24 = st.number_input('V24', value=0.0)
V25 = st.number_input('V25', value=0.0)
V26 = st.number_input('V26', value=0.0)
V27 = st.number_input('V27', value=0.0)
V28 = st.number_input('V28', value=0.0)

# Prediction button
if st.button('Predict'):
    # Creating a feature array based on the input
    input_data = np.array([[Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount]])

    # Feature scaling (if your model requires it)
    scaler = StandardScaler()
    input_data_scaled = scaler.fit_transform(input_data)
    
    # Model prediction
    prediction = model.predict(input_data_scaled)
    
    # Output the result
    if prediction[0] == 1:
        st.write('The customer is likely to default on their payment.')
    else:
        st.write('The customer is unlikely to default on their payment.')
