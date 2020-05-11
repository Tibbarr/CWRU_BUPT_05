//index.js
Page({
  data: {
  },

  onLoad: function() {
  },

  startPre(){
    wx.navigateTo({
      url: '/pages/preindex/preindex',
    })
  },

  lookup() {
    wx.navigateTo({
      url: '/pages/lookgroup/lookgroup',
    })
  },

  createCharts() {
    wx.navigateTo({
      url: '/pages/multiCharts/multiCharts',
    })
  }
})
