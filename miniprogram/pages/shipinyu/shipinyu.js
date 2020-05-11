// pages/shipinyu/shipinyu.js
var Promise = require('../../promise.js')
var util = require('../../util/util.js');
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    filename:[],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
  },
  formsubmit(e) {
    util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
      {
        "access_token": app.globalData.access_token,
        "file_name": 'TEST' + e.detail.value.inputValue + '.csv',
      }).then(function (res) {
        app.globalData.output_fileName=res.data.data.file_name;
        console.log(app.globalData.output_fileName);
      })
    wx.hideLoading();
    app.globalData.filename0 = "TEST" + e.detail.value.inputValue + ".csv" ;
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest/RandomForest',
      })
    }, 4000)
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})