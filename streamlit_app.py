import joblib
import numpy as np
import streamlit as st

model = joblib.load("model.pkl")
X_train_final = joblib.load('X_train_final.pkl')
df = X_train_final

st.title("NYC House Price Predictor")

row_idx = st.selectbox("Select a property row to auto-fill features:", df.index)
selected_row = df.loc[row_idx]

features = X_train_final.columns.tolist()
input_data = selected_row[features].to_frame().T

st.write("Selected Property Details:", input_data)

if st.button("Predict Price"):
    pred_log = model.predict(input_data)
    pred_price = np.expm1(pred_log)
    st.success(f"🏠 Estimated Price: ${pred_price[0]:,.0f}")