import streamlit as st
import pandas as pd
import joblib
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(base_dir, 'model.pkl'))
columns = joblib.load(os.path.join(base_dir, 'columns.pkl'))

st.title("Adult Salary Predictor")
st.write("Predict whether a person earns >50K or <=50K")

# === USER INPUT FORM ===
age = st.number_input("Age", 18, 100, step=1)
education_num = st.number_input("Education Number", 1, 20, step=1)
capital_gain = st.number_input("Capital Gain", 0, 100000, step=100)
capital_loss = st.number_input("Capital Loss", 0, 5000, step=10)
hours_per_week = st.number_input("Hours per Week", 1, 100, step=1)

sex = st.selectbox("Sex", ['Male', 'Female'])
race = st.selectbox("Race", ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'])
workclass = st.selectbox("Workclass", ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay'])
relationship = st.selectbox("Relationship", ['Husband', 'Wife', 'Not-in-family', 'Unmarried', 'Own-child', 'Other-relative'])
occupation = st.selectbox("Occupation", ['Exec-managerial', 'Handlers-cleaners', 'Adm-clerical', 'Sales', 'Craft-repair', 'Prof-specialty', 'Other-service', 'Machine-op-inspct', 'Transport-moving', 'Farming-fishing', 'Tech-support', 'Protective-serv', 'Priv-house-serv', 'Armed-Forces'])

# === Create dummy row ===
user_input = {
    'age': age,
    'education.num': education_num,
    'capital.gain': capital_gain,
    'capital.loss': capital_loss,
    'hours.per.week': hours_per_week,
    f'sex_{sex}': 1,
    f'race_{race}': 1,
    f'workclass_{workclass}': 1,
    f'relationship_{relationship}': 1,
    f'occupation_{occupation}': 1,
}

# Convert to DataFrame
input_df = pd.DataFrame([user_input])
input_df = input_df.reindex(columns=columns, fill_value=0)  # Fill missing dummy columns with 0

# === Predict ===
if st.button("Predict"):
    pred = model.predict(input_df)[0]
    label = ">50K" if pred == 1 else "<=50K"
    st.success(f"Prediction: The person is likely to earn {label}.")
