import joblib
import pandas as pd
import streamlit as st


st.title("Car Price Predictor")

st.write(
    "Enter the details of the car to estimate its price."
)

model=joblib.load("car_price_model.joblib")

col1,col2=st.columns(2)

with col1:
    fuel_type=st.selectbox(
        "Fuel Type",
        ["Petrol","Diesel","Electric"]
    )
    horsepower=st.slider(
        "Horsepower",
        min_value=50,
        max_value=500,
        value=150
    )

with col2:
    transmission=st.selectbox(
        "Transmission",
        ["Manual","Automatic"]
    )
    seats=st.selectbox(
        "Number of Seats",
        [2,4,5,7]
    )

if st.button("Predict Price"): 
    input_data=pd.DataFrame(
        {
            "fuel_type":[fuel_type],
            "horsepower":[horsepower],
            "transmission":[transmission],
            "seats":[seats]
        }
    )
    predicted_price=model.predict(input_data)
    st.write(f"The estimated price of the car is: ${predicted_price[0]:.2f}")