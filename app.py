import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd



app = Flask(__name__)

XGmodel = pickle.load(open('xgboost.pkl','rb'))

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/predict_api',method = ['POST'])
def predict_api():
    data = request.json['data']
    print(data)

      