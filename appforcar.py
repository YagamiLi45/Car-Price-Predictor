# import streamlit as st 
# import pickle
# import pandas as pd
# import sklearn
# from sklearn.pipeline import make_pipeline

# st.title("Welcome to car price predictor")

# model_file="rf_pipeline.pkl"

# with open(model_file, 'rb') as file:
#     model_predictor = pickle.load(file)

# col_names = ['year', 'km_driven', 'fuel', 'seller_type',
#        'transmission', 'owner', 'mileage', 'seats', 'Brand', 'Model',
#        'make_country']

# # year = 2013
# # km_driven=40000
# # fuel='Petrol'
# # seller_type='Dealer'
# # transmission='Automatic'
# # owner='First Owner'
# # mileage=23.4
# # seats=5
# # Brand='Maruti'
# # Model='Swift Dzire VDI'
# # make_country='India'


# year = st.slider("Year of Manufacture", min_value=1990, max_value=2023)
# make_country = st.text_input("Country of Manufacture")
# Brand = st.text_input("Car Brand")
# Model = st.text_input("Car Model")
# km_driven = st.number_input("Kilometers Driven")
# fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG"])
# mileage = st.number_input("Mileage (km/l)", min_value=0.0)
# seats = st.number_input("Number of Seats", min_value=2, max_value=20)
# seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
# transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])
# owner = st.selectbox("Owner Type", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner"])



# col_names=[year, km_driven, fuel, seller_type, transmission, owner, mileage, seats, Brand, Model, make_country]

# if st.button("Predict"):
#     df_input = pd.DataFrame([[year, km_driven, fuel, seller_type, transmission, owner, mileage, seats, Brand, Model, make_country]], columns=col_names)
#     prediction=model_predictor.predict(df_input)
#     st.write(f"Predicted Car Price: ₹{prediction[0]:.2f}")
import streamlit as st
import pickle
import pandas as pd

st.title("Car Price Predictor")

# Define the column names for the input DataFrame
col_names = ['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'seats', 'Brand', 'Model', 'make_country']

# Create input widgets for user input
year = st.slider("Year of Manufacture", min_value=1990, max_value=2023, value=2013)
km_driven = st.number_input("Kilometers Driven", min_value=0, value=40000)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG"], index=0)
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"], index=0)
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"], index=1)
owner = st.selectbox("Owner Type", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner"], index=0)
mileage = st.number_input("Mileage (km/l)", min_value=0.0, value=23.4)
seats = st.number_input("Number of Seats", min_value=2, max_value=20, value=5)
Brand = st.text_input("Car Brand", value="Maruti")
Model = st.text_input("Car Model", value="Swift Dzire VDI")
make_country = st.text_input("Country of Manufacture", value="India")

# Create a DataFrame with user input
user_input = pd.DataFrame([[year, km_driven, fuel, seller_type, transmission, owner, mileage, seats, Brand, Model, make_country]], columns=col_names)

# Load the trained machine learning model
model_file = "rf_pipeline.pkl"
with open(model_file, 'rb') as file:
    loaded_pipeline = pickle.load(file)

# Make predictions
if st.button("Predict"):
    prediction = loaded_pipeline.predict(user_input)
    st.write(f"Predicted Car Price: ₹{prediction[0]:.2f}")

