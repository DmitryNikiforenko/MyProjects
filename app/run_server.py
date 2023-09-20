# -*- coding: utf-8 -*-
"""Работа с Flask"""

from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify
import pandas as pd
import dill
import numpy as np
import json

#загрузка модели
with open('/content/drive/MyDrive/XGBClass_pipeline.dill', 'rb') as in_strm:
  model = dill.load(in_strm)

#Запуск Flask

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/", methods=["GET"])
def general():
  return "Welcome to fraudelent prediction process"

@app.route("/predict", methods=["POST"])
def predict():
  data = {'success': False}

  request_json = request.get_json()

  gender, tartar, age, height_cm, triglyceride, hemoglobin, Gtp, dental_caries = '', '', '', '', '', '', '', ''

  if request_json["gender"]:
    gender = request_json["gender"]

  if request_json["tartar"]:
    tartar = request_json['tartar']

  if request_json["age"]:
    age = request_json['age']

  if request_json["height(cm)"]:
    height_cm = request_json['height(cm)']

  if request_json["triglyceride"]:
    triglyceride = request_json['triglyceride']

  if request_json["hemoglobin"]:
    hemoglobin = request_json['hemoglobin']

  if request_json["Gtp"]:
    Gtp = request_json['Gtp']

  if request_json["dental caries"]:
    dental_caries = request_json['dental caries']

  preds = model.predict_proba(pd.DataFrame({"gender": [i for i in gender],
                                          "tartar": [i for i in tartar],
                                          "age": [i for i in age],
                                          "height(cm)": [i for i in height_cm],
                                          "triglyceride": [i for i in triglyceride],
                                          "hemoglobin": [i for i in hemoglobin],
                                          "Gtp": [i for i in Gtp],
                                          "dental caries": [i for i in dental_caries]}))

  data['predictions'] = [str(i) for i in preds[:, 1]]
  data['success'] = True
  print('Ok')

  return jsonify(data)

if __name__ == '__main__':
  app.run()