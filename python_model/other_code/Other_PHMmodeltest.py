# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:54:19 2020

@author: Hu Tong
"""

# 上传到平台的测试文件

import numpy as np
import pandas as pd
import sys
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
import json
import joblib

class Result:
    precision = 0
    recall = 0
    accuracy = 0
    rocX = []
    rocY = []
    featureImportances = []

params = {}
params['model'] = r'C:\Users\huton\Desktop\RFfinalmodel.model'
params['test'] = r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_more\T600W6more_test.csv'
argvs = sys.argv

try:
    for i in range(len(argvs)):
        if i < 1:
            continue
        if argvs[i].split('=')[1] == 'None':
            params[argvs[i].split('=')[0]] = None
        else:
            Type = type(params[argvs[i].split('=')[0]])
            params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])

    model = joblib.load(params['model'])    
    test_csv = pd.read_csv(params['test'])
    test_feature = test_csv.drop(['label'], axis=1)
    y_pred = model.predict_proba(test_feature)
    y_pred = model.predict(test_feature)
    


    predict = model.predict(test_feature)
    
#    precision = precision_score(test_csv, y_pred ,average='macro')
#    recall = recall_score(test_csv, y_pred ,average='macro')
#    accuracy = accuracy_score(test_csv, y_pred)
    
#    res = {}
#    res['fMeasure'] = f1_score(test_csv, y_pred ,average='macro')   
#    res['precision'] = precision
#    res['recall'] = recall
#    res['accuracy'] = accuracy
    
#    print(json.dumps(res))
except Exception as e:
    print(e)