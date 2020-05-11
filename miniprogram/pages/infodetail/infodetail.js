const app = getApp();
var myDate = new Date();
Page({
  data: {
    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar,
    Custom: app.globalData.Custom,

    zhouchengnumber:"",
    year: Math.floor(Math.random(myDate.getSeconds()) * 10),
    month: Math.floor(Math.random(myDate.getSeconds()) * 10),
    number: Math.floor(Math.random(myDate.getSeconds()) * 42),
    breakyear1: myDate.getFullYear() - Math.floor(Math.random(myDate.getSeconds()) * 10),
    breakmonth1: myDate.getMonth() - Math.floor(Math.random(myDate.getSeconds()) * 1),
    breakday1: myDate.getDate() - Math.floor(Math.random(myDate.getSeconds()) * 10),
    breakyear2: myDate.getFullYear() - Math.floor(Math.random(myDate.getSeconds()) * 10),
    breakmonth2: myDate.getMonth() - Math.floor(Math.random(myDate.getSeconds()) * 1),
    breakday2: myDate.getDate() - Math.floor(Math.random(myDate.getSeconds()) * 10),
    station: ""
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var chuancan = options.id
    var seed=Math.floor(Math.random() * 3)
    var temp = ""
    switch (seed) {
      case 0:
        temp="东"
        break;
      case 1:
        temp = "西"
        break;
      case 2:
        temp = "南"
        break;
      case 3:
        temp = "北"
        break;
    } 
    this.setData({
      station:temp,
      zhouchengnumber:chuancan
    })
  },

  startPre() {
    wx.navigateTo({
      url: '/pages/preindex/preindex',
    })
  },

  backlist(){
    wx.navigateBack({
    })
  },

})