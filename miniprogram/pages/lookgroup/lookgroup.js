const app = getApp();
var myDate = new Date();


Page({
  data: {
    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar,
    Custom: app.globalData.Custom,

    zhouchenglistData1:[],

    zhouchenglistData: [{ "message": 1 }, { "message": 2 },
      { "message": 3 }, { "message": 4 }, { "message": 5 },
      { "message": 6 }, { "message": 7 }, { "message": 8 },
      { "message": 9 }, { "message": 10 }, { "message": 11 },
      { "message": 12 }, { "message": 13 }, { "message": 14 },
      { "message": 15 }, { "message": 16 }, { "message": 17 },
      { "message": 18 }, { "message": 19 }, { "message": 20 },
      { "message": 21 }, { "message": 22 }, { "message": 23 },
      { "message": 24 }, { "message": 25 }, { "message": 26 },
      { "message": 27 }, { "message": 28 }, { "message": 29 },
      { "message": 30 }, { "message": 31 }, { "message": 32 },
      { "message": 33 }, { "message": 34 }, { "message": 35 },
      { "message": 36 }, { "message": 37 }, { "message": 38 },
      { "message": 39 }, { "message": 40 }, { "message": 41 },
      { "message": 42 }, { "message": 43 }, { "message": 44 },
      { "message": 45 }, { "message": 46 }, { "message": 47 },
      { "message": 48 }, { "message": 49 }, { "message": 50 },
      { "message": 51 }, { "message": 52 }, { "message": 53 },
      { "message": 54 }, { "message": 55 }, { "message": 56 },
      { "message": 57 }, { "message": 58 }, { "message": 59 },
      { "message": 60 }, { "message": 61 }, { "message": 62 },
      { "message": 63 }, { "message": 64 }, { "message": 65 },
      { "message": 66 }, { "message": 67 }, { "message": 68 },
      { "message": 69 }, { "message": 70 }, { "message": 71 },
      { "message": 72 }, { "message": 73 }, { "message": 74 },
      { "message": 75 }, { "message": 76 }, { "message": 77 },
      { "message": 78 }, { "message": 79 }, { "message": 80 },
      { "message": 81 }, { "message": 82 }, { "message": 83 },
      { "message": 84 }, { "message": 85 }, { "message": 86 },
      { "message": 87 }, { "message": 88 }, { "message": 89 },
      { "message": 90 }, { "message": 91 }, { "message": 92 },
      { "message": 93 }, { "message": 94 }, { "message": 95 },
      { "message": 96 }, { "message": 97 }, { "message": 98 },
      { "message": 99 }, { "message": 100 }, { "message": 101 },
      { "message": 102 }, { "message": 103 }, { "message": 104 },
      { "message": 105 }, { "message": 106 }, { "message": 107 },
      { "message": 108 }, { "message": 109 }, { "message": 110 },
      { "message": 111 }, { "message": 112 }, { "message": 113 },
      { "message": 114 }, { "message": 115 }, { "message": 116 },
      { "message": 117 }, { "message": 118 }, { "message": 119 },
      { "message": 120 }, { "message": 121 }, { "message": 122 },
      { "message": 123 }, { "message": 124 }, { "message": 125 },
      { "message": 126 }, { "message": 127 }, { "message": 128 },
      { "message": 129 }, { "message": 130 }, { "message": 131 },
      { "message": 132 }, { "message": 133 }, { "message": 134 },
      { "message": 135 }, { "message": 136 }, { "message": 137 },
      { "message": 138 }, { "message": 139 }, { "message": 140 },
      { "message": 141 }, { "message": 142 },
     ]

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

    var templist=[]
    for (var i = 1; i < 143; i++) {
      templist.push(i)
    }

    var seed = Math.floor(Math.random() * 3)
    var temp = ""
    switch (seed) {
      case 0:
        temp = "东"
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
      station: temp,
      zhouchenglistData1: templist})
  },
  
  infodetail(e) {
    var chuancan = e.currentTarget.dataset.index
    console.log(chuancan)
    wx.navigateTo({
      url: '/pages/infodetail/infodetail?id='+chuancan
    })
  },

  backindex(){
    wx.navigateBack({
    })
  }
})
