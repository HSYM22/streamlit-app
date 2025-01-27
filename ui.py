import streamlit as st
import requests

# Define the API endpoint
API_URL = "http://localhost:8000/predict"

# Create input columns for user input
def user_input():
    st.title("Loan Default Prediction")
    st.write("Fill in the details below to predict loan default risk:")

    # Input fields
    person_age = st.number_input("Person Age", min_value=18, max_value=100, step=1, value=25, format="%d")
    person_income = st.number_input("Person Income", min_value=0, step=1000, value=50000, format="%d")
    person_home_ownership = st.selectbox(
        "Person Home Ownership", ["MORTGAGE", "RENT", "OWN", "OTHER"]
    )
    person_emp_length = st.number_input("Person Employment Length (Years)", min_value=0.0, step=0.1, value=5.0)
    loan_intent = st.selectbox(
        "Loan Intent", ["EDUCATION", "PERSONAL", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"]
    )
    loan_grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])
    loan_amnt = st.number_input("Loan Amount", min_value=0, step=1000, value=10000, format="%d")
    loan_int_rate = st.number_input("Loan Interest Rate (%)", min_value=0.0, step=0.1, value=5.0)
    loan_percent_income = st.number_input("Loan Percent Income", min_value=0.0, step=0.1, value=10.0)
    cb_person_default_on_file = st.selectbox("Person Default on File", ["N", "Y"])
    cb_person_cred_hist_length = st.number_input("Credit History Length (Years)", min_value=0, step=1, value=10, format="%d")

    # Store inputs into a dictionary
    data = {
        "person_age": person_age,
        "person_income": person_income,
        "person_home_ownership": person_home_ownership,
        "person_emp_length": person_emp_length,
        "loan_intent": loan_intent,
        "loan_grade": loan_grade,
        "loan_amount": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_default_on_file": cb_person_default_on_file,
        "cb_person_cred_hist_length": cb_person_cred_hist_length
    }
    return data

# Get user inputs
data = user_input()

# Predict button
if st.button("Predict"):
    try:
        # Send the input data to the API
        response = requests.post(API_URL, json=data)
        response_data = response.json()

        # Display the prediction result
        st.subheader("Prediction Result")
        st.write(f"Predicted Class: {response_data['predicted_class']}")
        st.write(f"Prediction Probability: {response_data['prediction_proba']:.2f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")