import pandas as pd
import numpy as np
import streamlit as st
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Financial_Inclusion Prediction App")
st.write("Enter respondent details to predict bank account ownership.")

# Create input fields
age = st.number_input("Age of Respondent", min_value=10, max_value=100, step=1)
household_size = st.number_input("Household Size", min_value=1, max_value=20, step=1)

# Define categorical options (for Label Encoding)
education_levels = ["No formal education", "Other/Dont know/RTA", "Primary education",
                    "Secondary education", "Tertiary education", "Vocational/Specialised training"]
genders = ["Female", "Male"]
job_types = ["Dont Know/Refuse to answer", "Farming and Fishing", "Formally employed Government",
             "Formally employed Private", "Government Dependent", "Informally employed", "No Income",
             "Other Income", "Remittance Dependent", "Self employed"]
marital_statuses = ["Divorced/Seperated", "Dont know", "Married/Living together",
                    "Single/Never Married", "Widowed"]
relationship_types = ["Child", "Head of Household", "Other non-relatives",
                      "Other relative", "Parent", "Spouse"]

# Categorical input fields
cellphone_access = st.radio("Cellphone Access", ["No", "Yes"])
education_level = st.selectbox("Education Level", education_levels)
gender = st.radio("Gender", genders)
job_type = st.selectbox("Job Type", job_types)
location_type = st.radio("Location Type", ["Rural", "Urban"])
marital_status = st.selectbox("Marital Status", marital_statuses)
relationship_with_head = st.selectbox("Relationship with Head", relationship_types)

# Function to encode inputs
def encode_inputs():
    input_data = [
        age, household_size,
        0 if cellphone_access == "No" else 1,  # Binary encoding
        education_levels.index(education_level),
        genders.index(gender),
        job_types.index(job_type),
        0 if location_type == "Rural" else 1,  # Binary encoding
        marital_statuses.index(marital_status),
        relationship_types.index(relationship_with_head)
    ]
    return np.array([input_data])  # Ensure it's a 2D array

# Predict button
if st.button("Predict"):
    input_features = encode_inputs()
    prediction = model.predict(input_features)
    result = "Has a Bank Account" if prediction[0] == 1 else "No Bank Account"
    st.success(f"Prediction: {result}")
