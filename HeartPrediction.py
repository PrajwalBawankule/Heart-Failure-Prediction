import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/Acer/Documents/SEM 7/ML/heartfailure/trained_model.sav', 'rb'))

def diabetes_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==1):
        return('The person will have heart failure')
    else:
        return('The person will not have heart failure')


def main():
#giving a title
    st.title('Heart Failure Prediction Web App')
#getting the input data from the user
    age = st.text_input('Enter age: ')
    sex = st.text_input('Enter sex: ')
    cp = st.text_input('Enter chest pain type: ')
    trestbps= st.text_input('Enter rest BP: ')
    chol= st.text_input('Enter Cholesterol: ')
    fbs= st.text_input('Enter FBS over 120: ')
    restecg= st.text_input('Enter ECG Result: ')
    thalach = st.text_input('Enter max heart rate: ')
    exang= st.text_input('Enter exercise angina: ')
    oldpeak= st.text_input('Enter ST Depression: ')
    slope= st.text_input('Enter slope of ST: ')
    ca= st.text_input('Enter number vessels fluro: ')
    thal= st.text_input('Enter thallium: ')

# code for Prediction
    diagnosis =''
#creating a button for Prediction
    if st.button('Predict Heart Failure'):
        diagnosis = diabetes_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    st.success(diagnosis)

if __name__ == '__main__':
    main()