# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:00:04 2020

@author: Tibbarr
"""

# STEP5 给第一次的训练集打标签

import pandas as pd
import os


SaveFile_Path = r'C:\Users\huton\Desktop\week4\TF2\test1\T600_W6\labeled'   # 保存路径

for i in range(14):
    if i<9:
        number = '0'+str(i+1)
        file = r'C:\Users\huton\Desktop\week4\TF2\test1\T600_W6\TEST'+number+'.csv'     # 文件路径
        ofile = r'C:\Users\huton\Desktop\week4\TF2\test1\T600_W6\labeled\TEST'+number+'.csv'     # 文件路径

        filename = os.path.basename(r'C:\Users\huton\Desktop\week4\TF2\test1\T600_W6\labeled\TEST'+number+'.csv')
        if '01' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2['label'] = 1
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)
        elif '02' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2['label'] = 1
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)
        elif '03' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2['label'] = 3
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)
        elif '04' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)
        elif '05' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2['label'] = 2
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)
        elif '06' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)
        elif '07' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2['label'] = 2
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)
        elif '08' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2['label'] = 0
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)
        elif '09' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2['label'] = 2
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)
            
        
    else:
        number = str(i+1)
        file = r'C:\Users\huton\Desktop\week4\TF2\test1\T600_W6\TEST'+number+'.csv'     # 文件路径
        ofile = r'C:\Users\huton\Desktop\week4\TF2\test1\T600_W6\labeled\TEST'+number+'.csv'     # 文件路径

        filename = os.path.basename(r'C:\Users\huton\Desktop\week4\TF2\test1\T600_W6\labeled\TEST'+number+'.csv')
        if '10' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2['label'] = 2
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)
        elif '11' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2['label'] = 2
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)
        elif '12' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2['label'] = 3
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)
        elif '14' in filename:
            print('true')
            df = pd.read_csv(file)
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
            df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
            df2['label'] = 1
            df2.to_csv(ofile, encoding="utf_8_sig",index=False)