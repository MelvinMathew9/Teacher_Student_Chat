# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!
import requests
import urllib.request, json
from PyQt5 import QtCore, QtGui, QtWidgets
from a import Ui_MainWindow1

class Ui_MainWindow(object):
    def open(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow1()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(249, 303)
        MainWindow.setStyleSheet("background-colour:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.181818 rgba(0, 126, 255, 255), stop:1 rgba(147, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 251, 271))
        self.tabWidget.setStyleSheet("background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.181818 rgba(0, 126, 255, 255), stop:1 rgba(147, 255, 255, 255))")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(0, 40, 244, 20))
        self.lineEdit.setStyleSheet("background-color:white;\n"
"color:rgb(128, 128, 128)")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 80, 244, 20))
        self.lineEdit_2.setStyleSheet("background-color:white;\n"
"color:rgb(128, 128, 128)")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 140, 118, 23))
        self.pushButton_2.setStyleSheet("background-color:white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 10, 241, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 190, 241, 20))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 249, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "USERNAME"))
        self.lineEdit_2.setText(_translate("MainWindow", "PASSWORD"))
        self.pushButton_2.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton_2.clicked.connect(self.login)
        self.label.setText(_translate("MainWindow", "PROJECT NAME"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
    def login(self):
        user = ""
        userid = self.lineEdit.text()
        password =self.lineEdit_2.text()
        with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/StudentRegister.php") as url:
            data = json.loads(url.read().decode())
            for x in data['Details']:
                if (userid == x['UserID'] and password == x['Password']):
                    user = x['UserName']
                    self.label_2.setText("Successfully Loged IN")
                    self.open()
                    user_in = True
                    already_registered = True
                    break
                else:
                    already_registered = False
            if (already_registered == False):
                self.label_2.setText("Login UnSuccessfull")
                user_in = False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


