import streamlit as st 
import pickle
import pandas as pd
import numpy as np
st.title("Welcome to Hotel Review Prediction App")
st.header("Enter the  review below, We will predict whether it is authentic or fake")
review = st.text_area("Review")
mlmodel=pickle.load(open('mlmodel.pickle','rb'))
vectorizer=pickle.load(open('vectorizer.pickle','rb'))
data=pd.read_csv("Exaggeration in fake vs. authentic online reviews for luxury and budget hotels .csv")
if st.button("Predict"):
    if review == "":
        st.warning("Please enter a review")
    else:
        data=[review]
        new_data=vectorizer.transform(data).toarray()
        output=mlmodel.predict(new_data)
        if output[0]=='truth':
            st.success("This review is authentic")
        else:
            st.error("This review is fake")
st.warning("The accuracy of the model is 0.97")
st.write("This app is made by Prashanth Reddy")
st.write("You can connect me on LinkedIn:  https://www.linkedin.com/in/prashanthreddy07/")
