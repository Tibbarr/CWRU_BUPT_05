## 目录结构

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




## 依赖配置


#### 微信小程序开发环境

- 微信开发者工具稳定版 [Stable Build] (1.02.2004020)
> 下载地址：https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html



## 运行说明
### 微信小程序部分

```
在微信开发者工具中导入miniprogram项目即可进行编译。

如需使用PHM平台的其它功能，需要替换：
```

* app.js文件中的access_token
* 将需要请求api的对应.js文件中util.reqFunc()中的url替换为自己平台上获得的url


## 注意事项

3. 微信小程序中调用自己的api需要经过PHM平台，获取api及平台access_token的方式可参考以下教程：http://www.phmlearn.com/u/zangml/blogs/77