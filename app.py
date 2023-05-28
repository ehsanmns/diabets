import streamlit as st
import numpy as np
import pandas as pd
import re
import joblib
model=joblib.load('sss.joblib')
# Handling missing values
df['Glucose'].fillna(df['Glucose'].mean(), inplace=True)

# Handling outliers
q1 = df['BMI'].quantile(0.25)
q3 = df['BMI'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
df = df[(df['BMI'] >= lower_bound) & (df['BMI'] <= upper_bound)]

# Transforming data
df['Age'] = df['Age'].apply(lambda x: 1 if x > 30 else 0)

st.title('Diabetes Prediction App')

pregnancies = st.slider('Pregnancies', 0, 17, 3)
glucose = st.slider('Glucose', 0, 199, 117)
blood_pressure = st.slider('Blood Pressure', 0, 122, 72)
skin_thickness = st.slider('Skin Thickness', 0, 99, 23)
insulin = st.slider('Insulin', 0, 846, 30)
bmi = st.slider('BMI', 0.0, 67.1, 32.0)
dpf = st.slider('Diabetes Pedigree Function', 0.078, 2.42, 0.3725)
age = st.slider('Age', 21, 81, 29)

# Making predictions
input_data = np.array([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]).reshape(1, -1)
input_data = scaler.transform(input_data)
input_data = selector.transform(input_data)

prediction = model.predict(input_data)

# Displaying the prediction
if prediction == 0:
    st.write('Congratulations! Based on the information you provided, it seems like you do not have diabetes.')
else:
    st.write('Sorry, based on the information you provided, it seems like you may have diabetes. We recommend consulting with a healthcare professional to discuss your options.')
