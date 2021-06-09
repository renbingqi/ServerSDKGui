# -*- ecoding: utf-8 -*-
# @ModuleName: main
# @Author: Rex
# @Time: 2021/6/9 4:11 下午
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTextEdit,QPushButton


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
""""deviceId": "CC:1B:E0:E0:EC:88",
"deviceName": "Cassia Rex",
"address": "http://10.10.1.69",
"routerType": "Cassia" """)
        self.add_router_buttom=QPushButton("Add_Router",self)
        self.add_router_buttom.setGeometry(460,30,121,41)
        self.del_router_buttom=QPushButton("Del_Router",self)
        self.del_router_buttom.setGeometry(460, 70, 121, 41)
        self.show_router_buttom=QPushButton("S\nh\no\nw",self)
        self.show_router_buttom.setGeometry(580,30,41,80)

        # Device
        self.add_device_label = QLabel(
            '<html><head/><body><p><span style="color:#ff0000;">Device:</span></p></body></html>', self)
        self.add_device_label.setGeometry(10, 120, 350, 16)
        self.add_device_textEdit = QTextEdit(self)
        self.add_device_textEdit.setGeometry(10, 140, 441, 81)
        self.add_device_textEdit.setText(""""deviceId": "C7:EE:9D:4B:55:1C",
"deviceName": "O2 7640",
"deviceType": "Checkme_O2" """)
        self.add_device_buttom = QPushButton("Add_Device", self)
        self.add_device_buttom.setGeometry(460, 140, 121, 41)
        self.show_router_buttom = QPushButton("S\nh\no\nw", self)
        self.show_router_buttom.setGeometry(580, 140, 41, 80)
        self.del_device_buttom = QPushButton("Del_Device", self)
        self.del_device_buttom.setGeometry(460, 180, 121, 41)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    sys.exit(app.exec_())
