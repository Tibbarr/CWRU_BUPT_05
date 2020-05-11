// pages/shipinyu/shipinyu.js
var Promise = require('../../promise.js')
var util = require('../../util/util.js');
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    filename1:[],
    
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },
  navToPre1() {
    for (var k = 1; k <= 10; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString()+'.csv',
        }).then(function(res){
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },




  navToPre2() {
    for (var k = 11; k <= 20; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },



  navToPre3() {
    for (var k =21 ; k <= 30; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },



  navToPre4() {
    for (var k = 31; k <= 40; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },



  navToPre5() {
    for (var k = 41; k <= 50; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },



  navToPre6() {
    for (var k =51 ; k <= 60; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },


  navToPre7() {
    for (var k = 61; k <= 70; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },



  navToPre8() {
    for (var k = 71; k <= 80; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },



  navToPre9() {
    for (var k = 81; k <= 90; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },



  navToPre10() {
    for (var k = 91; k <= 100; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },



  navToPre11() {
    for (var k = 101; k <= 110; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },



  navToPre12() {
    for (var k = 111; k <= 120; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },



  navToPre13() {
    for (var k = 121; k <= 130; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },


  navToPre14() {
    for (var k = 131; k <= 140; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
  },


  navToPre15() {
    for (var k = 141; k <= 142; k++) {
      app.globalData.filename1.push('TEST' + k.toString() + '.csv');
      util.reqFunc('https://api.phmlearn.com/component/upload/2/145',
        {
          "access_token": app.globalData.access_token,
          "file_name": 'TEST' + k.toString() + '.csv',
        }).then(function (res) {
          app.globalData.output_fileName1.push(res.data.data.file_name);
        })
    }
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/RandomForest1/RandomForest1',
      })
    }, 4000)
    console.log(app.globalData.output_fileName1);
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