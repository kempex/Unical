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
    else:
      return 'The person is diabetic'
     
def main():
    hide_streamlit_style = """ <style> #MainMenu {visibility: hidden;} .viewerBadge_container__r5tak styles_viewerBadge__CvC9N {visibility: hidden;} </style> """
    hide_streamlit_style2 = """
           <style>
            #MainMenu {visibility: hidden;}
            footer {
	
	visibility: hidden;
	
	}
footer:after {
	content:'goodbye'; 
	visibility: visible;
	display: block;
	position: relative;
	#background-color: red;
	padding: 5px;
	top: 2px;
}
            </style>
            """
	
    # giving title
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.markdown(hide_streamlit_style2, unsafe_allow_html=True)
    st.subheader('Diabetes Diagnostics System')
    st.image("logo2.jpeg",width=100)
    #getting the input data from the user
    #age = st.slider('How old are you?', 0, 130, 25)
    Pregnancies = st.number_input('Number of Pregnancy-->(Between 1 - 10)', value=0)
    Glucose = st.number_input('Glucose Level  -->(Without diabetes is 70 to 99 mg/dL)', value=70)
    BloodPressure = st.number_input('Blood Pressure Value  -->(Between 60 - 99)', value=80)
    SkinThickness = st.number_input('Skin Thickness Value  -->(1.60 mm to 25.45 mm in males, whereas 3.40 mm to 25.20 mm in females)', value=1.6)
    Insulin = st.number_input('Insulin Level  -->(Between 0 to 876 mIU/L)', value=5)
    BMI = st.number_input('BMI value  -->(below 18.5 for underweight and 30 or over for obese range)', value=18)
    DiabetesPedigreeFunction  = st.number_input('Diabetes Pedigree Function value -->(Between ranges of 0.08 to 2.42)', value=0)
    Age  = st.number_input('Age -->(Between ranges of 20 to 130)', value=30)
    #code for prediction 
    diagnosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
   # st.image("logo.png",width=200)
    st.success(diagnosis)



if __name__=='__main__':
    main()
