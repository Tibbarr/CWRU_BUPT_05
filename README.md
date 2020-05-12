# CWRU_BUPT_05
【移动互联网应用课程设计】第五组CWRU轴承运维监测平台项目汇总


------



## 项目概述

故障预测与健康管理PHM（Prognostics Health Management）满足了自主保障、自主诊断的，是基于状态的维修CBM (视情维修，condition based maintenance)的升级发展。它强调资产设备管理中的状态感知，监控设备健康状况、故障频发区域与周期，通过数据监控与分析，预测故障的发生，从而大幅度提高运维效率。

本项目使用CWRU数据集，在python环境下使用随机森林算法实现了轴承故障的预测，并通过PHM平台将数据和模型接入微信小程序，实现了一个可提供给运维人员使用的 “轴承运维监测平台” 工业APP。

1. 实验平台：www.phmlearn.com

2. CWRU数据集说明：

   包含正常基座数据（NORMAL），滚动体故障（B），内圈故障（IR），外圈故障（OR）四种类型。

   数据特征包括：

- DE - 驱动端加速度数据
- FE - 风扇端加速度数据
- BA - 基本加速度数据
- RPM- rpm during testing



## 目录结构

**【python_code】**（具体的文件说明参考“运行说明”部分）

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


* colorui：colorui组件库
* components：colorui组件库
* ec-canvas：echarts组件库
* images：小程序中用到的背景图

* pages
  * index：首页
  * preindex：开始预测页
  * shipinyu：单个元件特征提取
  * shipinyu1：选择分组并进行特征提取
  * RandomForest：单个元件预测
  * RandomForest1：分组预测
  * result：单个元件预测结果页
  * csvtest：分组预测结果展示
  * lookgroup：查看详情选择页
  * infodetail：单个元件详情页
  * multiCharts：报表展示页
  
* util：用户配置文件
* app.js / app.json / app.wxss：全局配置文件
* icon.wxss：icon样式设置文件
* main.wxss：整体样式设置文件
* project.config.json：项目配置文件
* promise.js：时序控制文件



**【data】**

* Train：训练集
  * NORMAL01.csv  -  NORMAL02.csv
  * B01.csv  -  B06.csv
  * OR01.csv  -  OR14.csv
  * IR01.csv  -  IR06.csv
  
* TEST1 : 第一组测试集
  * TEST01.csv  -  TEST14.csv
  
* TEST2 : 第二组测试集
  * TEST1.csv  -  TEST142.csv



**【packets】**

* numpy_cp37

* pandas_cp37

* scikit-learn_cp37





## 版本管理

* v 0.0.1：上传了数据集、模型处理和小程序部分的源代码
* v 1.0.1：上传了依赖包，完善了项目文档




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

项目地址：https://github.com/Tibbarr/CWRU_BUPT_05.git

从github上克隆项目至本地即可。

#### 2. 部署项目

1）安装python环境及开发工具

2）使用cmd进入对应whl文件所在的目录，安装依赖包，命令如下：

```
pip install numpy-1.16.6-cp37-cp37m-win_amd64.whl
pip install pandas-0.23.2-cp37-cp37m-win_amd64.whl
pip install scikit_learn-0.19.2-cp37-cp37m-win_amd64.whl
```

3）安装成功后，使用开发工具打开对应的.py文件，即可运行相应代码

4）安装微信开发者工具，导入miniprogram项目，进行编译和预览即可



## 运行说明
### 一.  python 模型处理部分
#### 1. 数据处理

##### 1.1 本地预处理

​		在执行代码之前，需手动为训练集中的 NORMAL2.csv 和第一组测试集中的 TEST08.csv 补齐第三列，可用任意数字填充。

##### 1.2 处理训练集

​		按照文件名中的STEP标注，顺序执行 STEP1 - STEP7 对应的 .py 文件：

* **STEP1_TrainDrop：** 初步处理训练集，规整格式，方便后续特征提取
> 运行前需将本地train文件夹中的文件分类整理在B、IR、OR、NORMAL文件夹中，并替换相应的输出路径
* **STEP2_Test1Drop：** 初步处理第一组训练集，规整格式，增加用于训练的数据量
* **STEP3_TimeAndFreRefine：** 对规整之后的数据集进行时频域特征提取
* **STEP4_LabelTrain：** 给训练集打上对应的标签，并进行初步合并
* **STEP5_LabelTest1：** 给第一组训练集打上对应的标签
* **STEP6_AddLabeledTrainTest：** 将处理好的训练集和第一组测试集合并为一个文件
> 运行前需要将打好标签的训练集和第一组测试集放到同一个文件夹下，并按照同样的形式修改路径
* **STEP7_Split：** 将上述处理好的数据集按照 4:1 的比例划分为 train 和 test

##### 1.3 处理测试集

按照文件名中的STEP标注，顺序执行 STEP8 - STEP9 对应的 .py 文件，对第二组测试集进行处理：

* **STEP8_TimeAndFreRefineTest2：** 对142个测试集文件进行与训练集同样的时频域特征提取
* **STEP9_Addfilename：** 给142个测试文件打上对应的TEST文件名，并整合为一个文件



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

* **Other_Dataclean：** 原本用于特征提取之前的数据清洗
> 在项目后期，考虑到时间窗选取较大导致训练集的数据量过少，最终的执行步骤中舍弃了数据清洗，直接进行特征提取
* **Other_PHMmodeltest：** 将保存在本地的.model模型上传至平台以获取api时使用的测试文件
* **Other_Rftiaocan：** 模型训练的过程中用于调参的代码，按照注释具体分为多个部分
> 由于调参每次只针对其中的一个或两个参数，运行时需要局部运行或将剩余部分进行注释
* **Other_SaveModel：** 将训练好的模型保存在本地

### 二.  微信小程序部分

​	在微信开发者工具中导入miniprogram项目即可进行编译。

​	如需使用PHM平台的其它功能，需要替换：

* app.js文件中的access_token
* 将需要请求api的对应.js文件中util.reqFunc()中的url替换为自己平台上获得的url


## 注意事项

1. 在执行python代码的过程中，需要按照上述说明替换对应的目录地址；
2. 如果直接运行代码时随机森林模型运行时出现报错，可能是由于sklearn的版本导致，可尝试安装低版本的sklearn
3. 微信小程序中调用自己的api需要经过PHM平台，获取api及平台access_token的方式可参考以下教程：http://www.phmlearn.com/u/zangml/blogs/77
