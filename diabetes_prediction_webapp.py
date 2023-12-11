# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 12:21:49 2021

@author: TANDRIMA SINGHA
"""

import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# creating a function for prediction
def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
      st.toast('You can use emoji :sunglasses: in toast message')
    else:
      return 'The person is diabetic'
    st.toast('You can use emoji :sunglasses: in toast message')
  
def main():
    
    # giving title
    st.title('Diabetes Prediction Web App Diabetes Prediction Web App')
    st.image("logo.png",width=200)
    st.image("logo.png",width=200)
    #getting the input data from the user
    Pregnancies = st.number_input('Number of Pregnencie', value=0)
    Glucose = st.number_input('Glucose Level', value=0)
    BloodPressure = st.number_input('Blood Pressure Value', value=80)
    SkinThickness = st.number_input('Skin Thickness Value', value=0)
    Insulin = st.number_input('Insulin Level', value=0)
    BMI = st.number_input('BMI value', value=0)
    DiabetesPedigreeFunction  = st.number_input('Diabetes Pedigree Function value', value=0)
    Age  = st.number_input('Age of the person', value=0)
    
    #code for prediction 
    diagnosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)



if __name__=='__main__':
    main()
