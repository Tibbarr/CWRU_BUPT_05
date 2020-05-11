import * as echarts from '../../ec-canvas/echarts';
const app = getApp();
var myDate = new Date();
Page({
  onShareAppMessage: function (res) {
    return {
      title: 'ECharts',
      path: '/pages/index/index',
      success: function () { },
      fail: function () { }
    }
  },
  data: {

    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar,
    Custom: app.globalData.Custom,

    zhouchengnumber1: Math.floor(Math.random(myDate.getSeconds()) * 142),
    zhouchengnumber2: Math.floor(Math.random(myDate.getSeconds()) * 142),
    year: Math.floor(Math.random(myDate.getSeconds()) * 10),
    month: Math.floor(Math.random(myDate.getSeconds()) * 10),
    number: Math.floor(Math.random(myDate.getSeconds()) * 42),
    breakyear1: myDate.getFullYear() - Math.floor(Math.random(myDate.getSeconds()) * 10),
    breakmonth1: myDate.getMonth() - Math.floor(Math.random(myDate.getSeconds()) * 1),
    breakday1: myDate.getDate() - Math.floor(Math.random(myDate.getSeconds()) * 10),
    breakyear2: myDate.getFullYear() - Math.floor(Math.random(myDate.getSeconds()) * 10),
    breakmonth2: myDate.getMonth() - Math.floor(Math.random(myDate.getSeconds()) * 1),
    breakday2: myDate.getDate() - Math.floor(Math.random(myDate.getSeconds()) * 10),
    breakclass1: "",
    breakclass2: "",

    ecPie: {
      onInit: function (canvas, width, height) {
        const pieChart = echarts.init(canvas, null, {
          width: width,
          height: 280
        });
        canvas.setChart(pieChart);
        pieChart.setOption(getPieOption());

        return pieChart;
      }
    },

    ecBar: {
      onInit: function (canvas, width, height) {
        const barChart = echarts.init(canvas, null, {
          width: width,
          height: height
        });
        canvas.setChart(barChart);
        barChart.setOption(getBarOption());

        return barChart;
      }
    }
  },

  onReady() {
  },

  onLoad: function (options) {
    var myDate2 = new Date();
    var seed1 = Math.floor(Math.random(myDate.getSeconds()) * 2)
    var seed2 = Math.floor(Math.random(myDate2.getSeconds()+3) * 2)
    var temp1 = ""
    var temp2 = ""

    switch (seed1) {
      case 0:
        temp1 = "B"
        break;
      case 1:
        temp1 = "OR"
        break;
      case 2:
        temp1 = "IR"
        break;
    }

    switch (seed2) {
      case 0:
        temp2 = "B"
        break;
      case 1:
        temp2 = "OR"
        break;
      case 2:
        temp2 = "IR"
        break;
    }
    this.setData({
      breakclass1: temp1,
      breakclass2: temp2,
    })
  },


  output() {
  wx.navigateBack({
  })
  },
});


function getPieOption() {
  var B = Math.floor(Math.random() * 30)
  var IR = Math.floor(Math.random() * 50)
  var OR = Math.floor(Math.random() * 40)

  return {
    color: ["#CCE1F3", "#F7F4F4", "#B4D1E1"],
    series: [{
      label: {
        position: 'inside',
        normal: {
          fontSize: 24,
          position: 'inside',
        }
      },
      type: 'pie',
      center: ['50%', '50%'],
      radius: [30, '65%'],
      data: [{
        value: B,
        name: 'B',
      }, {
        value: IR,
        name: 'IR'
      }, {
        value: OR,
        name: 'OR'
      }, 
      ],
      //修改字体
      itemStyle: {
        normal: {
          show: true,
          label: {
            formatter: '{b}:({d}%)',
            textStyle: {
              color: 'black',
              fontSize: 34,
              fontWeight: 'bolder'
            }
          },
          labelLine: {
            lineStyle: {
              color: 'black'
            }
          }
        },

        emphasis: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 2, 2, 0.3)'
        }
      }
    }]
  };
}

