# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:58:05 2020

@author: Hu Tong
"""

# STEP4 给训练集打标签并初步合并

import pandas as pd
import os

# 合并B
Folder_Path = r'C:\Users\huton\Desktop\week4\TF2\fea_train_T600F6_2\B'     # 文件夹路径
SaveFile_Path = r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_moremore'                   # 合并文件路径
SaveFile_Name = r'T600_W6_B.csv'                        # 合并文件名

os.chdir(Folder_Path)
file_list = os.listdir()

df = pd.read_csv(Folder_Path +'\\'+ file_list[0])
df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
df2['label'] = 1
df2.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False)

for i in range(1,len(file_list)):
    df = pd.read_csv(Folder_Path + '\\'+ file_list[i])
    df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
    df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()

    if 'NORMAL' == file_list[i][0]:
        df2['label'] = 1
    else:
        df2['label'] = 1

    df2.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False, header=False, mode='a+')


# 合并NORMAL
Folder_Path = r'C:\Users\huton\Desktop\week4\TF2\fea_train_T600F6_2\NORMAL'     # 文件夹路径
SaveFile_Path = r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_moremore'                   # 合并文件路径
SaveFile_Name = r'T600_W6_NORMAL.csv'                        # 合并文件名

os.chdir(Folder_Path)
file_list = os.listdir()

df = pd.read_csv(Folder_Path +'\\'+ file_list[0])
df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
df2['label'] = 0
df2.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False)

for i in range(1,len(file_list)):
    df = pd.read_csv(Folder_Path + '\\'+ file_list[i])
    df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
    df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()

    if 'OR' == file_list[i][0]:
        df2['label'] = 0
    else:
        df2['label'] = 0

    df2.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False, header=False, mode='a+')


# 合并IR
Folder_Path = r'C:\Users\huton\Desktop\week4\TF2\fea_train_T600F6_2\IR'     # 文件夹路径
SaveFile_Path = r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_moremore'                   # 合并文件路径
SaveFile_Name = r'T600_W6_IR.csv'                        # 合并文件名

os.chdir(Folder_Path)
file_list = os.listdir()

df = pd.read_csv(Folder_Path +'\\'+ file_list[0])
df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
df2['label'] = 3
df2.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False)

for i in range(1,len(file_list)):
    df = pd.read_csv(Folder_Path + '\\'+ file_list[i])
    df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
    df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()

    if 'IR' == file_list[i][0]:
        df2['label'] = 3
    else:
        df2['label'] = 3

    df2.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False, header=False, mode='a+')


# 合并OR
Folder_Path = r'C:\Users\huton\Desktop\week4\TF2\fea_train_T600F6_2\OR'     # 文件夹路径
SaveFile_Path = r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_moremore'                   # 合并文件路径
SaveFile_Name = r'T600_W6_OR.csv'                        # 合并文件名
os.chdir(Folder_Path)
file_list = os.listdir()

df = pd.read_csv(Folder_Path +'\\'+ file_list[0])
df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
df2['label'] = 2
df2.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False)

for i in range(1,len(file_list)):
    df = pd.read_csv(Folder_Path + '\\'+ file_list[i])
    df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
    df2 = df[['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()

    if 'IR' == file_list[i][0]:
        df2['label'] = 2
    else:
        df2['label'] = 2

    df2.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False, header=False, mode='a+')
    

# 合并为一个
# 合并

Folder_Path=r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_moremore'    #要拼接的文件夹及其完整路径，注意不要包含中文  
SaveFile_Path=r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_moremore'  #拼接后要保存的文件路径  
SaveFile_Name='T600_W6_train_all.csv'    #合并后要保存的文件名
        
os.chdir(Folder_Path)
file_list = os.listdir()

#读取第一个CSV文件并包含表头  
df = pd.read_csv(Folder_Path +'/'+ file_list[0],
                 encoding="utf8"
                 )  #编码默认UTF-8，若乱码自行更改

#将读取的第一个CSV文件写入合并后的文件保存  
df.to_csv(SaveFile_Path+'/'+ SaveFile_Name,
          encoding="utf8",
          index=False) 

#循环遍历列表中各个CSV文件名，并追加到合并后的文件  
FileStart = 1
FileEnd = len(file_list)
for i in range(FileStart,FileEnd):  
    df = pd.read_csv(Folder_Path + '/'+ file_list[i],encoding="utf8")  
    df.to_csv(SaveFile_Path+'/'+ SaveFile_Name,
              encoding="utf8",
              index=False, 
              header=False, 
              mode='a') #mode='a'表示追加写入的意思

## 合并TEST
#Folder_Path = r'C:\Users\huton\Desktop\week4\TF2\fea_test_T600F5'     # 文件夹路径
#SaveFile_Path = r'C:\Users\huton\Desktop\week4\TF2\fea_test_T600F5'                   # 合并文件路径
#SaveFile_Name = r'TEST_T600_W5_OR.csv'                        # 合并文件名
#os.chdir(Folder_Path)
#file_list = os.listdir()
#
#df = pd.read_csv(Folder_Path +'\\'+ file_list[0])
#df2 = df[['DE_time_cA5','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA5','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
#df2 = df[['DE_time_cA5','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA5','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
#df2['label'] = 2
#df2.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False)
#
#for i in range(1,len(file_list)):
#    df = pd.read_csv(Folder_Path + '\\'+ file_list[i])
#    df2 = df[['DE_time_cA5','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA5','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']]
#    df2 = df[['DE_time_cA5','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA5','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1']].copy()
#    
#    if 'IR' == file_list[i][0]:
#        df2['label'] = 2
#    else:
#        df2['label'] = 2
#
#    df2.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False, header=False, mode='a+')
#    
