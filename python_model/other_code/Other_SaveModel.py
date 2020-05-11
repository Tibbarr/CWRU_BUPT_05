# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:58:28 2020

@author: Hu Tong
"""

#OTHER 将模型保存为.model文件


from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
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


#时频域T600W6+test1最高分
params = {}
#666
params['n_estimators'] = 200
params['max_depth'] = 15
params['max_features'] = "auto"
params['min_samples_split'] = 2
params['min_samples_leaf'] = 1
params['average'] = None


params['train'] =r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_more\T600W6more_train.csv'
params['test'] = r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_more\T600W6more_test.csv'


argvs = sys.argv
try:
    for i in range(1):
        train = np.array(pd.read_csv(params['train']))
        train_y = train[:, -1]
        train_x = train[:, :-1]
    
        test = np.array(pd.read_csv(params['test']))
        test_y = test[:, -1]
        test_x = test[:, :-1]
    
        clf = RandomForestClassifier(n_estimators=params['n_estimators'],
                                 max_features=params['max_features'],
                                 max_depth=params['max_depth'],
                                 #max_leaf_nodes = 20,
                                 min_samples_split=params['min_samples_split'],
                                 min_samples_leaf=params['min_samples_leaf'],
                                 class_weight= {0:0.1, 1:0.3, 2:0.3, 3:0.3},
                                 #n_jobs = 5,
                                 ).fit(train_x, train_y)
                                
        joblib.dump(clf,r'C:\Users\huton\Desktop\RFfinalmodel.model')
        
        predict = clf.predict(test_x)
        precision = precision_score(test_y, predict,average='macro')
        recall = recall_score(test_y, predict,average='macro')
        accuracy = accuracy_score(test_y, predict)
        res = {}
        res['fMeasure'] = f1_score(test_y, predict,average='macro')
        res['precision'] = precision
        res['recall'] = recall
        res['accuracy'] = accuracy

        print(json.dumps(res))
except Exception as e:
    print(e)

#
##============================ 模型测试及输出 2 ==================================
#
#data_test = r'C:\Users\huton\Desktop\week4\TF2\test2\T600F6_filename\TEST_2_all.csv'
#data_test = np.array(pd.read_csv(data_test))
#data_test0 = data_test
#
#from sklearn.impute import SimpleImputer
#
#imp = SimpleImputer(missing_values=np.nan, strategy='mean')
#data_test1 = data_test[:, :-1]
#data_test = imp.fit_transform(data_test1)
#filename = data_test0[:,14] 
#predictions = clf.predict(data_test)
#
#output = pd.DataFrame({'label':predictions,'filename':filename})
#output.to_csv(r'C:\Users\huton\Desktop\week4\TF2\test2\T600F6_filename\TEST_2_all_resulttest8.csv',index = False)
#output.head()
### =============================================================================
