# -*- ecoding: utf-8 -*-
# @ModuleName: main
# @Author: Rex
# @Time: 2021/6/9 4:11 下午
import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton, QMenuBar, QAction, QLineEdit
import requests
import json

class Ui_DeviceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(650,800)
        #Device
        self.add_Device_label=QLabel('<html><head/><body><p><span style="color:#ff0000;">Operating device:</span></p></body></html>',self)
        self.add_Device_label.setGeometry(10, 30, 350, 16)
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
        self.deivceNameLabel.setGeometry(10, 40, 80, 120)
        self.deviceNameLineEdit = QLineEdit(self)
        self.deviceNameLineEdit.setGeometry(110, 90, 220, 25)
        self.deviceNameLineEdit.setText("B34.00083637")
        self.deviceNameTipsLabel = QLabel(
            '<html><head/><body><p><span style="color:#ff0000;">Enter the SnNumber of the device</span></p></body></html>',
            self)
        self.deviceNameTipsLabel.setGeometry(340, 90, 300, 20)
        #deviceType
        self.deivceTypeLabel = QLabel("DeviceType:", self)
        self.deivceTypeLabel.setGeometry(10, 90, 100, 100)
        self.deviceTypeLineEdit = QLineEdit(self)
        self.deviceTypeLineEdit.setGeometry(110, 130, 220, 25)
        self.deviceTypeLineEdit.setText("V200")
        self.deviceTypeTipsLabel = QLabel(
            '<html><head/><body><p><span style="color:#ff0000;">Enter the type of the device</span></p></body></html>',
            self)
        self.deviceTypeTipsLabel.setGeometry(340, 130, 300, 20)

        #Add Device
        self.addDeviceButtom=QPushButton('Add Device',self)
        self.addDeviceButtom.setGeometry(10,170,110,35)
        self.addDeviceButtom.clicked.connect(self.add_Device)

        #Del Device
        self.DelDeviceButtom = QPushButton('Del Device', self)
        self.DelDeviceButtom.setGeometry(150, 170, 110, 35)
        self.DelDeviceButtom.clicked.connect(self.del_Device)

        # Show Device
        self.ShowDeviceButtom = QPushButton('Show Device', self)
        self.ShowDeviceButtom.setGeometry(290, 170, 110, 35)
        self.ShowDeviceButtom.clicked.connect(self.show_Device)

        #Listen Device
        self.list_Device_label = QLabel(self)
        self.list_Device_label.setText(
            '<a href=http://127.0.0.1:8123/listener/eventlog>''<b>''Listener Router''</b>''</a>')
        self.list_Device_label.setOpenExternalLinks(True)
        self.list_Device_label.setGeometry(10, 290, 600, 50)
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
                              '<html><head/><body><span style="color:#ff0000;">1.Add Device 体温设备可只填写DeviceId字段（SN号）其余设备所有字段都为必填 </span></body></html>\n'
                              '<html><head/><body><span style="color:#ff0000;">2.Del Device 只需填写DeviceId字段 </span></body></html>',self)
        self.TipsLabel.setGeometry(10,220,500,90)
        # 日志栏
        self.log_textEdit=QTextEdit(self)
        self.log_textEdit.setGeometry(30,340,500,430)
        self.setWindowTitle("ServerSDKGui v2.0")
        #创建菜单栏
        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)
        device_window = QAction('Add Router', self)
        self.menubar.addAction(device_window)
        device_window.triggered.connect(self.show_router_window)
        self.show()


    def show_router_window(self):
        from Router import Ui_RouterWindow
        self.close()
        self.device_ui = Ui_RouterWindow()
        self.device_ui.show()

    def show_testEdit(self,str):
        self.log_textEdit.append(str)

    def add_Device(self):
        self.log_textEdit.clear()
        deviceId=self.deviceIdLineEdit.text()
        deviceName=self.deviceNameLineEdit.text()
        deviceType=self.deviceTypeLineEdit.text()
        self.thread = Add_Device(deviceId,deviceName,deviceType)
        self.thread.trigger.connect(self.show_testEdit)
        self.thread.start()

    def del_Device(self):
        self.log_textEdit.clear()
        deviceId = self.deviceIdLineEdit.text()
        deviceName=self.deviceNameLineEdit.text()
        self.thread = Del_Device(deviceId,deviceName)
        self.thread.trigger.connect(self.show_testEdit)
        self.thread.start()

    def show_Device(self):
        self.log_textEdit.clear()
        self.thread = Show_Device()
        self.thread.trigger.connect(self.show_testEdit)
        self.thread.start()



class Add_Device(QThread):
    trigger = pyqtSignal(str)
    def __init__(self,deviceId,deviceName,deviceType):
        super(Add_Device, self).__init__()
        self.deviceId=deviceId
        self.deviceName=deviceName
        self.deviceType=deviceType

    def run(self):
        try:
            requestbody = [{"deviceId":self.deviceId,"deviceName":self.deviceName,"deviceType":self.deviceType}]
            url = "http://localhost:8123/devices"
            payload = json.dumps(requestbody)
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            if response.json()['message'] == 'success':
                self.trigger.emit(f'{self.deviceName}添加成功')
            else:
                self.trigger.emit(f'{self.deviceName}添加失败')
        except Exception as e:
            self.trigger.emit(str(e))

class Del_Device(QThread):
    trigger = pyqtSignal(str)
    def __init__(self,deviceId,deviceName):
        super(Del_Device,self).__init__()
        self.deviceId=deviceId
        self.deviceName=deviceName

    def run(self):
        try:
            requestbody=[{"deviceId":self.deviceId}]
            url = "http://localhost:8123/Devices"

            payload = json.dumps(requestbody)
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("DELETE", url, headers=headers, data=payload)
            if response.json()['message'] == 'success':
                self.trigger.emit(f'{self.deviceName}删除成功')
            else:
                self.trigger.emit(f'{self.deviceName}删除失败')
        except Exception as e:
            self.trigger.emit(str(e))

class Show_Device(QThread):
    trigger = pyqtSignal(str)
    def __init__(self):
        super(Show_Device, self).__init__()

    def run(self):
        url = "http://localhost:8123/devices"
        payload = {}
        headers = {}
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            for Device in response.json()['data']:
                self.trigger.emit(str(Device).replace(",", '\n').replace('{', '').replace("}", '').replace(" ", ''))
                self.trigger.emit("----------------------------------------")
        except Exception as e:
            self.trigger.emit(str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_DeviceWindow()
    sys.exit(app.exec_())
