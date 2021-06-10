# -*- ecoding: utf-8 -*-
# @ModuleName: main
# @Author: Rex
# @Time: 2021/6/9 4:11 下午
import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton, QAction, QLineEdit
import requests
import json

class Ui_RouterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(650,800)
        #Router
        self.add_router_label=QLabel('<html><head/><body><p><span style="color:#ff0000;">Operating router:</span></p></body></html>',self)
        self.add_router_label.setGeometry(10, 30, 350, 16)
        # Device Id
        self.deivceIdLabel=QLabel("DeviceId:",self)
        self.deivceIdLabel.setGeometry(10,20,60,80)
        self.deviceIdLineEdit=QLineEdit(self)
        self.deviceIdLineEdit.setGeometry(110,50,220,25)
        self.deviceIdLineEdit.setText("CC:1B:E0:E0:EC:88")
        self.deviceIdTipsLabel=QLabel('<html><head/><body><p><span style="color:#ff0000;">Enter the MAC address of the device</span></p></body></html>',self)
        self.deviceIdTipsLabel.setGeometry(340,50,300,20)
        # Device Name
        self.deivceNameLabel = QLabel("DeviceName:", self)
        self.deivceNameLabel.setGeometry(10, 60, 80, 80)
        self.deviceNameLineEdit = QLineEdit(self)
        self.deviceNameLineEdit.setGeometry(110, 90, 220, 25)
        self.deviceNameLineEdit.setText("Cassia Rex")
        self.deviceNameTipsLabel = QLabel(
            '<html><head/><body><p><span style="color:#ff0000;">Enter the Name of the device</span></p></body></html>',
            self)
        self.deviceNameTipsLabel.setGeometry(340, 90, 300, 20)
        #address
        self.deivceaddressLabel = QLabel("Routeraddress:", self)
        self.deivceaddressLabel.setGeometry(10, 90, 100, 100)
        self.deviceAddressLineEdit = QLineEdit(self)
        self.deviceAddressLineEdit.setGeometry(110, 130, 220, 25)
        self.deviceAddressLineEdit.setText("http://10.10.1.69")
        self.deviceAddressTipsLabel = QLabel(
            '<html><head/><body><p><span style="color:#ff0000;">Enter the Ipaddress of the router</span></p></body></html>',
            self)
        self.deviceAddressTipsLabel.setGeometry(340, 130, 300, 20)
        # router type
        self.deivceTypeLabel = QLabel("RouterType:", self)
        self.deivceTypeLabel.setGeometry(10, 130, 100, 100)
        self.deviceTypeLineEdit = QLineEdit(self)
        self.deviceTypeLineEdit.setGeometry(110, 170, 220, 25)
        self.deviceTypeLineEdit.setText("Cassia")
        self.deviceTypeTipsLabel = QLabel(
            '<html><head/><body><p><span style="color:#ff0000;">Enter the type of the router</span></p></body></html>',
            self)
        self.deviceTypeTipsLabel.setGeometry(340, 170, 300, 20)

        #Add Router
        self.addRouterButtom=QPushButton('Add Router',self)
        self.addRouterButtom.setGeometry(10,210,110,35)
        self.addRouterButtom.clicked.connect(self.add_router)

        #Del Router
        self.DelRouterButtom = QPushButton('Del Router', self)
        self.DelRouterButtom.setGeometry(150, 210, 110, 35)
        self.DelRouterButtom.clicked.connect(self.del_router)

        # Show Router
        self.ShowRouterButtom = QPushButton('Show Router', self)
        self.ShowRouterButtom.setGeometry(290, 210, 110, 35)
        self.ShowRouterButtom.clicked.connect(self.show_router)

        #Listen router
        self.list_router_label = QLabel(self)
        self.list_router_label.setText(
            '<a href=http://127.0.0.1:8123/listener/eventlog>''<b>''List Temperature Data''</b>''</a>')
        self.list_router_label.setOpenExternalLinks(True)
        self.list_router_label.setGeometry(10, 290, 600, 50)
        #listen temp
        self.list_temp_label=QLabel(self)
        self.list_temp_label.setText('<a href=http://127.0.0.1:8123/listener/temperature>''<b>List Temperature Data</b>''</a>')
        self.list_temp_label.setOpenExternalLinks(True)
        self.list_temp_label.setGeometry(180,290,600,50)
        #listen ECG
        self.list_ecg_label=QLabel(self)
        self.list_ecg_label.setText('<a href=http://127.0.0.1:8123/listener/ecg>'' <b>List ECG Data</b>''</a>')
        self.list_ecg_label.setOpenExternalLinks(True)
        self.list_ecg_label.setGeometry(370,290,600,50)
        # list SpO2
        self.list_spo2_label = QLabel(self)
        self.list_spo2_label.setText(
            '<a href=http://127.0.0.1:8123/listener/spo2>'' <b>List SpO2 Data</b>''</a>')
        self.list_spo2_label.setOpenExternalLinks(True)
        self.list_spo2_label.setGeometry(500, 290, 600, 50)

        #Tips:
        self.TipsLabel=QLabel('<html><head/><body><span style="color:#ff0000;">Tips: </span></body></html>\n'
                              '<html><head/><body><span style="color:#ff0000;">1.Add Router 所有字段都为必填 </span></body></html>\n'
                              '<html><head/><body><span style="color:#ff0000;">2.Del Router 只需填写DeviceId字段 </span></body></html>',self)
        self.TipsLabel.setGeometry(10,180,600,200)
        # 日志栏
        self.log_textEdit=QTextEdit(self)
        self.log_textEdit.setGeometry(30,340,500,430)
        self.setWindowTitle("ServerSDKGui v2.0")
        #创建菜单栏
        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)
        device_window = QAction('Add Device', self)
        self.menubar.addAction(device_window)
        device_window.triggered.connect(self.show_device_window)
        self.show()



    def show_device_window(self):
        from Device import Ui_DeviceWindow
        self.close()
        self.device_ui = Ui_DeviceWindow()
        self.device_ui.show()

    def show_testEdit(self,str):
        self.log_textEdit.append(str)

    def add_router(self):
        print("1111")
        self.log_textEdit.clear()
        deviceId=self.deviceIdLineEdit.text()
        deviceName=self.deviceNameLineEdit.text()
        deviceAddress=self.deviceAddressLineEdit.text()
        deviceType=self.deviceTypeLineEdit.text()
        self.thread = Add_router(deviceId,deviceName,deviceAddress,deviceType)
        self.thread.trigger.connect(self.show_testEdit)
        self.thread.start()

    def del_router(self):
        self.log_textEdit.clear()
        deviceId = self.deviceIdLineEdit.text()
        self.thread = Del_router(deviceId)
        self.thread.trigger.connect(self.show_testEdit)
        self.thread.start()

    def show_router(self):
        self.log_textEdit.clear()
        self.thread = Show_router()
        self.thread.trigger.connect(self.show_testEdit)
        self.thread.start()



class Add_router(QThread):
    trigger = pyqtSignal(str)
    def __init__(self,deviceId,deviceName,deviceAddress,deviceType):
        super(Add_router, self).__init__()
        self.deviceId=deviceId
        self.deviceName=deviceName
        self.deviceAddress=deviceAddress
        self.deviceType=deviceType

    def run(self):
        try:
            requestbody = [{"deviceId":self.deviceId,"deviceName":self.deviceName,"address":self.deviceAddress,"routerType":self.deviceType}]
            url = "http://localhost:8123/routers"
            payload = json.dumps(requestbody)
            print(payload)
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
    def __init__(self,deviceId):
        super(Del_router,self).__init__()
        self.deviceId=deviceId

    def run(self):
        try:
            requestbody=[{"deviceId":self.deviceId}]
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_RouterWindow()
    sys.exit(app.exec_())
