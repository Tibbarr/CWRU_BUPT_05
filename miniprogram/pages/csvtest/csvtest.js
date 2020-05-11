var util = require('../../util/util.js');
var app = getApp();
Page({
  data: {
    output_fileName: [],
    predict: [],
    predict1: [],
    filename: '',
    filename1:[],
    output_fileName1: [],



  },

  onLoad: function (options) {
    this.setData({
      output_fileName: getApp().globalData.output_fileName,
      output_fileName1: getApp().globalData.output_fileName1,
      predict: getApp().globalData.predict,
      predict1: getApp().globalData.predict1,
      filename1: getApp().globalData.filename1,
      filename0: getApp().globalData.filename0,
      

    })
  },
  navToPre() {
    app.globalData.predict = [];
    app.globalData.predict1 = [];
    app.globalData.output_fileName1 = [];
    app.globalData.filename1 = [];
    wx.navigateBack({
      delta: 4
    })  
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