function getBarOption() {
 
  var B1 = Math.floor(Math.random() * 20)
  var B2 = Math.floor(Math.random() * 22)
  var B3 = Math.floor(Math.random() * 20)
  var B4 = Math.floor(Math.random() * 15)
  var B5 = Math.floor(Math.random() * 18)
  var B6 = Math.floor(Math.random() * 20)
  var B7 = Math.floor(Math.random() * 30)
  var B8 = Math.floor(Math.random() * 24)
  var B9 = Math.floor(Math.random() * 25)
  var B10 = Math.floor(Math.random() * 21)
  var B11 = Math.floor(Math.random() * 26)
  var B12 = Math.floor(Math.random() * 25)
  var B13 = Math.floor(Math.random() * 28)
  var B14 = Math.floor(Math.random() * 23)

  var OR1 = Math.floor(Math.random() * 30)
  var OR2 = Math.floor(Math.random() * 22)
  var OR3 = Math.floor(Math.random() * 40)
  var OR4 = Math.floor(Math.random() * 25)
  var OR5 = Math.floor(Math.random() * 28)
  var OR6 = Math.floor(Math.random() * 20)
  var OR7 = Math.floor(Math.random() * 19)
  var OR8 = Math.floor(Math.random() * 18)
  var OR9 = Math.floor(Math.random() * 21)
  var OR10 = Math.floor(Math.random() * 23)
  var OR11 = Math.floor(Math.random() * 27)
  var OR12 = Math.floor(Math.random() * 32)
  var OR13 = Math.floor(Math.random() * 22)
  var OR14 = Math.floor(Math.random() * 26)

  var IR1 = Math.floor(Math.random() * 26)
  var IR2 = Math.floor(Math.random() * 32)
  var IR3 = Math.floor(Math.random() * 27)
  var IR4 = Math.floor(Math.random() * 35)
  var IR5 = Math.floor(Math.random() * 48)
  var IR6 = Math.floor(Math.random() * 19)
  var IR7 = Math.floor(Math.random() * 39)
  var IR8 = Math.floor(Math.random() * 25)
  var IR9 = Math.floor(Math.random() * 38)
  var IR10 = Math.floor(Math.random() * 27)
  var IR11 = Math.floor(Math.random() * 25)
  var IR12 = Math.floor(Math.random() * 29)
  var IR13 = Math.floor(Math.random() * 30)
  var IR14 = Math.floor(Math.random() * 24)


  return {
  color: ['#37a2da', '#32c5e9', '#67e0e3'],
    tooltip: {
    trigger: 'axis',
      axisPointer: {            // 坐标轴指示器，坐标轴触发有效
      type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
    },
    confine: true
  },
  legend: {
    data: ['B', 'OR', 'IR']
  },
  grid: {
    left: 20,
      right: 20,
        bottom: 15,
          top: 40,
            containLabel: true
  },
  xAxis: [
    {
      type: 'value',
      axisLine: {
        lineStyle: {
          color: '#999'
        }
      },
      axisLabel: {
        color: '#666'
      }
    }
  ],
    yAxis: [
      {
        type: 'category',
        axisTick: { show: false },
        data: ['设备14', '设备13', '设备12', '设备11', '设备10', '设备9', '设备8', '设备7', '设备6', '设备5', '设备4', '设备3', '设备2', '设备1'],
        axisLine: {
          lineStyle: {
            color: '#999'
          }
        },
        axisLabel: {
          color: '#666'
        }
      }
    ],
      series: [
        {
          name: 'B',
          type: 'bar',
          label: {
            normal: {
              show: true,
              position: 'inside'
            }
          },
          data: [B1, B2, B3, B4, B5, B6, B7,B8,B9,B10,B11,B12,B13,B14],
          itemStyle: {
            // emphasis: {
            //   color: '#37a2da'
            // }
          }
        },

        {
          name: 'OR',
          type: 'bar',
          label: {
            normal: {
              show: true
            }
          },
          data: [OR1, OR2, OR3, OR4, OR5, OR6, OR7,OR8,OR9,OR10,OR11,OR12,OR13,OR14],
          itemStyle: {
            // emphasis: {
            //   color: '#32c5e9'
            // }
          }
        },

        {
          name: 'IR',
          type: 'bar',
          label: {
            normal: {
              show: true,
              position: 'inside'
            }
          },
          data: [IR1, IR2, IR3, IR4, IR5, IR6, IR7,IR8,IR9,IR10,IR11,IR12,IR13,IR14],
          itemStyle: {
            // emphasis: {
            //   color: '#67e0e3'
            // }
          }
        }
      ]
}
}