# -*- ecoding: utf-8 -*-
# @ModuleName: main
# @Author: Rex
# @Time: 2021/6/9 4:11 下午
import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTextEdit,QPushButton
import requests
import json

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(650,800)
        #Router
        self.add_router_label=QLabel('<html><head/><body><p><span style="color:#ff0000;">Router:</span></p></body></html>',self)
        self.add_router_label.setGeometry(10, 10, 350, 16)
        self.add_router_textEdit=QTextEdit(self)
        self.add_router_textEdit.setGeometry(10,30,441,81)
        self.add_router_textEdit.setText(
"""{"deviceId": "CC:1B:E0:E0:EC:88",
"deviceName": "Cassia Rex",
"address": "http://10.10.1.69",
"routerType": "Cassia"} """)
        self.add_router_buttom=QPushButton("Add_Router",self)
        self.add_router_buttom.setGeometry(460,30,121,41)
        self.add_router_buttom.clicked.connect(self.add_router)
        self.del_router_buttom=QPushButton("Del_Router",self)
        self.del_router_buttom.setGeometry(460, 70, 121, 41)
        self.del_router_buttom.clicked.connect(self.del_router)
        self.show_router_buttom=QPushButton("S\nh\no\nw",self)
        self.show_router_buttom.setGeometry(580,30,41,80)
        self.show_router_buttom.clicked.connect(self.show_router)

        # Device
        self.add_device_label = QLabel(
            '<html><head/><body><p><span style="color:#ff0000;">Device:</span></p></body></html>', self)
        self.add_device_label.setGeometry(10, 120, 350, 16)
        self.add_device_textEdit = QTextEdit(self)
        self.add_device_textEdit.setGeometry(10, 140, 441, 81)
        self.add_device_textEdit.setText(
"""{"deviceId": "C7:EE:9D:4B:55:1C",
"deviceName": "O2 7640",
"deviceType": "Checkme_O2"} """)
        self.add_device_buttom = QPushButton("Add_Device", self)
        self.add_device_buttom.setGeometry(460, 140, 121, 41)
        self.add_device_buttom.clicked.connect(self.add_device)
        self.show_router_buttom = QPushButton("S\nh\no\nw", self)
        self.show_router_buttom.setGeometry(580, 140, 41, 80)
        self.show_router_buttom.clicked.connect(self.show_device)
        self.del_device_buttom = QPushButton("Del_Device", self)
        self.del_device_buttom.setGeometry(460, 180, 121, 41)
        self.del_device_buttom.clicked.connect(self.del_device)
        #List router
        self.list_router_label = QLabel(self)
        self.list_router_label.setText(
            'List Temperature Data:''<a href=http://127.0.0.1:8123/listener/eventlog>''&nbsp; <b>http://127.0.0.1:8123/listener/eventlog</b>''</a>')
        self.list_router_label.setOpenExternalLinks(True)
        self.list_router_label.setGeometry(10, 215, 600, 50)
        #list temp
        self.list_temp_label=QLabel(self)
        self.list_temp_label.setText('List Temperature Data:''<a href=http://127.0.0.1:8123/listener/temperature>''&nbsp; <b>http://127.0.0.1:8123/listener/temperature</b>''</a>')
        self.list_temp_label.setOpenExternalLinks(True)
        self.list_temp_label.setGeometry(10,240,600,50)
        #list ECG
        self.list_ecg_label=QLabel(self)
        self.list_ecg_label.setText('List ECG Data:''<a href=http://127.0.0.1:8123/listener/ecg>''&nbsp; <b>http://127.0.0.1:8123/listener/ecg</b>''</a>')
        self.list_ecg_label.setOpenExternalLinks(True)
        self.list_ecg_label.setGeometry(10,265,600,50)
        # list SpO2
        self.list_spo2_label = QLabel(self)
        self.list_spo2_label.setText(
            'List SpO2 Data:''<a href=http://127.0.0.1:8123/listener/spo2>''&nbsp; <b>http://127.0.0.1:8123/listener/spo2</b>''</a>')
        self.list_spo2_label.setOpenExternalLinks(True)
        self.list_spo2_label.setGeometry(10, 290, 600, 50)
        # 日志栏
        self.log_textEdit=QTextEdit(self)
        self.log_textEdit.setGeometry(30,340,500,430)
        self.setWindowTitle("ServerSDKGui v1.0")
        self.show()

    def show_testEdit(self,str):
        self.log_textEdit.append(str)

    def add_router(self):
        self.log_textEdit.clear()
        self.thread = Add_router(self.add_router_textEdit)
        self.thread.trigger.connect(self.show_testEdit)
        self.thread.start()


    def del_router(self):
        self.log_textEdit.clear()
        self.thread = Del_router(self.add_router_textEdit)
        self.thread.trigger.connect(self.show_testEdit)
        self.thread.start()

    def add_device(self):
        self.log_textEdit.clear()
        self.thread = Add_device(self.add_device_textEdit)
        self.thread.trigger.connect(self.show_testEdit)
        self.thread.start()

    def del_device(self):
        self.log_textEdit.clear()
        self.thread = Del_device(self.add_device_textEdit)
        self.thread.trigger.connect(self.show_testEdit)
        self.thread.start()

    def show_router(self):
        self.log_textEdit.clear()
        self.thread = Show_router()
        self.thread.trigger.connect(self.show_testEdit)
        self.thread.start()


    def show_device(self):
        self.log_textEdit.clear()
        self.thread = Show_device()
        self.thread.trigger.connect(self.show_testEdit)
        self.thread.start()


