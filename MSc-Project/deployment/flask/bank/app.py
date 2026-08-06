from flask import Flask, render_template, request,jsonify
import pandas as pd
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
model_columns = pickle.load(open('model_columns.pkl', 'rb'))
@app.route('/', methods=['GET','POST'])

def Home():
    return render_template('index.html')
    
    
scaler = MinMaxScaler()
@app.route('/predict',methods=['POST'])    
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        job = request.form['job']
        marital = request.form['marital']
        education = request.form['education']
        default = request.form['default']
        balance = float(request.form['balance'])
        housing = request.form['housing']
        loan = request.form['loan']
        contact = request.form['contact'] 
        day = int(request.form['day'])
        campaign = int(request.form['campaign'])
        pdays = int(request.form['pdays'])
        previous = int(request.form['previous'])
        poutcome = request.form['poutcome']          
 
        cols_names = ['age','job','marital','education','default','balance','housing','loan','contact','day','campaign','pdays','previous','poutcome']
        col_vals = [[age, job, marital, education, default, balance, housing, loan, contact, day, campaign, pdays, previous, poutcome]]
        df = pd.DataFrame(col_vals, columns = cols_names)
        df = pd.get_dummies(data=df, columns = ['marital','contact','job', 'education','poutcome'])
        df = df.reindex(columns=model_columns, fill_value=0)
        cols = ['default','housing','loan']
        for col in cols:
            df[col].replace({'yes': 1,'no': 0},inplace=True)
            
        scale_cols = ['age','balance','pdays','previous','day','campaign']
        df[scale_cols] = scaler.fit_transform(df[scale_cols])

        prediction = model.predict(df)

        if prediction==1:
             return render_template('index.html',prediction_text="The Customer will leave the bank")
        else:
             return render_template('index.html',prediction_text="The Customer will not leave the bank")
                
if __name__=="__main__":
    app.run(debug=True) 
