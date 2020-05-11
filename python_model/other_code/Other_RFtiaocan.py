# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:02:15 2020

@author: Hu Tong
"""
# OTHER 随机森林调参

from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import matplotlib.pylab as plt
import sys
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score


class Result:
    precision = 0
    recall = 0
    accuracy = 0
    rocX = []
    rocY = []
    featureImportances = []
params = {}
params['n_estimators'] = 60
params['max_depth'] = 4
params['max_features'] = "auto"
params['min_samples_split'] = 16
params['min_samples_leaf'] = 2
params['average'] = None

#params['train'] =r'C:\Users\huton\Desktop\week4\traintime\feature_600\separate_feature_600_train.csv'
#params['test'] = r'C:\Users\huton\Desktop\week4\traintime\feature_600\separate_feature_600_test.csv'
#
#params['train'] =r'C:\Users\huton\Desktop\week4\traintime\feature_600_addtest1\Time_600_train.csv'
#params['test'] = r'C:\Users\huton\Desktop\week4\traintime\feature_600_addtest1\Time_600_test.csv.csv'


params['train'] =r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6\T600_W6_train_all_train.csv'
params['test'] = r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6\T600_W6_train_all_test.csv'

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

    train = np.array(pd.read_csv(params['train']))
    train_y = train[:, -1]
    train_x = train[:, :-1]

    test = np.array(pd.read_csv(params['test']))
    test_y = test[:, -1]
    test_x = test[:, :-1]

## =============================================================================
#    param_test1 = {'n_estimators':range(10,1000,10)}
#    gsearch1 = GridSearchCV(estimator = RandomForestClassifier(min_samples_split=30,
#                                  min_samples_leaf=10,max_depth=13,max_features='sqrt'), 
#                                  param_grid = param_test1,cv=5,verbose=1,n_jobs=-1)
#    grid_result = gsearch1.fit(test_x,test_y)
#    
#    print('Best:%f using %s'%(grid_result.best_score_,gsearch1.best_params_))
### =============================================================================
    
# =============================================================================
# 
#    param_test2 = {'max_depth':range(2,20,2), 'min_samples_split':range(2,30,2)}
#    gsearch2 = GridSearchCV(estimator = RandomForestClassifier(n_estimators= 210, 
#            min_samples_leaf=10,max_features='sqrt' ,oob_score=True, random_state=10),
#    param_grid = param_test2,iid=False, cv=5)
#     
#    grid_result = gsearch2.fit(test_x,test_y)
#    print('Best:%f using %s'%(grid_result.best_score_,gsearch2.best_params_))
## =============================================================================

# =============================================================================
    param_test3 = {'min_samples_split':range(2,30,2), 'min_samples_leaf':(2,30,2)}
    gsearch3 = GridSearchCV(estimator = RandomForestClassifier(n_estimators= 210, max_depth=4,
                                     max_features='sqrt' ,oob_score=True, random_state=10),
                                     param_grid = param_test3,iid=False, cv=5)
    grid_result = gsearch3.fit(test_x,test_y)
       
    print('Best:%f using %s'%(grid_result.best_score_,gsearch3.best_params_))
 
# =============================================================================

    means = grid_result.cv_results_['mean_test_score']
    params = grid_result.cv_results_['params']
    for  mean,param in zip(means,params):
        print("%f with: %r" % (mean,param))
except Exception as e:
    print(e)
