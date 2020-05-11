# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:44:01 2020

@author: Hu Tong
"""

# 处理训练集STEP2 - 规整第一次测试集的格式（之后会和训练集合并，增加用于训练的数据量）

# 批量删除RPM

import pandas as pd


# TEST
for i in range(14):
    if i<9:
        number = '0'+str(i+1)
        file = r'C:\Users\huton\Desktop\week4\TF2\test1\original\TEST'+number+'.csv'
        print(file)
        data = pd.read_csv(file)
        data_column=list(data.columns)
        newdata = data[[data_column[0],data_column[1],data_column[2]]]
        newdata.to_csv(r'C:\Users\huton\Desktop\week4\TF2\test1\DE_FE_BA\TEST'+number+'.csv',index=False,header=True)  
    else:
        number = str(i+1)
        file = r'C:\Users\huton\Desktop\week4\TF2\test1\original\TEST'+number+'.csv'
        print(file)
        data = pd.read_csv(file)
        data_column=list(data.columns)
        newdata = data[[data_column[0],data_column[1],data_column[2]]]
        newdata.to_csv(r'C:\Users\huton\Desktop\week4\TF2\test1\DE_FE_BA\TEST'+number+'.csv',index=False,header=True)  