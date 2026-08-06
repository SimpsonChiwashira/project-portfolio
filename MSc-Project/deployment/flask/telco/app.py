from flask import Flask, render_template, request,jsonify
import pandas as pd
import requests
import pickle
import numpy as np
from sklearn import metrics
import sklearn
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)
model = pickle.load(open('rf_clf_telco.pkl', 'rb'))
model_columns = pickle.load(open('rf_columns_telco.pkl', 'rb'))
@app.route('/', methods=['GET','POST'])

def Home():
    return render_template('index.html')
    
    
scaler = MinMaxScaler()
@app.route('/predict',methods=['POST'])    
def predict():
    if request.method == 'POST':
        gender = int(request.form['gender'])
        SeniorCitizen = int(request.form['SeniorCitizen'])
        Partner = int(request.form['Partner'])
        Dependents = int(request.form['Dependents'])
        tenure = int(request.form['tenure'])
        PhoneService = int(request.form['PhoneService'])
        MultipleLines = int(request.form['MultipleLines'])
        InternetService = request.form['InternetService']
        OnlineSecurity = int(request.form['OnlineSecurity']) 
        OnlineBackup = int(request.form['OnlineBackup'])
        DeviceProtection = int(request.form['DeviceProtection'])
        TechSupport = int(request.form['TechSupport'])
        StreamingTV = int(request.form['StreamingTV'])
        StreamingMovies = int(request.form['StreamingMovies'])
        Contract = request.form['Contract']
        PaperlessBilling = int(request.form['PaperlessBilling'])
        PaymentMethod = request.form['PaymentMethod']
        MonthlyCharges = float(request.form['MonthlyCharges'])
        TotalCharges = float(request.form['TotalCharges'])          
 
        #cols_names = ['age','job','marital','education','default','balance','housing','loan','contact','day','campaign','pdays','previous','poutcome']
        col_vals = [[gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges]]
        cols_names = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']

        df = pd.DataFrame(col_vals, columns = cols_names)
        #df = pd.DataFrame(col_vals)
        #df = pd.get_dummies(data=df, columns = ['marital','contact','job', 'education','poutcome'])
        df = pd.get_dummies(data=df, columns=['InternetService','Contract','PaymentMethod'])
        df = df.reindex(columns=model_columns, fill_value=0)

        prediction = model.predict(df)
        probablity = model.predict_proba(df)
        if prediction==1:
             return render_template('index.html',prediction_text="The Customer will leave! Confidence Level {}".format(np.round(probablity*100)))
        else:
             return render_template('index.html',prediction_text="The Customer will not leave! Confidence Level {}".format(np.round(probablity*100)))
                
if __name__=="__main__":
    app.run(debug=True) 
