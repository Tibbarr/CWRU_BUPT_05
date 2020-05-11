# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:24:20 2020

@author: Hu Tong
"""

# STEP7 划分train和test

#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
import numpy as np
import sys
import pandas as pd

data = pd.read_csv(r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_moremoremore\T600W6more.csv')

# 将矩阵最后一列之前的数值给x（输入数据），将矩阵最后一列的数值给y（标签）
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2,random_state=0)

# np.column_stack将两个矩阵进行组合连接
train= np.column_stack((x_train,y_train))
test = np.column_stack((x_test, y_test))

# numpy.savetxt 将txt文件保存为.csv结尾的文件
np.savetxt(r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_moremoremore\T600W6more_train.csv',train, delimiter = ',')
np.savetxt(r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_moremoremore\T600W6more_test.csv', test, delimiter = ',')