# -*- coding: utf-8 -*-
'''
PyQt中高德地图交互操作
'''
from PyQt5.QtWidgets  import QApplication , QWidget , QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
import sys
# 创建一个 application实例
app = QApplication(sys.argv)  
win = QWidget()
win.setWindowTitle('PyQt高德地图API接入')
# 创建一个垂直布局器
layout = QVBoxLayout()
win.setLayout(layout)
# 创建一个 QWebEngineView 对象
view = QWebEngineView()
view.load(QUrl(r"file:///C:/Users/DC/Desktop/amap.html"))
# view.setHtml('''
# <!doctype html>
# <html>
# <head>
#   <meta charset="utf-8">
#   <meta http-equiv="X-UA-Compatible" content="IE=edge">
#   <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
#   <link rel="stylesheet" href="https://a.amap.com/jsapi_demos/static/demo-center/css/demo-center.css" />
#   <link rel="stylesheet" type="text/css" href="https://a.amap.com/jsapi_demos/static/demo-center/css/prety-json.css">
#   <style>
#     html,
#     body,
#     #container {
#       width: 100%;
#       height: 100%;
#     }
#   </style>
#   <title>获取搜索信息</title>
# </head>
#
# <body>
#   <div id="container"></div>
#   <div class="info">
#     <h4>搜索结果展示</h4>
#     <p><span id="input-info"></span></p>
#   </div>
#   <script type="text/javascript">
#         window._AMapSecurityConfig = {
#             securityJsCode:'0501b6504db3a5dd403f52b85094eea1',
#         }
#   </script>
#   <script src="https://webapi.amap.com/maps?v=1.4.15&key=b0f98e823d246c31aefd360f909c39b8&plugin=AMap.PlaceSearch"></script>
#   <script type="text/javascript" src="https://a.amap.com/jsapi_demos/static/demo-center/js/jquery-1.11.1.min.js" ></script>
#   <script type="text/javascript" src="https://a.amap.com/jsapi_demos/static/demo-center/js/underscore-min.js" ></script>
#   <script type="text/javascript" src="https://a.amap.com/jsapi_demos/static/demo-center/js/backbone-min.js" ></script>
#   <script type="text/javascript" src='https://a.amap.com/jsapi_demos/static/demo-center/js/prety-json.js'></script>
#   <script>
#     // 初始化地图
#     var map = new AMap.Map("container", {
#         resizeEnable: true
#     });
#
#     // 获取搜索信息
#     function autoInput(){
#       var keywords = '北京大学';
#       AMap.plugin('AMap.PlaceSearch', function(){
#         var autoOptions = {
#           city: '全国'
#         }
#         var placeSearch = new AMap.PlaceSearch(autoOptions);
#         placeSearch.search(keywords, function(status, result) {
#           // 搜索成功时，result即是对应的匹配数据
#           var node = new PrettyJSON.view.Node({
#               el: document.querySelector("#input-info"),
#               data: result
#           });
#         })
#       })
#     }
#
#     autoInput();
#   </script>
# </body>
#
# </html>
# ''')

layout.addWidget(view)

# 显示窗口和运行app
win.show()
sys.exit(app.exec_())