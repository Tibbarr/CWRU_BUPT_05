# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:39:34 2020

@author: Hu Tong
"""

#STEP8 处理测试集数据

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
  



for i in range(142):

    number = str(i+1)
    params['path'] = r'C:\Users\huton\Desktop\week4\TF2\test2\original\TEST'+number+'.csv'
    params['opath'] = r'C:\Users\huton\Desktop\week4\TF2\test2\T600F7\TEST'+number+'.csv'

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
 