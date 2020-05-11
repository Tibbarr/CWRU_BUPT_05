# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:40:25 2020

@author: Hu Tong
"""

# 处理训练集STEP1 - 规整格式
# 保留前三列

import pandas as pd

# B
for i in range(6):
    number = '0'+str(i+1)
    file = r'C:\Users\huton\Desktop\week4\time_train_test1\original\B\B'+number+'.csv'
    print(file)
    data = pd.read_csv(file)
    data_column=list(data.columns)
    newdata = data[[data_column[0],data_column[1],data_column[2]]]
    newdata.to_csv(r'C:\Users\huton\Desktop\week4\time_train_test1\DE_FE_train\B\B'+number+'.csv',index=False,header=True)  

# NORMAL
for i in range(2):
    number = '0'+str(i+1)
    file = r'C:\Users\huton\Desktop\week4\time_train_test1\original\NORMAL\NORMAL'+number+'.csv'
    print(file)
    data = pd.read_csv(file)
    data_column=list(data.columns)
    newdata = data[[data_column[0],data_column[1],data_column[2]]]
    newdata.to_csv(r'C:\Users\huton\Desktop\week4\time_train_test1\DE_FE_train\NORMAL\NORMAL'+number+'.csv',index=False,header=True)  


# IR
for i in range(6):
    number = '0'+str(i+1)
    file = r'C:\Users\huton\Desktop\week4\time_train_test1\original\IR\IR'+number+'.csv'
    print(file)
    data = pd.read_csv(file)
    data_column=list(data.columns)
    newdata = data[[data_column[0],data_column[1],data_column[2]]]
    newdata.to_csv(r'C:\Users\huton\Desktop\week4\time_train_test1\DE_FE_train\IR\IR'+number+'.csv',index=False,header=True)  


# OR
for i in range(14):
    if i<9:
        number = '0'+str(i+1)
        file = r'C:\Users\huton\Desktop\week4\time_train_test1\original\OR\OR'+number+'.csv'
        print(file)
        data = pd.read_csv(file)
        data_column=list(data.columns)
        newdata = data[[data_column[0],data_column[1],data_column[2]]]
        newdata.to_csv(r'C:\Users\huton\Desktop\week4\time_train_test1\DE_FE_train\OR\OR'+number+'.csv',index=False,header=True)  
    else:
        number = str(i+1)
        file = r'C:\Users\huton\Desktop\week4\time_train_test1\original\OR\OR'+number+'.csv'
        print(file)
        data = pd.read_csv(file)
        data_column=list(data.columns)
        newdata = data[[data_column[0],data_column[1]]]
        newdata.to_csv(r'C:\Users\huton\Desktop\week4\time_train_test1\DE_FE_train\OR\OR'+number+'.csv',index=False,header=True)  