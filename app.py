import pickle
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
model = pickle.load(open(r'C:\\Users\\Nalla\\OneDrive\\Desktop\\miniproject\\blue.pkl', 'rb'))
app=Flask(__name__) 
@app.route('/')
def home():
     return render_template('index.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict() :
    MinOfUpperTRange= float(request.form['MinofupperTRange'])
    MaxOfLowerTRange= float(request.form['MaxOfLowerTRange'])
    MinOfLowerTRange= float(request.form['MinofLowerTRange'])
    AverageOfUpperTRange= float(request.form['AverageOfUpperTRange'])
    AverageRainingDays= float(request.form['AverageRainingDays'])
    AverageOfLowerTRange = float(request.form['AverageOfLowerTRange'])
    MaxOfUpperTRange= float(request.form['MaxOfUpperTRange'])
    Honeybees = float(request.form['Honeybees'])
    prediction =model.predict(pd.DataFrame([[AverageOfLowerTRange, AverageOfUpperTRange, AverageRainingDays, MaxOfLowerTRange,MinOfLowerTRange,MaxOfUpperTRange,MinOfUpperTRange,MaxOfUpperTRange,MaxOfUpperTRange,Honeybees]]))
    return render_template('predict.html', prediction_text ="{}".format(prediction))

# loading model which we saved
if __name__ == "__main__":
       app.run(debug=True)