class Add_router(QThread):
    trigger = pyqtSignal(str)
    def __init__(self,add_router_textEdit):
        super(Add_router, self).__init__()
        self.add_router_textEdit=add_router_textEdit

    def run(self):
        try:
            requestbody = [eval(self.add_router_textEdit.toPlainText())]
            url = "http://localhost:8123/routers"
            payload = json.dumps(requestbody)
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            if response.json()['message'] == 'success':
                self.trigger.emit(f'{eval(self.add_router_textEdit.toPlainText())["deviceId"]}添加成功')
            else:
                self.trigger.emit(f'{eval(self.add_router_textEdit.toPlainText())["deviceId"]}添加失败')
        except Exception as e:
            self.trigger.emit(str(e))

class Del_router(QThread):
    trigger = pyqtSignal(str)
    def __init__(self,add_router_textEdit):
        super(Del_router,self).__init__()
        self.add_router_textEdit=add_router_textEdit

    def run(self):
        try:
            requestbody=[{"deviceId":eval(self.add_router_textEdit.toPlainText())['deviceId']}]
            url = "http://localhost:8123/routers"

            payload = json.dumps(requestbody)
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("DELETE", url, headers=headers, data=payload)
            if response.json()['message'] == 'success':
                self.trigger.emit(f'{eval(self.add_router_textEdit.toPlainText())["deviceId"]}删除成功')
            else:
                self.trigger.emit(f'{eval(self.add_router_textEdit.toPlainText())["deviceId"]}删除失败')
        except Exception as e:
            self.trigger.emit(str(e))

class Add_device(QThread):
    trigger = pyqtSignal(str)
    def __init__(self,add_device_textEdit):
        super(Add_device,self).__init__()
        self.add_device_textEdit=add_device_textEdit

    def run(self):
        try:
            requestbody=[eval(self.add_device_textEdit.toPlainText())]
            url = "http://localhost:8123/devices"
            payload = json.dumps(requestbody)
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.json()['message'] == 'success':
                self.trigger.emit(f'{eval(self.add_device_textEdit.toPlainText())["deviceName"]}添加成功')
            else:
                self.trigger.emit(f'{eval(self.add_device_textEdit.toPlainText())["deviceName"]}添加失败')
        except Exception as e:
            self.trigger.emit(str(e))

class Del_device(QThread):
    trigger = pyqtSignal(str)
    def __init__(self,add_device_textEdit):
        super(Del_device, self).__init__()
        self.add_device_textEdit=add_device_textEdit

    def run(self):
        try:
            requestbody=[{"deviceId":eval(self.add_device_textEdit.toPlainText())['deviceId']}]
            url = "http://localhost:8123/devices"
            payload = json.dumps(requestbody)
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("DELETE", url, headers=headers, data=payload)
            if response.json()['message'] == 'success':
                self.trigger.emit(f'{eval(self.add_device_textEdit.toPlainText())["deviceName"]}删除成功')
            else:
                self.trigger.emit(f'{eval(self.add_device_textEdit.toPlainText())["deviceName"]}删除失败')
        except Exception as e:
            self.trigger.emit(str(e))

class Show_router(QThread):
    trigger = pyqtSignal(str)
    def __init__(self):
        super(Show_router, self).__init__()

    def run(self):
        url = "http://localhost:8123/routers"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        for router in response.json()['data']:
            self.trigger.emit(str(router).replace(",", '\n').replace('{', '').replace("}", '').replace(" ", ''))
            self.trigger.emit("----------------------------------------")

class Show_device(QThread):
    trigger = pyqtSignal(str)
    def __init__(self):
        super(Show_device, self).__init__()

    def run(self):
        url = "http://localhost:8123/devices"
        payload = ""
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        for device in response.json()['data']:
            self.trigger.emit(str(device).replace(",", '\n').replace('{', '').replace("}", '').replace(" ", ''))
            self.trigger.emit("----------------------------------------")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    sys.exit(app.exec_())
