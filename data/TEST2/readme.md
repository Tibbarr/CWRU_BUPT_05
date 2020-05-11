# CWRU四分类任务第二组测试集数据说明及打分方案

## 一、数据说明
数据中共包含142个文件，文件名为TEST1.csv-TEST142.csv，每个文件数据共有三列，分别为DE_time、FE_time和RPM。    
文件中数据列的含义如下：   
DE_time:驱动端加速度数据      
FE_time:风扇端加速度数据       
RPM:每分钟转速数据，在提取时实际上RPM对于每个文件只有一个值，但为了文件格式整齐，扩展成了一列，即实际上这一列都是同一个值，代表该文件的RPM   

## 二、测试集答案提交形式
提交答案时，约定normal(NORMAL), ball(B), outer race(OR), inner race(IR)的预测输出标签为0, 1, 2, 3。      
提交csv文件，文件分两列，第一列为按序预测结果(0/1/2/3)，第二列为预测结果所在的测试集文件(字符串形式，例如TEST1)，分别以label和filename作为列名。提交文件格式、内容和形式与第一组测试集相同，可参照第一组测试集附带的example.csv文件。

## 三、评分规则
使用四类的f1-score(precision和recall值的调和平均数)加权和进行评价，按照上面的标签约定，即：   
score = [0.3×f1score(class1) + 0.3×f1score(class2) + 0.3×f1score(class3) + 0.1×f1score(class0)]*100   
满分为100分。   
打分系统还会返回其他指标，如准确率accuracy，加权精确率precision，加权召回率recall，其中precision和recall权值分配和加权f1-score的权值分配一致。