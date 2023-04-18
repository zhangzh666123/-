// pages/test/test.js
const db = wx.cloud.database()
const dbPoints = db.collection('points')
const garbagesList = require('../../uitls/garbagesListNew')
// 题目数量
let testNum = 10
// 判断结果列表
let judge = []
// 按键点击次数
let index = 0
let newTest = []

Component({
  /**
   * 页面的初始数据
   */
  data: {
    progressWidth: '10%',
    progress: [],
    constentShow: 1,
    titleShow: 1,
    slide: 1,
    options: [{
      "title": "有害垃圾",
      "class": 1,
      "color": ''
    }, {
      "title": "可回收物",
      "class": 2,
      "color": ''
    }, {
      "title": "厨余垃圾",
      "class": 3,
      "color": ''
    }, {
      "title": "其他垃圾",
      "class": 4,
      "color": ''
    }],
    testObject: {},
    test: [],
    optionButtonJudge: '',
    resultShow: false,
    userName: '',
    portrait: '',

    allRightNumber: 0,
    allWrongNumber: 0,
    newAnswerNumber: 0,
    allPoints: 0,


    rightNumber: 0,
    wrongNumber: 0,
    points: 0,
    answerNumber: 0,
    date: "",

    testAuthShow: false,
    unableTouch: false
  },
  pageLifetimes: {
    show() {
      if (typeof this.getTabBar === 'function' &&
        this.getTabBar()) {
        this.getTabBar().setData({
          selected: 1,
        })
      }
    }
  },
  methods: {
    changePoints(docId, date, NewAnswerNumber, NewNrongNumber, NewRightNumber, NewPoints) {
      dbPoints.doc(docId).update({
          data: {
            date: date,
            answerNumber: NewAnswerNumber,
            wrongNumber: NewNrongNumber,
            rightNumber: NewRightNumber,
            points: NewPoints
          }
        })
        .then((res) => {
          console.log(res);
          wx.showToast({
            icon: 'success',
            title: '积分上传成功',
          })
        })
        .catch((err) => {
          console.error(err);
        })
    },
    getAnswerNumber(openid) {
      return new Promise((resolve, reject) => {
        dbPoints.where({
            _openid: openid
          }).get()
          .then((res) => {
            resolve({
              status: 200,
              data: res.data[0]
            })
          })
          .catch((err) => {
            reject({
              status: 400,
              errMsg: err
            })
          })
      })
    },
    // 上方进度条宽度
    progressWidth() {
      let width = Math.floor(100 / testNum)
      this.setData({
        progressWidth: width + '%'
      })
    },
    // 随机抽取十个数提取不同类别中的题目
    randomIndex() {
      return new Promise((resolve, reject) => {
        // 抽取
        newTest = []
        for (let i = 0; i < testNum; i++) {
          const classIndex = Math.floor(Math.random() * 4 + 1)
          const dataLength = garbagesList[classIndex].data.length
          const dataIndex = Math.floor(Math.random() * dataLength)
          const dataListLength = garbagesList[classIndex].data[dataIndex].dataList.length
          const dataListIndex = Math.floor(Math.random() * dataListLength)
          // 将提取出来的题目保存到列表
          newTest.push({
            // [showActive]: true,
            "class": classIndex,
            "title": garbagesList[classIndex].data[dataIndex].dataList[dataListIndex],
            "index": i + 1,
            "judge": ''
          })
          // console.log(i);
          if (i == testNum - 1) {
            // setTimeout(() => {
            resolve('题目抽取完成')
            // }, 5000)
          }

        }
      })
    },
    // 按钮判断
    judgeTrue(e) {
      // 按钮初始状态
      let options = [{
        "title": "有害垃圾",
        "class": 1,
        "optionButtonJudge": ''
      }, {
        "title": "可回收物",
        "class": 2,
        "optionButtonJudge": ''
      }, {
        "title": "厨余垃圾",
        "class": 3,
        "optionButtonJudge": ''
      }, {
        "title": "其他垃圾",
        "class": 4,
        "optionButtonJudge": ''
      }]
      this.setData({
        unableTouch: true
      })
      if (this.data.testObject.class == e.target.dataset.class) {
        // 选择正确情况，按钮变为绿色，上方进度条加一段绿色，积分数增加
        options[e.target.dataset.class - 1]["optionButtonJudge"] = 'optionButtonRight'
        this.data.progress.push("progressRight")
        this.setData({
          options: options,
          progress: this.data.progress
        })
        judge.push("第" + index + "题" + "题目是：" + this.data.testObject.title + ",你选对啦 ,答案是" + this.data.options[e.target.dataset.class - 1].title)
        console.log('你选对啦！')
        this.data.rightNumber += 1
        this.data.points = this.data.rightNumber * 1
      } else {
        // 错误情况，按钮为红色，并且正确的按钮变为绿色，上方进度条增加一段绿色
        options[this.data.testObject.class - 1]["optionButtonJudge"] = 'optionButtonRight'
        options[e.target.dataset.class - 1]["optionButtonJudge"] = 'optionButtonError'
        this.data.progress.push("progressError")
        this.setData({
          options: options,
          progress: this.data.progress
        })
        judge.push("第" + index + "题" + "题目是：" + this.data.testObject.title + ",你选错了,你选择了" + this.data.options[e.target.dataset.class - 1].title + ",正确答案是:" + this.data.options[this.data.testObject.class - 1].title)
        console.log('选择错误。')
        this.data.wrongNumber += 1
      }
      // 答题结束，初始化按钮状态，按钮点击次数加1
      this.setData({
        options: options
      })
      index++
      if (index < testNum) {
        // 按钮次数小于测试题目数，切换到下一题，否则跳转到结束
        // 延时一段时间用来显示按钮颜色
        setTimeout(() => {
          this.setData({
            titleShow: false,
            slide: 2,
            stopTab: true
          }, () => {
            setTimeout(() => {
              this.setData({
                titleShow: true,
                slide: 1,
                testObject: this.data.test[index],
                stopTab: false,
                options: [{
                  "title": "有害垃圾",
                  "class": 1,
                  "optionButtonJudge": ''
                }, {
                  "title": "可回收物",
                  "class": 2,
                  "optionButtonJudge": ''
                }, {
                  "title": "厨余垃圾",
                  "class": 3,
                  "optionButtonJudge": ''
                }, {
                  "title": "其他垃圾",
                  "class": 4,
                  "optionButtonJudge": ''
                }]
              })
              this.setData({
                unableTouch: false
              })
              console.log(this.data.testObject.title, this.data.options[this.data.testObject.class - 1].title)
            }, 500)
          })
        }, 1000)
      } else {
        // 按钮次数等于题数，说明完成答题，关闭答题页面跳转到结束，加载正确数和积分数
        this.setData({
          constentShow: false
        }, () => {
          setTimeout(() => {
            this.setData({
              resultShow: true,
              points: this.data.points
            })
          }, 1500)
        })
        // 积分与正确题目数比例

        console.log("正确数：", this.data.rightNumber, "错误数：", this.data.wrongNumber, "得分：", this.data.points)
        this.setData({
          allRightNumber: this.data.rightNumber + this.data.allRightNumber,
          allWrongNumber: this.data.wrongNumber + this.data.allWrongNumber,
          newAnswerNumber: this.data.answerNumber - 1,
          allPoints: this.data.points + this.data.allPoints,
          date: new Date()
        }, () => {
          this.changePoints(this.data.docId, this.data.date, this.data.newAnswerNumber, this.data.allWrongNumber, this.data.allRightNumber, this.data.allPoints)
        })
      }
    },
    goon() {
      wx.redirectTo({
        url: '../testTitle/testTitle',
      })
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: async function (options) {
      wx.showLoading({
        title: '抽取题目中...',
      })
      const eventChannel = this.getOpenerEventChannel()
      // 监听acceptDataFromOpenerPage事件，获取上一页面通过eventChannel传送到当前页面的数据
      eventChannel.on('acceptDataFromOpenerPage', (data) => {
        console.log(data.data)
        this.setData({
          openid: data.data.openid,
          docId: data.data.docId,
          answerNumber: data.data.answerNumber
        })
      })

      // 判断结果列表
      judge = []
      // 按键点击次数
      index = 0
      this.setData({
        test: [],
        testObject: {}
      })

      let getInfoStorage = wx.getStorageSync('userInfoStorage')
      if (getInfoStorage) {
        this.setData({
          userName: getInfoStorage.userName,
          portrait: getInfoStorage.portrait
        })
      }
    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: async function () {

      // 判断答题次数
      let getAnswerNumber = await this.getAnswerNumber(this.data.openid)
      console.log(getAnswerNumber);
      if (getAnswerNumber.data.answerNumber == 0) {
        wx.showToast({
          title: '您已经答过了',
        })
        return
      }



      this.setData({
        allWrongNumber: getAnswerNumber.data.wrongNumber,
        allRightNumber: getAnswerNumber.data.rightNumber,
        allPoints: getAnswerNumber.data.points,
        answerNumber: getAnswerNumber.data.answerNumber,
      })

      // 修改上方进度条单元
      this.progressWidth()
      // 生成题库
      this.randomIndex()
        .then((e) => {
          console.log(e)
          this.setData({
            test: newTest,
            testObject: newTest[0]
          }, () => {
            wx.hideLoading({
              success: (res) => {
                wx.showToast({
                  icon: "success",
                  title: '抽取完成',
                })
              },
            })
          })
          console.log("第一道题：", this.data.testObject.title, this.data.options[this.data.testObject.class - 1].title)
          // console.log(this.data.test)
        })
    },
    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {
    
      this.setData({
        test: [],
        testObject: {}
      })
    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {
      
      this.setData({
        test: [],
        testObject: {}
      })
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
  }
})
