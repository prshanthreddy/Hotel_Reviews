import pickle
from flask import Flask,request,app,render_template
import pandas as pd
import numpy as np

app=Flask(__name__)
# load the model
mlmodel=pickle.load(open('mlmodel.pickle','rb'))
vectorizer=pickle.load(open('vectorizer.pickle','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    if request.method=="POST":
        data=request.form['message']
        data=[data]
        new_data=vectorizer.transform(data).toarray()
        output=mlmodel.predict(new_data)
    return render_template('home.html',prediction=output)
    
if __name__=="__main__":
    app.run(debug=True)
