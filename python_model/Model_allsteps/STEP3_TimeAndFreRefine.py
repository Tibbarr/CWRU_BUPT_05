# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:46:58 2020

@author: Hu Tong
"""

# STEP3 - 特征提取
# 对规整之后的训练集和第一次测试集进行特征提取

import pandas as pd
import numpy as np
import pywt
import sys
import csv
from scipy import stats
from pywt import wavedec
import math

argvs = sys.argv

params = {}
params['len_piece']= 600
params['wave_layer']= 6
params['wave_win']=38*pow(2,params['wave_layer']-1)-1  

def  one_row(arr,label_mean):
    result_list = []
    arr_add=arr.loc[:,:]
    for j in range(int(params['wave_win']/params['len_piece'])):  
        arr_add =arr_add.append(arr,ignore_index=True)
    for i in arr_add.columns:    
        cD=wavedec(arr_add[i],'db10',level=params['wave_layer'])   
        for i in range(params['wave_layer']+1):
            ener_cD = np.square(cD[i]).sum()   
            list_para = [ener_cD]
            result_list.extend(list_para)
    list_label=[label_mean.mean()]
    result_list.extend(list_label)
    return result_list
  

# B
    
for i in range(6):
    number = '0'+str(i+1)
    params['path'] = r'C:\Users\huton\Desktop\week4\TF2\DE_FE_train2\B\B'+number+'.csv'
    params['opath'] = r'C:\Users\huton\Desktop\week4\TF2\fea_train_T600F6_2\B\B'+number+'_feature_T600_W6.csv'

    try:
        for i in range(len(argvs)):
            if i < 1:
                continue
            if argvs[i].split('=')[1] == 'None':
                params[argvs[i].split('=')[0]] = None
            else:
                Type = type(params[argvs[i].split('=')[0]])
                params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])
    
        with open(params['path'],'r') as f:
            reader = csv.reader(f)
            head_row=next(reader)
            head_label=head_row[-1]
            head_row=head_row[:-1]      
            head_label2=head_row[-1]
        data_head=[]
        head_out=[]
        for i in head_row:   
             head_out=[i+'_cA'+str(params['wave_layer'])]
             data_head.extend(head_out)
             for j in range(params['wave_layer']):
                    head_out=[i+'_cD'+str(params['wave_layer']-j)]
                    data_head.extend(head_out)
        headlabel_out=[head_label]
        data_head.extend(headlabel_out)
        data_out=[]
        data_out.append(data_head)
        df = pd.read_csv(params['path'])
        data=np.array(df)
        lenth=data[:,-1]
        lenth=len(np.array(lenth))
        i=1
        while i*params['len_piece']<lenth:
            arr_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,:head_label2]
            label_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,head_label]       
            i=i+1
            data_out.append(one_row(arr_pic,label_pic))
        if params['len_piece']>lenth:
            arr_pic=df.loc[:lenth,:head_label2]
            label_pic=df.loc[:lenth,head_label]
        else:
            arr_pic=df.loc[lenth-params['len_piece']:lenth,:head_label2]
            label_pic=df.loc[lenth-params['len_piece']:lenth,head_label]
        data_out.append(one_row(arr_pic,label_pic))
        wrtocsv = pd.DataFrame(data_out)
        wrtocsv.to_csv(params['opath'],index=False,header=False)
    except Exception as e:
        print(e)
        
# NORMAL
for i in range(2):
    number = '0'+str(i+1)
    params['path'] = r'C:\Users\huton\Desktop\week4\TF2\DE_FE_train2\NORMAL\NORMAL'+number+'.csv'
    params['opath'] = r'C:\Users\huton\Desktop\week4\TF2\fea_train_T600F6_2\NORMAL\NORMAL'+number+'_feature_T600_W6.csv'

    
    try:
        for i in range(len(argvs)):
            if i < 1:
                continue
            if argvs[i].split('=')[1] == 'None':
                params[argvs[i].split('=')[0]] = None
            else:
                Type = type(params[argvs[i].split('=')[0]])
                params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])
    
        with open(params['path'],'r') as f:
            reader = csv.reader(f)
            head_row=next(reader)
            head_label=head_row[-1]
            head_row=head_row[:-1]      
            head_label2=head_row[-1]
        data_head=[]
        head_out=[]
        for i in head_row:   
             head_out=[i+'_cA'+str(params['wave_layer'])]
             data_head.extend(head_out)
             for j in range(params['wave_layer']):
                    head_out=[i+'_cD'+str(params['wave_layer']-j)]
                    data_head.extend(head_out)
        headlabel_out=[head_label]
        data_head.extend(headlabel_out)
        data_out=[]
        data_out.append(data_head)
        df = pd.read_csv(params['path'])
        data=np.array(df)
        lenth=data[:,-1]
        lenth=len(np.array(lenth))
        i=1
        while i*params['len_piece']<lenth:
            arr_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,:head_label2]
            label_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,head_label]       
            i=i+1
            data_out.append(one_row(arr_pic,label_pic))
        if params['len_piece']>lenth:
            arr_pic=df.loc[:lenth,:head_label2]
            label_pic=df.loc[:lenth,head_label]
        else:
            arr_pic=df.loc[lenth-params['len_piece']:lenth,:head_label2]
            label_pic=df.loc[lenth-params['len_piece']:lenth,head_label]
        data_out.append(one_row(arr_pic,label_pic))
        wrtocsv = pd.DataFrame(data_out)
        wrtocsv.to_csv(params['opath'],index=False,header=False)
    except Exception as e:
        print(e)
        
# IR
for i in range(6):
    number = '0'+str(i+1)
    params['path'] = r'C:\Users\huton\Desktop\week4\TF2\DE_FE_train2\IR\IR'+number+'.csv'
    params['opath'] = r'C:\Users\huton\Desktop\week4\TF2\fea_train_T600F6_2\IR\IR'+number+'_feature_T600_W6.csv'


    try:
        for i in range(len(argvs)):
            if i < 1:
                continue
            if argvs[i].split('=')[1] == 'None':
                params[argvs[i].split('=')[0]] = None
            else:
                Type = type(params[argvs[i].split('=')[0]])
                params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])
    
        with open(params['path'],'r') as f:
            reader = csv.reader(f)
            head_row=next(reader)
            head_label=head_row[-1]
            head_row=head_row[:-1]      
            head_label2=head_row[-1]
        data_head=[]
        head_out=[]
        for i in head_row:   
             head_out=[i+'_cA'+str(params['wave_layer'])]
             data_head.extend(head_out)
             for j in range(params['wave_layer']):
                    head_out=[i+'_cD'+str(params['wave_layer']-j)]
                    data_head.extend(head_out)
        headlabel_out=[head_label]
        data_head.extend(headlabel_out)
        data_out=[]
        data_out.append(data_head)
        df = pd.read_csv(params['path'])
        data=np.array(df)
        lenth=data[:,-1]
        lenth=len(np.array(lenth))
        i=1
        while i*params['len_piece']<lenth:
            arr_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,:head_label2]
            label_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,head_label]       
            i=i+1
            data_out.append(one_row(arr_pic,label_pic))
        if params['len_piece']>lenth:
            arr_pic=df.loc[:lenth,:head_label2]
            label_pic=df.loc[:lenth,head_label]
        else:
            arr_pic=df.loc[lenth-params['len_piece']:lenth,:head_label2]
            label_pic=df.loc[lenth-params['len_piece']:lenth,head_label]
        data_out.append(one_row(arr_pic,label_pic))
        wrtocsv = pd.DataFrame(data_out)
        wrtocsv.to_csv(params['opath'],index=False,header=False)
    except Exception as e:
        print(e)
 
# OR
for i in range(14):
    if i<9:
        number = '0'+str(i+1)
        params['path'] = r'C:\Users\huton\Desktop\week4\TF2\DE_FE_train2\OR\OR'+number+'.csv'
        params['opath'] = r'C:\Users\huton\Desktop\week4\TF2\fea_train_T600F6\OR\OR'+number+'_feature_T600_W6.csv'

    try:
        for i in range(len(argvs)):
            if i < 1:
                continue
            if argvs[i].split('=')[1] == 'None':
                params[argvs[i].split('=')[0]] = None
            else:
                Type = type(params[argvs[i].split('=')[0]])
                params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])
    
        with open(params['path'],'r') as f:
            reader = csv.reader(f)
            head_row=next(reader)
            head_label=head_row[-1]
            head_row=head_row[:-1]      
            head_label2=head_row[-1]
        data_head=[]
        head_out=[]
        for i in head_row:   
             head_out=[i+'_cA'+str(params['wave_layer'])]
             data_head.extend(head_out)
             for j in range(params['wave_layer']):
                    head_out=[i+'_cD'+str(params['wave_layer']-j)]
                    data_head.extend(head_out)
        headlabel_out=[head_label]
        data_head.extend(headlabel_out)
        data_out=[]
        data_out.append(data_head)
        df = pd.read_csv(params['path'])
        data=np.array(df)
        lenth=data[:,-1]
        lenth=len(np.array(lenth))
        i=1
        while i*params['len_piece']<lenth:
            arr_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,:head_label2]
            label_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,head_label]       
            i=i+1
            data_out.append(one_row(arr_pic,label_pic))
        if params['len_piece']>lenth:
            arr_pic=df.loc[:lenth,:head_label2]
            label_pic=df.loc[:lenth,head_label]
        else:
            arr_pic=df.loc[lenth-params['len_piece']:lenth,:head_label2]
            label_pic=df.loc[lenth-params['len_piece']:lenth,head_label]
        data_out.append(one_row(arr_pic,label_pic))
        wrtocsv = pd.DataFrame(data_out)
        wrtocsv.to_csv(params['opath'],index=False,header=False)
    except Exception as e:
        print(e)

for i in range(5):
    number = str(i+10)
    params['path'] = r'C:\Users\huton\Desktop\week4\TF2\DE_FE_train2\OR\OR'+number+'.csv'
    params['opath'] = r'C:\Users\huton\Desktop\week4\TF2\fea_train_T600F6_2\OR\OR'+number+'_feature_T600_W6.csv'

    try:
        for i in range(len(argvs)):
            if i < 1:
                continue
            if argvs[i].split('=')[1] == 'None':
                params[argvs[i].split('=')[0]] = None
            else:
                Type = type(params[argvs[i].split('=')[0]])
                params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])
    
        with open(params['path'],'r') as f:
            reader = csv.reader(f)
            head_row=next(reader)
            head_label=head_row[-1]
            head_row=head_row[:-1]      
            head_label2=head_row[-1]
        data_head=[]
        head_out=[]
        for i in head_row:   
             head_out=[i+'_cA'+str(params['wave_layer'])]
             data_head.extend(head_out)
             for j in range(params['wave_layer']):
                    head_out=[i+'_cD'+str(params['wave_layer']-j)]
                    data_head.extend(head_out)
        headlabel_out=[head_label]
        data_head.extend(headlabel_out)
        data_out=[]
        data_out.append(data_head)
        df = pd.read_csv(params['path'])
        data=np.array(df)
        lenth=data[:,-1]
        lenth=len(np.array(lenth))
        i=1
        while i*params['len_piece']<lenth:
            arr_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,:head_label2]
            label_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,head_label]       
            i=i+1
            data_out.append(one_row(arr_pic,label_pic))
        if params['len_piece']>lenth:
            arr_pic=df.loc[:lenth,:head_label2]
            label_pic=df.loc[:lenth,head_label]
        else:
            arr_pic=df.loc[lenth-params['len_piece']:lenth,:head_label2]
            label_pic=df.loc[lenth-params['len_piece']:lenth,head_label]
        data_out.append(one_row(arr_pic,label_pic))
        wrtocsv = pd.DataFrame(data_out)
        wrtocsv.to_csv(params['opath'],index=False,header=False)
    except Exception as e:
        print(e)
        
#
## ================= test =====================
#for i in range(14):
#    if i<9:
#        number = '0'+str(i+1)
#        params['path'] = r'C:\Users\huton\Desktop\week4\TF2\test1\DE_FE_BA\TEST'+number+'.csv'
#        params['opath'] = r'C:\Users\huton\Desktop\week4\TF2\test1\T600_W7\TEST'+number+'.csv'
#
#    try:
#        for i in range(len(argvs)):
#            if i < 1:
#                continue
#            if argvs[i].split('=')[1] == 'None':
#                params[argvs[i].split('=')[0]] = None
#            else:
#                Type = type(params[argvs[i].split('=')[0]])
#                params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])
#    
#        with open(params['path'],'r') as f:
#            reader = csv.reader(f)
#            head_row=next(reader)
#            head_label=head_row[-1]
#            head_row=head_row[:-1]      
#            head_label2=head_row[-1]
#        data_head=[]
#        head_out=[]
#        for i in head_row:   
#             head_out=[i+'_cA'+str(params['wave_layer'])]
#             data_head.extend(head_out)
#             for j in range(params['wave_layer']):
#                    head_out=[i+'_cD'+str(params['wave_layer']-j)]
#                    data_head.extend(head_out)
#        headlabel_out=[head_label]
#        data_head.extend(headlabel_out)
#        data_out=[]
#        data_out.append(data_head)
#        df = pd.read_csv(params['path'])
#        data=np.array(df)
#        lenth=data[:,-1]
#        lenth=len(np.array(lenth))
#        i=1
#        while i*params['len_piece']<lenth:
#            arr_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,:head_label2]
#            label_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,head_label]       
#            i=i+1
#            data_out.append(one_row(arr_pic,label_pic))
#        if params['len_piece']>lenth:
#            arr_pic=df.loc[:lenth,:head_label2]
#            label_pic=df.loc[:lenth,head_label]
#        else:
#            arr_pic=df.loc[lenth-params['len_piece']:lenth,:head_label2]
#            label_pic=df.loc[lenth-params['len_piece']:lenth,head_label]
#        data_out.append(one_row(arr_pic,label_pic))
#        wrtocsv = pd.DataFrame(data_out)
#        wrtocsv.to_csv(params['opath'],index=False,header=False)
#    except Exception as e:
#        print(e)
#
#for i in range(5):
#    number = str(i+10)
#    params['path'] = r'C:\Users\huton\Desktop\week4\TF2\test1\DE_FE_BA\TEST'+number+'.csv'
#    params['opath'] = r'C:\Users\huton\Desktop\week4\TF2\test1\T600_W7\TEST'+number+'.csv'
#
#    try:
#        for i in range(len(argvs)):
#            if i < 1:
#                continue
#            if argvs[i].split('=')[1] == 'None':
#                params[argvs[i].split('=')[0]] = None
#            else:
#                Type = type(params[argvs[i].split('=')[0]])
#                params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])
#    
#        with open(params['path'],'r') as f:
#            reader = csv.reader(f)
#            head_row=next(reader)
#            head_label=head_row[-1]
#            head_row=head_row[:-1]      
#            head_label2=head_row[-1]
#        data_head=[]
#        head_out=[]
#        for i in head_row:   
#             head_out=[i+'_cA'+str(params['wave_layer'])]
#             data_head.extend(head_out)
#             for j in range(params['wave_layer']):
#                    head_out=[i+'_cD'+str(params['wave_layer']-j)]
#                    data_head.extend(head_out)
#        headlabel_out=[head_label]
#        data_head.extend(headlabel_out)
#        data_out=[]
#        data_out.append(data_head)
#        df = pd.read_csv(params['path'])
#        data=np.array(df)
#        lenth=data[:,-1]
#        lenth=len(np.array(lenth))
#        i=1
#        while i*params['len_piece']<lenth:
#            arr_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,:head_label2]
#            label_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,head_label]       
#            i=i+1
#            data_out.append(one_row(arr_pic,label_pic))
#        if params['len_piece']>lenth:
#            arr_pic=df.loc[:lenth,:head_label2]
#            label_pic=df.loc[:lenth,head_label]
#        else:
#            arr_pic=df.loc[lenth-params['len_piece']:lenth,:head_label2]
#            label_pic=df.loc[lenth-params['len_piece']:lenth,head_label]
#        data_out.append(one_row(arr_pic,label_pic))
#        wrtocsv = pd.DataFrame(data_out)
#        wrtocsv.to_csv(params['opath'],index=False,header=False)
#    except Exception as e:
#        print(e)
        
#====================处理单独的文件================
#        
#number = '0'+str(i+1)
#params['path'] = r'C:\Users\huton\Desktop\TEST08.csv'
#params['opath'] = r'C:\Users\huton\Desktop\TEST081.csv'
#
#
#
#try:
#    for i in range(len(argvs)):
#        if i < 1:
#            continue
#        if argvs[i].split('=')[1] == 'None':
#            params[argvs[i].split('=')[0]] = None
#        else:
#            Type = type(params[argvs[i].split('=')[0]])
#            params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])
#
#    with open(params['path'],'r') as f:
#        reader = csv.reader(f)
#        head_row=next(reader)
#        head_label=head_row[-1]
#        head_row=head_row[:-1]      
#        head_label2=head_row[-1]
#    data_head=[]
#    head_out=[]
#    for i in head_row:   
#         head_out=[i+'_cA'+str(params['wave_layer'])]
#         data_head.extend(head_out)
#         for j in range(params['wave_layer']):
#                head_out=[i+'_cD'+str(params['wave_layer']-j)]
#                data_head.extend(head_out)
#    headlabel_out=[head_label]
#    data_head.extend(headlabel_out)
#    data_out=[]
#    data_out.append(data_head)
#    df = pd.read_csv(params['path'])
#    data=np.array(df)
#    lenth=data[:,-1]
#    lenth=len(np.array(lenth))
#    i=1
#    while i*params['len_piece']<lenth:
#        arr_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,:head_label2]
#        label_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,head_label]       
#        i=i+1
#        data_out.append(one_row(arr_pic,label_pic))
#    if params['len_piece']>lenth:
#        arr_pic=df.loc[:lenth,:head_label2]
#        label_pic=df.loc[:lenth,head_label]
#    else:
#        arr_pic=df.loc[lenth-params['len_piece']:lenth,:head_label2]
#        label_pic=df.loc[lenth-params['len_piece']:lenth,head_label]
#    data_out.append(one_row(arr_pic,label_pic))
#    wrtocsv = pd.DataFrame(data_out)
#    wrtocsv.to_csv(params['opath'],index=False,header=False)
#except Exception as e:
#    print(e)