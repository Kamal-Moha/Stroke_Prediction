import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import  LabelEncoder
file_path = '/content/drive/MyDrive/CODING DOJO DS BOOTCAMP/PROJECTS/PROJECT 2/Stroke Prediction Dataset'

df = pd.read_csv(f'{file_path}/healthcare-dataset-stroke-data.csv')

#load label encoder
le=LabelEncoder()

#df['gender']=label.fit_transform(df['gender'])
#df['ever_married']=label.fit_transform(df['ever_married'])
#df['work_type']=label.fit_transform(df['work_type'])
#df['Residence_type']=label.fit_transform(df['Residence_type'])
#df['smoking_status']=label.fit_transform(df['smoking_status'])

# Load our model
pickle_in = open(f'{file_path}/best_knn_model.pkl', 'rb')
model = pickle.load(pickle_in)


def predict_stroke(gender, age, hypertension, heart_disease, ever_married,
       work_type, Residence_type, avg_glucose_level, bmi,
       smoking_status):
  le=LabelEncoder()

  le.fit(df['gender'].value_counts().index)
  gender = le.transform([f'{gender}'])[0]

  le.fit(df['ever_married'].value_counts().index)
  ever_married = le.transform([f'{ever_married}'])[0]

  le.fit(df['work_type'].value_counts().index)
  work_type = le.transform([f'{work_type}'])[0]

  le.fit(df['Residence_type'].value_counts().index)
  Residence_type = le.transform([f'{Residence_type}'])[0]

  le.fit(df['smoking_status'].value_counts().index)
  smoking_status = le.transform([f'{smoking_status}'])[0]
  
  prediction = model.predict([[gender, age, hypertension, heart_disease, ever_married,
       work_type, Residence_type, avg_glucose_level, bmi,
       smoking_status]])[0]
  print(prediction)
  if prediction == 0:
    return 'Negative. You are good'
  elif prediction == 1:
    return 'Positive. You are most likely to have stroke. See a doctor now'


def main():
  st.title('Heart Stroke Prediction')
  #gender = st.text_input('Enter Your Gender?')
  left_column, right_column = st.columns(2)
  with left_column:
    gender = st.radio(
        'Your gender:',
        np.unique(df['gender']))
    


  age = st.slider('Your Age', 0.0, max(df["age"]), 1.0)

  hypertension = st.selectbox(
        'Your hypertension:',
        np.unique(df['hypertension']))


  heart_disease = st.radio(
        'Have Heart Disease:',
        np.unique(df['heart_disease']))


  ever_married = st.radio(
        'Have you been ever married?:',
        np.unique(df['ever_married']))
  
  work_type = st.selectbox(
        'Work Type:',
        np.unique(df['work_type']))

  residence_type = st.radio(
        'Residence Type?:',
        np.unique(df['Residence_type']))

  avg_glucose_level = st.slider('Average Glucose Level', 0.0, max(df["avg_glucose_level"]), 1.0)

  bmi = st.slider('BMI', 0.0, max(df["bmi"]), 1.0)

  smoking_status = st.radio(
        'Smoking Status?:',
        np.unique(df['smoking_status']))

  result = ''
  if st.button('Predict'):
    result = predict_stroke(gender, age, hypertension, heart_disease, ever_married,
       work_type, residence_type, avg_glucose_level, bmi,
       smoking_status)
  st.success(f'The output is: {result}')


if __name__ == '__main__':
  main()
  
