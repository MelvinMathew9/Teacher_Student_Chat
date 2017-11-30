# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student_Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import urllib.request, json
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
userid=""
d1=[]
class Ui_MainWindow_Stud(object):
    def setupUi(self, MainWindow_Stud):
        MainWindow_Stud.setObjectName("MainWindow_Stud")
        MainWindow_Stud.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow_Stud)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_ask = QtWidgets.QWidget()
        self.tab_ask.setObjectName("tab_ask")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_ask)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_ask)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_publicask = QtWidgets.QWidget()
        self.tab_publicask.setObjectName("tab_publicask")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_publicask)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.tab_publicask)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.tab_publicask)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_publicask)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_8.addWidget(self.lineEdit_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.tab_publicask)
        self.pushButton.setIconSize(QtCore.QSize(10, 16))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(self.tab_publicask)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.tabWidget_2.addTab(self.tab_publicask, "")
        self.tab_privateask = QtWidgets.QWidget()
        self.tab_privateask.setObjectName("tab_privateask")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_privateask)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem6 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_9.addItem(spacerItem6)
        self.label_4 = QtWidgets.QLabel(self.tab_privateask)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.tab_privateask)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem8)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_privateask)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_9.addWidget(self.pushButton_4)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem9)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_privateask)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_9.addWidget(self.textBrowser)
        spacerItem10 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_9.addItem(spacerItem10)
        self.label_8 = QtWidgets.QLabel(self.tab_privateask)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_privateask)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_9.addWidget(self.lineEdit)
        self.label_6 = QtWidgets.QLabel(self.tab_privateask)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_privateask)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_9.addWidget(self.lineEdit_2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_9.addItem(spacerItem11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_privateask)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_9.addItem(spacerItem14)
        self.label_7 = QtWidgets.QLabel(self.tab_privateask)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem15)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.tabWidget_2.addTab(self.tab_privateask, "")
        self.verticalLayout_3.addWidget(self.tabWidget_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_ask, "")
        self.tab_answer = QtWidgets.QWidget()
        self.tab_answer.setObjectName("tab_answer")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_answer)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.tab_answer)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.tab_answer)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_answer)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.pushButton_5)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_answer)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_5.addWidget(self.textBrowser_4)
        self.label_13 = QtWidgets.QLabel(self.tab_answer)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_answer)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_5.addWidget(self.lineEdit_5)
        self.label_12 = QtWidgets.QLabel(self.tab_answer)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_answer)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_5.addWidget(self.lineEdit_6)
        self.label_11 = QtWidgets.QLabel(self.tab_answer)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_answer)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_5.addWidget(self.lineEdit_4)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem16)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_answer)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem18)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem19 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem19)
        self.label_14 = QtWidgets.QLabel(self.tab_answer)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem20)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_answer, "")
        self.tab_notifications = QtWidgets.QWidget()
        self.tab_notifications.setObjectName("tab_notifications")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_notifications)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem21)
        self.label_17 = QtWidgets.QLabel(self.tab_notifications)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_notifications)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_7.addWidget(self.pushButton_6)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_notifications)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_11.addWidget(self.textBrowser_2)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.tabWidget.addTab(self.tab_notifications, "")
        self.tab_rewards = QtWidgets.QWidget()
        self.tab_rewards.setObjectName("tab_rewards")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_rewards)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem22)
        self.label_15 = QtWidgets.QLabel(self.tab_rewards)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_rewards)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_9.addWidget(self.pushButton_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_rewards)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_6.addWidget(self.textBrowser_3)
        self.label_16 = QtWidgets.QLabel(self.tab_rewards)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.label_18 = QtWidgets.QLabel(self.tab_rewards)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAutoFillBackground(False)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_rewards, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_13.addWidget(self.pushButton_8)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_10.addWidget(self.textBrowser_5)
        self.verticalLayout_13.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow_Stud.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_Stud)
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Stud)

    def retranslateUi(self, MainWindow_Stud):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Stud.setWindowTitle(_translate("MainWindow_Stud", "Students Corner"))
        self.label_2.setText(_translate("MainWindow_Stud", "Questions asked through this section will be displayed globally to all users, be it teachers or students!"))
        self.label_3.setText(_translate("MainWindow_Stud", "Enter your question:"))
        self.pushButton.setText(_translate("MainWindow_Stud", "SUBMIT"))
        self.pushButton.clicked.connect(self.submit_qn)
        self.pushButton_4.setText(_translate("MainWindow_Stud", "REFRESH"))
        self.pushButton_5.setText(_translate("MainWindow_Stud", "REFRESH"))
        self.pushButton_6.setText(_translate("MainWindow_Stud", "REFRESH"))
        self.pushButton_7.setText(_translate("MainWindow_Stud", "REFRESH"))
        self.pushButton_6.clicked.connect(self.notice)
        self.pushButton_5.clicked.connect(self.run)
        self.pushButton_4.clicked.connect(self.check)
        self.pushButton_7.clicked.connect(self.reward)
        self.label.setText(_translate("MainWindow_Stud", "Question Status"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_publicask), _translate("MainWindow_Stud", "Public"))
        self.label_4.setText(_translate("MainWindow_Stud", "Questions asked through this section will be displayed to the specified teacher, whose code is entered"))
        self.label_5.setText(_translate("MainWindow_Stud", "Make sure you enter both the teacher ID and question correctly!"))
        self.label_8.setText(_translate("MainWindow_Stud", "Enter teacher ID:"))
        self.label_6.setText(_translate("MainWindow_Stud", "Enter your question:"))
        self.pushButton_2.setText(_translate("MainWindow_Stud", "SUBMIT"))
        self.pushButton_2.clicked.connect(self.stu_ask_spec)
        self.label_7.setText(_translate("MainWindow_Stud", "Question status"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_privateask), _translate("MainWindow_Stud", "Private"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ask), _translate("MainWindow_Stud", "Ask"))
        self.label_9.setText(_translate("MainWindow_Stud", "Help answering questions asked by fellow students and earn points in the process!"))
        self.label_10.setText(_translate("MainWindow_Stud", "Available questions:"))
        self.label_13.setText(_translate("MainWindow_Stud", "Enter User ID of student whose question  you want to answer:"))
        self.label_12.setText(_translate("MainWindow_Stud", "Enter the question:"))
        self.label_11.setText(_translate("MainWindow_Stud", "Enter your answer:"))
        self.pushButton_3.setText(_translate("MainWindow_Stud", "SUBMIT"))
        self.pushButton_3.clicked.connect(self.sub_ans)
        self.label_14.setText(_translate("MainWindow_Stud",
                                         "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_answer), _translate("MainWindow_Stud", "Answer"))
        self.label_17.setText(_translate("MainWindow_Stud", "Latest notices from KTU:"))
        self.pushButton_6.setText(_translate("MainWindow_Stud", "REFRESH"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_notifications),
                                  _translate("MainWindow_Stud", "Notices"))
        self.label_15.setText(_translate("MainWindow_Stud", "View Leaderboard"))
        self.pushButton_7.setText(_translate("MainWindow_Stud", "REFRESH"))
        self.label_16.setText(_translate("MainWindow_Stud", "Current points total:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rewards), _translate("MainWindow_Stud", "Rewards"))
        self.pushButton_8.setText(_translate("MainWindow_Stud", "REFRESH"))
        self.label_18.setText(_translate("MainWindow_Stud", "0"))
        self.pushButton_8.clicked.connect(self.view)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  _translate("MainWindow_Stud", "View Your Questions"))

    def view(self):
        try:
            self.textBrowser_5.setText("")
            with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/ans_specific_view.php") as url:
                data = json.loads(url.read().decode())
                for x in data['ans']:
                    if(x['UserID']==userid):
                        if(x['ans']==""):
                            self.textBrowser_5.append(x['spec_id']+ ":  Did not answer your Question [ "+x['Ask_specific']+" ]")
                        else:
                            self.textBrowser_5.append(
                                x['spec_id'] + ": answered for [ " + x['Ask_specific'] + " ] as:"+x['ans'])
        except:
            self.textBrowser_5.setText("Network Error")
    def reward(self):
        try:
            us_id = ""
            reward = ""
            with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/reward_display.php") as url:
                data = json.loads(url.read().decode())
                counter = 0
                self.textBrowser_3.setText("")
                for x in data['s1s2']:
                    us_id = x['UserID']
                    reward = x['Rewards']
                    user1 = x['UserName']

                    if (counter < 5):
                            self.textBrowser_3.append(user1 + " Scored " + reward + " points")
                            if (userid == us_id):
                                self.textBrowser_3.append("Congrats you are on top 5")
                                self.label_18.setText(reward)
                                break
                    if (counter >= 5):
                            self.textBrowser_3.append(user1 + " Scored " + reward + " points")
                            if (userid == us_id):
                                self.textBrowser_3.append("Your reward " + reward + "Position" + counter)
                                self.label_18.setText(reward)
                                break
                            counter += 1
        except:
                    self.textBrowser_3.setText("Network Error")
    def submit_qn(self):
        try:
            qn = self.lineEdit_3.text()
            values = {'UserID':userid, 'ask_global': qn, 'ask_specific': "None", 'spec_id': "None"}
            data = requests.post("https://melvinmathew0102.000webhostapp.com/Student_main.php", values)
            if (data):
                self.label.setText("Entered Successfully")
        except:
            self.label.setText("Network Error")
    def notice(self):
        try:
            notification = "https://ktu.edu.in/eu/core/announcements.htm"
            uclient = uReq(notification)
            content_html = uclient.read()
            uclient.close()
            # html parsing3
            page_soup = soup(content_html, "html.parser")
            item_class = page_soup.find_all("div", {"class": "c-details"})
            # grab each

            for container in item_class:
                b = container.findAll("td")
                c = container.findAll("a")

                for j in range(0, len(b)):
                    content = b[j].text.strip()
                    if (content == b[j - 1].text.strip()):
                        self.textBrowser_2.append("")
                    else:
                        self.textBrowser_2.append(content)
        except:
            self.textBrowser_2.append("Network Error")
    def check(self):
        try:
            self.textBrowser.setText("Available Teachers")
            with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/Student_ask_specific.php") as url:
                data = json.loads(url.read().decode())
                for x in data['details']:
                    tid = x['T_ID']
                    tname = x['T_Name']
                    d1.append(tid)
                    self.textBrowser.append("\nTeacher ID:"+ tid+ " Teacher Name:"+ tname)
        except:
            self.textBrowser.append("Network Error")
    def sub_ans(self):
        try:
            uid = self.lineEdit_5.text()
            q = self.lineEdit_6.text()
            answered=True
            with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/Teacher_ans.php") as url:
                data = json.loads(url.read().decode())
                d={}
                for x in data['Questions']:
                    if (x['ans_by'] != 'None' and x['Ask_global'] == q and x['UserID'] == uid):
                        answered = True
                        break
                    else:
                        d.update({x['UserID']: x['Ask_global']})
                        answered = False

            if (uid == userid):
                self.label_14.setText("Dont try to earn reward by answering your own questions")
            elif (answered == False):
                question = q.strip()
                ans = self.lineEdit_4.text()
                if uid in d:
                    if(d[uid]==q):
                        values = {'UserID': uid, 'ans_by': userid, 'ans': ans, 'verified': 'No', 'question': q}
                        data = requests.post("https://melvinmathew0102.000webhostapp.com/ans_group.php", values)
                        self.label_14.setText("Entered Successfully")
                else:
                    self.label_14.setText("Check The Values Entered")
            elif (answered == True):
                self.label_14.setText("Already answered,Answer before others do,Be more Competitive")
        except:
             self.label_14.setText("Network Error")
    def stu_ask_spec(self):
        try:
            tid = self.lineEdit.text()
            qn =self.lineEdit_2.text()
            values = {'UserID': userid, 'ask': qn, 'T_id': tid}
            if tid in d1:
                data = requests.post("https://melvinmathew0102.000webhostapp.com/Student_ask_specific.php", values)
                if (data):
                  self.label_7.setText("Entered Successfully")
            else:
                self.label_7.setText("Check the values Entered")
        except:
            self.label_7.setText("Network Error")
    def run(self):
        try:
            data = ""
            answered = False
            self.textBrowser_4.setText("")
            with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/Teacher_ans.php") as url:
                data = json.loads(url.read().decode())
                for x in data['Questions']:
                    self.textBrowser_4.append("Student_ID-"+ x['UserID']+ ", "+ x['Username'] + " Asked " + x['Ask_global'])
                    self.textBrowser_4.append("\t"+ x['ans_by']+ " answered "+ x['ans'])
                    if (x['ans_by'] != 'None'):
                        self.textBrowser_4.append("\t"+ "Verified :"+ x['verified'])
        except:
            self.textBrowser_4.setText("Network Error")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Stud = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Stud()
    ui.setupUi(MainWindow_Stud)
    MainWindow_Stud.show()
    sys.exit(app.exec_())

