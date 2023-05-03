import streamlit as st
import pickle
     

# Load our model
file_path = '/content/drive/MyDrive/CODING DOJO DS BOOTCAMP/PROJECTS/PROJECT 2/Stroke Prediction Dataset/'
pickle_in = open(f'{file_path}best_knn_model.pkl', 'rb')
model = pickle.load(pickle_in)
     

def welcome():
  return 'Welcome All'
     

parameters = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
       'work_type', 'Residence_type', 'avg_glucose_level', 'bmi',
       'smoking_status', 'stroke']
     

def predict_stroke(gender, age, hypertension, heart_disease, ever_married,
       work_type, Residence_type, avg_glucose_level, bmi,
       smoking_status, stroke):
  prediction = model.predict([gender, age, hypertension, heart_disease, ever_married,
       work_type, Residence_type, avg_glucose_level, bmi,
       smoking_status, stroke])
  print(prediction)
  return prediction
     

def main():
  st.title('Heart Stroke Prediction')
  gender = st.text_input('Enter Your Gender?')
  age = st.text_input('Enter Your age?')
  hypertension = st.text_input('Enter Your hypertension?')
  heart_disease = st.text_input('Enter Your heart_disease?')
  ever_married = st.text_input('Enter Your ever_married?')
  work_type = st.text_input('Enter Your work_type?')
  residence_type = st.text_input('Enter Your Residence Type?')
  avg_glucose_level = st.text_input('Enter Your glucose levels?')
  bmi = st.text_input('Enter Your bmi?')
  smoking_status = st.text_input('Enter Your smoking status?')
  result = ''
  if st.button('Predict'):
    result = predict_stroke(gender, age, hypertension, heart_disease, ever_married,
       work_type, residence_type, avg_glucose_level, bmi,
       smoking_status)
  st.success(f'The output is: {result}')


if __name__ == '__main__':
  main()
  
