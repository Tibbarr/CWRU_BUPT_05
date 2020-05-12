# CWRU_BUPT_05
【移动互联网应用课程设计】第五组CWRU轴承运维监测平台项目汇总


------



## 项目概述

简要描述项目的背景和内容。



## 目录结构

**【python_code】**

* Model_allsteps

  * STEP1_TrainDrop.py
  * STEP2_Test1Drop.py
  * STEP3_TimeAndFreRefine.py
  * STEP4_LabelTrain.py
  * STEP5_LabelTest1.py
  * STEP6_AddLabeledTrainTest.py
  * STEP7_Split.py
  * STEP8_TimeAndFreRefineTest2.py
  * STEP9_Addfilename.py
  * STEP10_Model_TrainAndOutput.py
    

* Model_runmodel

  * ModelSTEP1_UseModelOutput.py
  * RFfinalmodel.model
  * T600W6more_test.csv
  * TEST_2_all.csv
  

* other_code

  * Other_Dataclean.py
  * Other_PHMmodeltest.py
  * Other_RFtiaocan.py
  * Other_SaveModel.py



**【miniprogram】**



**【data】**

* Train
  * NORMAL01.csv  -  NORMAL02.csv
  * B01.csv  -  B06.csv
  * OR01.csv  -  OR14.csv
  * IR01.csv  -  IR06.csv
  
* TEST1 : TEST01.csv  -  TEST14.csv
  
* TEST2 : TEST1.csv  -  TEST142.csv




## 版本管理

* v 0.0.1：上传了数据集、模型处理和小程序部分的源代码





## 依赖配置

#### 1. Python环境

- Python 3.7版本


#### 2. 需要配置的python依赖包

- pandas-0.23.2-cp37-cp37m-win_amd64
- numpy-1.16.6-cp37-cp37m-win_amd64
- scikit_learn-0.19.2-cp37-cp37m-win_amd64
  

#### 3. python 开发工具

  推荐使用的开发工具：

* spyder
* pycharm
* jupyter notebook

> 以上工具任选其一即可。小组成员完成本项目使用的主要工具为spyder。


#### 4. 微信小程序开发环境

- 微信开发者工具稳定版 [Stable Build] (1.02.2004020)
> 下载地址：https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html


## 部署说明

#### 1. 从Github上获取项目



#### 2. 部署项目



## 运行说明

#### 1. 数据处理

##### 1.1 本地预处理

​		在执行代码之前，需手动为训练集中的 NORMAL2.csv 和第一组测试集中的 TEST08.csv 补齐第三列，可用任意数字填充。

##### 1.2 处理训练集

​		按照文件名中的STEP标注，顺序执行 STEP1 - STEP7 对应的 .py 文件：

* **STEP1_TrainDrop：** 该文件用于初步处理训练集，规整格式，方便后续进行特征提取
> 运行前需将本地train文件夹中的文件分类整理在B、IR、OR、NORMAL文件夹中，并替换相应的输出路径

* **STEP2_Test1Drop：** 该文件用于初步处理第一组训练集，规整格式，增加用于训练的数据量，方便后续进行特征提取

* **STEP3_TimeAndFreRefine：** 该文件用于对规整之后的训练集和规整后的第一次测试集进行时频域特征提取

* **STEP4_LabelTrain：** 该文件用于给训练集打上对应的标签，并进行初步合并

* **STEP5_LabelTest1：** 该文件用于给第一组训练集打上对应的标签。

* **STEP6_AddLabeledTrainTest：** 该文件用于将处理好的训练集和第一组测试集合并为一个文件
> 运行前需要将打好标签的训练集和第一组测试集放到同一个文件夹下，并按照同样的形式修改路径

* **STEP7_Split：** 该文件用于将上述处理好的数据集按照 4:1 的比例划分为 train 和 test

##### 1.3 处理测试集

按照文件名中的STEP标注，顺序执行 STEP8 - STEP9 对应的 .py 文件，对第二组测试集进行处理：

* **STEP8_TimeAndFreRefineTest2：** 该文件用于对142个测试集文件进行与训练集同样的时频域特征提取

* **STEP9_Addfilename：** 该文件用于给142个测试文件打上对应的TEST文件名，并整合为一个文件



#### 2. 模型训练及输出

经过以上处理后，可以得到用于训练模型的 train 和 test 文件和用于输出第二组测试集结果的 test 文件。运行 STEP10_Model_TrainAndOutput.py 文件，即可进行模型训练和最终的预测结果输出。


#### 3. 模型调用及输出

使用处理好的第二组测试集，直接调用保存在本地的.model模型文件，可进行结果输出。所需的文件已放置在“直接调用model代码及测试文件”文件夹中。其中：
* ModelSTEP1_UseModelOutput.py 文件用于调用模型并进行输出
* .model文件为已经训练好并使用joblib保存的模型文件
* T600Wmore_test 文件用于得到模型评分
* TEST_2_all 为处理后的第二组测试文件

运行代码，即可在设定的路径下得到与执行上述 10 个  STEP 相同的结果输出。



#### 4. 其它代码文件说明

在“其它代码”文件夹中，包含四个处理及调试的过程中用到的辅助代码，分别为：

* **Other_Dataclean：** 该文件原本用于特征提取之前的数据清洗
> 在项目后期，考虑到时间窗选取较大导致训练集的数据量过少，最终的执行步骤中舍弃了数据清洗，直接进行特征提取

* **Other_PHMmodeltest：** 该文件是将保存在本地的.model模型上传至平台以获取api时，使用的测试文件

* **Other_Rftiaocan：** 该文件是模型训练的过程中用于调参的代码，按照注释具体分为多个部分。
> 由于调参每次只针对其中的一个或两个参数，运行时需要局部运行或将剩余部分进行注释

* **Other_SaveModel：** 该文件用于将训练好的模型保存在本地。



## 注意事项

1. 在执行python代码的过程中，需要按照上述说明替换对应的目录地址；
