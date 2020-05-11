# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:44:00 2020

@author: Hu Tong
"""


#STEP9 给test2添加文件名

import pandas as pd
import os

for i in range(142):

    number = str(i+1)    
    file = r'C:\Users\huton\Desktop\week4\TF2\test2\T600F7\TEST'+number+'.csv'
    
    data = pd.read_csv(file)
    data_column=list(data.columns)
    #newdata = data[[data_column[0],data_column[1],data_column[2],data_column[3],data_column[4],data_column[5],data_column[6],data_column[7],data_column[8],data_column[9],data_column[10],data_column[11]]]
    newdata = data[[data_column[0],data_column[1],data_column[2],data_column[3],data_column[4],data_column[5],data_column[6],data_column[7],data_column[8],data_column[9],data_column[10],data_column[11],data_column[12],data_column[13]]]
    #newdata = data[[data_column[0],data_column[1],data_column[2],data_column[3],data_column[4],data_column[5],data_column[6],data_column[7],data_column[8],data_column[9],data_column[10],data_column[11],data_column[12],data_column[13],data_column[14],data_column[15]]]
    
    filename = os.path.basename(r'C:\Users\huton\Desktop\week4\TF2\test2\T600F7\TEST'+number+'.csv')
    print(filename)
    if i < 9 :
        newfilename = filename[0:5]
        print(newfilename)
    elif i < 99:
        newfilename = filename[0:6]
        print(newfilename)
    else:
        newfilename = filename[0:7]
        print(newfilename)
        
    newdata['filename']= newfilename
    newdata.to_csv(r'C:\Users\huton\Desktop\week4\TF2\test2\T600F7_filename\TEST'+number+'.csv',
              columns=['DE_time_cA6','DE_time_cD6','DE_time_cD5','DE_time_cD4','DE_time_cD3','DE_time_cD2','DE_time_cD1','FE_time_cA6','FE_time_cD6','FE_time_cD5','FE_time_cD4','FE_time_cD3','FE_time_cD2','FE_time_cD1','filename'],index=0,header=1)

 
# 合并

Folder_Path=r'C:\Users\huton\Desktop\week4\TF2\test2\T600F7_filename'    #要拼接的文件夹及其完整路径，注意不要包含中文  
SaveFile_Path=r'C:\Users\huton\Desktop\week4\TF2\test2\T600F7_filename'  #拼接后要保存的文件路径  
SaveFile_Name='TEST_2_all.csv'    #合并后要保存的文件名
        
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

## 排序
#batchfile = r'C:\Users\huton\Desktop\week4\test2\TimeRefine\600_filename\TEST_2_all.csv'
#    
#batchdata = pd.read_csv(batchfile)
#TEST_sorted = batchdata.sort_values("filename",inplace=True)
#print(TEST_sorted)