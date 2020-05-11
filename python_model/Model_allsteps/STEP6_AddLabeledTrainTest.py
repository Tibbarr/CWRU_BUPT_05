# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:55:49 2020

@author: Hu Tong
"""

# STEP6 将处理好的训练集和第一次测试集放到同一个文件夹下，合并为一个文件

# 合并为一个
# 合并

Folder_Path=r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_moremoremore'    #要拼接的文件夹及其完整路径，注意不要包含中文  
SaveFile_Path=r'C:\Users\huton\Desktop\week4\TF2\hebin_train\T600_W6_moremoremore'  #拼接后要保存的文件路径  
SaveFile_Name='train_test1_all.csv'    #合并后要保存的文件名
        
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
