// pages/GBDT/GBDT.js
var util = require('../../util/util.js');
var Promise = require('../../promise.js')
var app = getApp();
Page({
  data: {

  },
  onLoad: function (options) {

  },

  formsubmit(e) {
    for (var k = 0; k < 10; k++) {
      util.reqFunc("https://api.phmlearn.com/component/upload/ML/model/72/144",
        {
          "access_token": app.globalData.access_token,
          "file_name": app.globalData.output_fileName1[k],
        }).then(function (res) {
          app.globalData.predict1.push(res.data.data.predict);
          
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/csvtest/csvtest',
      })
    }, 8000)
    console.log(app.globalData.predict1);
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