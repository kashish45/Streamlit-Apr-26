import streamlit as st

import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
data = pd.DataFrame({
    "fuel_type": [
        "Petrol", "Diesel", "Petrol", "Electric",
        "Diesel", "Petrol", "Electric", "Diesel",
        "Petrol", "Electric"
    ],
    "horsepower": [
        100, 130, 150, 220,
        120, 180, 260, 140,
        110, 300
    ],
    "transmission": [
        "Manual", "Manual", "Automatic", "Automatic",
        "Automatic", "Manual", "Automatic", "Manual",
        "Automatic", "Automatic"
    ],
    "seats": [
        5, 5, 5, 5,
        7, 5, 5, 7,
        5, 5
    ],
    "price": [
        8, 11, 14, 28,
        15, 18, 35, 14,
        10, 42
    ]
})


X = data[
    [
        "fuel_type",
        "horsepower",
        "transmission",
        "seats"
    ]
]

y = data["price"]

categorical_features = [
    "fuel_type",
    "transmission"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "regressor",
            RandomForestRegressor(
                n_estimators=100,
                random_state=42
            )
        )
    ]
)

model.fit(X, y)
joblib.dump(
    model,
    "car_price_model.joblib"
)
