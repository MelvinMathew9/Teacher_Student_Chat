# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Teacher_Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import random
import urllib.request, json
userid=""
l1=[]
l2=[]
l3=[]
l4=[]
class Ui_MainWindow_Teacher(object):

    def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(800, 600)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.verticalLayout = QtWidgets.QVBoxLayout()
            self.verticalLayout.setObjectName("verticalLayout")
            self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
            self.tabWidget.setObjectName("tabWidget")
            self.tab_answer = QtWidgets.QWidget()
            self.tab_answer.setObjectName("tab_answer")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_answer)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout()
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_answer)
            self.tabWidget_2.setObjectName("tabWidget_2")
            self.tab_2 = QtWidgets.QWidget()
            self.tab_2.setObjectName("tab_2")
            self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_2)
            self.horizontalLayout_8.setObjectName("horizontalLayout_8")
            self.verticalLayout_5 = QtWidgets.QVBoxLayout()
            self.verticalLayout_5.setObjectName("verticalLayout_5")
            self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_5.addItem(spacerItem)
            self.label_12 = QtWidgets.QLabel(self.tab_2)
            self.label_12.setObjectName("label_12")
            self.horizontalLayout_5.addWidget(self.label_12)
            self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
            self.pushButton_4.setObjectName("pushButton_4")
            self.horizontalLayout_5.addWidget(self.pushButton_4)
            self.verticalLayout_5.addLayout(self.horizontalLayout_5)
            self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
            self.textBrowser.setObjectName("textBrowser")
            self.verticalLayout_5.addWidget(self.textBrowser)
            spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_5.addItem(spacerItem1)
            self.label_9 = QtWidgets.QLabel(self.tab_2)
            self.label_9.setObjectName("label_9")
            self.verticalLayout_5.addWidget(self.label_9)
            self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
            self.lineEdit_5.setObjectName("lineEdit_5")
            self.verticalLayout_5.addWidget(self.lineEdit_5)
            self.label_10 = QtWidgets.QLabel(self.tab_2)
            self.label_10.setObjectName("label_10")
            self.verticalLayout_5.addWidget(self.label_10)
            self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
            self.lineEdit_6.setObjectName("lineEdit_6")
            self.verticalLayout_5.addWidget(self.lineEdit_6)
            self.label_11 = QtWidgets.QLabel(self.tab_2)
            self.label_11.setObjectName("label_11")
            self.verticalLayout_5.addWidget(self.label_11)
            self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
            self.lineEdit_7.setObjectName("lineEdit_7")
            self.verticalLayout_5.addWidget(self.lineEdit_7)
            self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
            self.pushButton_3.setObjectName("pushButton_3")
            self.verticalLayout_5.addWidget(self.pushButton_3)
            self.label_16 = QtWidgets.QLabel(self.tab_2)
            self.label_16.setObjectName("label_16")
            self.verticalLayout_5.addWidget(self.label_16)
            spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_5.addItem(spacerItem2)
            self.horizontalLayout_8.addLayout(self.verticalLayout_5)
            self.tabWidget_2.addTab(self.tab_2, "")
            self.verticalLayout_2.addWidget(self.tabWidget_2)
            self.horizontalLayout_2.addLayout(self.verticalLayout_2)
            self.tabWidget.addTab(self.tab_answer, "")
            self.tab_verify = QtWidgets.QWidget()
            self.tab_verify.setObjectName("tab_verify")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_verify)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.verticalLayout_3 = QtWidgets.QVBoxLayout()
            self.verticalLayout_3.setObjectName("verticalLayout_3")
            self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_7.setObjectName("horizontalLayout_7")
            spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_7.addItem(spacerItem3)
            self.label = QtWidgets.QLabel(self.tab_verify)
            self.label.setObjectName("label")
            self.horizontalLayout_7.addWidget(self.label)
            self.pushButton_5 = QtWidgets.QPushButton(self.tab_verify)
            self.pushButton_5.setObjectName("pushButton_5")
            self.horizontalLayout_7.addWidget(self.pushButton_5)
            self.verticalLayout_3.addLayout(self.horizontalLayout_7)
            self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_verify)
            self.textBrowser_2.setObjectName("textBrowser_2")
            self.verticalLayout_3.addWidget(self.textBrowser_2)
            self.label_2 = QtWidgets.QLabel(self.tab_verify)
            self.label_2.setObjectName("label_2")
            self.verticalLayout_3.addWidget(self.label_2)
            self.lineEdit = QtWidgets.QLineEdit(self.tab_verify)
            self.lineEdit.setObjectName("lineEdit")
            self.verticalLayout_3.addWidget(self.lineEdit)
            self.label_3 = QtWidgets.QLabel(self.tab_verify)
            self.label_3.setObjectName("label_3")
            self.verticalLayout_3.addWidget(self.label_3)
            self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_verify)
            self.lineEdit_2.setObjectName("lineEdit_2")
            self.verticalLayout_3.addWidget(self.lineEdit_2)
            self.label_13 = QtWidgets.QLabel(self.tab_verify)
            self.label_13.setObjectName("label_13")
            self.verticalLayout_3.addWidget(self.label_13)
            self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_verify)
            self.lineEdit_8.setObjectName("lineEdit_8")
            self.verticalLayout_3.addWidget(self.lineEdit_8)
            self.label_14 = QtWidgets.QLabel(self.tab_verify)
            self.label_14.setObjectName("label_14")
            self.verticalLayout_3.addWidget(self.label_14)
            self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_verify)
            self.lineEdit_9.setObjectName("lineEdit_9")
            self.verticalLayout_3.addWidget(self.lineEdit_9)
            self.label_15 = QtWidgets.QLabel(self.tab_verify)
            self.label_15.setObjectName("label_15")
            self.verticalLayout_3.addWidget(self.label_15)
            self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_verify)
            self.lineEdit_10.setObjectName("lineEdit_10")
            self.verticalLayout_3.addWidget(self.lineEdit_10)
            spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_3.addItem(spacerItem4)
            self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_6.setContentsMargins(-1, 0, 0, -1)
            self.horizontalLayout_6.setObjectName("horizontalLayout_6")
            spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_6.addItem(spacerItem5)
            self.pushButton = QtWidgets.QPushButton(self.tab_verify)
            self.pushButton.setObjectName("pushButton")
            self.horizontalLayout_6.addWidget(self.pushButton)
            spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_6.addItem(spacerItem6)
            self.verticalLayout_3.addLayout(self.horizontalLayout_6)
            spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_3.addItem(spacerItem7)
            self.label_4 = QtWidgets.QLabel(self.tab_verify)
            self.label_4.setObjectName("label_4")
            self.verticalLayout_3.addWidget(self.label_4)
            spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_3.addItem(spacerItem8)
            self.horizontalLayout_3.addLayout(self.verticalLayout_3)
            self.tabWidget.addTab(self.tab_verify, "")
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName("tab")
            self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab)
            self.horizontalLayout_9.setObjectName("horizontalLayout_9")
            self.verticalLayout_4 = QtWidgets.QVBoxLayout()
            self.verticalLayout_4.setObjectName("verticalLayout_4")
            spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_4.addItem(spacerItem9)
            self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_10.setContentsMargins(-1, 0, 0, -1)
            self.horizontalLayout_10.setObjectName("horizontalLayout_10")
            spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_10.addItem(spacerItem10)
            self.pushButton_6 = QtWidgets.QPushButton(self.tab)
            self.pushButton_6.setObjectName("pushButton_6")
            self.horizontalLayout_10.addWidget(self.pushButton_6)
            spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_10.addItem(spacerItem11)
            self.verticalLayout_4.addLayout(self.horizontalLayout_10)
            spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_4.addItem(spacerItem12)
            self.label_17 = QtWidgets.QLabel(self.tab)
            self.label_17.setObjectName("label_17")
            self.verticalLayout_4.addWidget(self.label_17)
            spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_4.addItem(spacerItem13)
            self.horizontalLayout_9.addLayout(self.verticalLayout_4)
            self.tabWidget.addTab(self.tab, "")
            self.verticalLayout.addWidget(self.tabWidget)
            self.horizontalLayout.addLayout(self.verticalLayout)
            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            self.tabWidget.setCurrentIndex(2)
            self.tabWidget_2.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_12.setText(_translate("MainWindow", "Questions"))
        self.pushButton_4.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_4.clicked.connect(self.view)
        self.label_9.setText(_translate("MainWindow", "Student_ID:"))
        self.label_10.setText(_translate("MainWindow", "Question:"))
        self.label_11.setText(_translate("MainWindow", "Answer:"))
        self.pushButton_3.setText(_translate("MainWindow", "SUBMIT"))
        self.pushButton_3.clicked.connect(self.ans)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Private"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_answer), _translate("MainWindow", "Answer"))
        self.label.setText(_translate("MainWindow", "Verify answers answered by students on  the public forums:"))
        self.pushButton_5.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_5.clicked.connect(self.view1)
        self.label_2.setText(_translate("MainWindow", "Student ID:"))
        self.label_3.setText(_translate("MainWindow", "Question:"))
        self.label_13.setText(_translate("MainWindow", "Answered_Student_ID:"))
        self.label_14.setText(_translate("MainWindow", "ANS"))
        self.label_15.setText(_translate("MainWindow", "Verify:"))
        self.pushButton.setText(_translate("MainWindow", "VERIFY"))
        self.pushButton.clicked.connect(self.verify)
        self.label_4.setText(_translate("MainWindow", "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_verify), _translate("MainWindow", "Verify"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Logout"))
        self.pushButton_6.setText(_translate("MainWindow", "Logout"))
        self.label_16.setText(_translate("MainWindow", ""))
    def view(self):
        try:
            with urllib.request.urlopen(
                    "https://melvinmathew0102.000webhostapp.com/teacher_question_display.php")as url:
                data = json.loads(url.read().decode())
                counter = 0
                for a in data['details']:
                    if (userid == a['T_ID']):
                        counter += 1
                        if(counter==1):
                            self.textBrowser.setText("Student id:" + a['Stud_ID'] + " asked " + a['Question'])
                        else:
                            self.textBrowser.append("Student id:" + a['Stud_ID'] + " asked " + a['Question'])
                        if (a['Ans_Specific'] != ''):
                            self.textBrowser.append("You answered: " + a['Ans_Specific'])
                    elif (counter == 0):
                        self.textBrowser.append("NO STUDENT ASKED ANY QUESTION")
                        break
        except:
            self.textBrowser.append("Network Error failed to refresh")

    def ans(self):
        try:

            answered = False
            uid = self.lineEdit_5.text()
            q = self.lineEdit_6.text()
            l1=[]
            l2=[]
            with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/teacher_question_display.php") as url:
                data = json.loads(url.read().decode())
                for x in data['details']:
                    l1.append(x['Stud_ID'])
                    l2.append(x['Question'])
                    if (x['Ans_Specific'] != '' and x['Question'] == q and x['Stud_ID'] == uid):
                        answered = True
                        break
                    else:
                        answered = False
            if (answered == False):
                question = q.strip()
                ans = self.lineEdit_7.text()
                print(l1)
                print(l2)
                if uid in l1:
                    if q in l2:
                        values = {'Stud_id': uid, 'ans_specific': ans, 'spec_id': userid, 'verified': 'Yes', 'Question': q}
                        data = requests.post("https://melvinmathew0102.000webhostapp.com/Teacher_ans_specific.php", values)
                        if (data):
                            self.label_16.setText("Entered Successfully")
                    else:
                            self.label_16.setText("Check The Entered Value")
                else:
                    self.label_16.setText("Check The Entered Value")
        except:
            self.label_16.setText("Network Error")

    def view1(self):
        try:
             with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/Teacher_ans.php") as url:
                data = json.loads(url.read().decode())
                counter=0
                for x in data['Questions']:
                    counter+=1
                    if(counter==1):
                        self.textBrowser_2.setText("Student_ID: "+ x['UserID']+ ", "+ x['Username'] + " Asked " + x['Ask_global'])
                    else:
                        self.textBrowser_2.append(
                            "Student_ID: " + x['UserID'] + ", " + x['Username'] + " Asked " + x['Ask_global'])
                        self.textBrowser_2.append("\t"+ x['ans_by']+ " answered "+ x['ans'])
                        l1.append(x['ans_by'])
                        l2.append(x['ans'])
                        l3.append(x['UserID'])
                        l4.append(x['Ask_global'])
                        if (x['ans_by'] != 'None'):
                            self.textBrowser_2.append("\t"+ "Verified :"+ x['verified'])
        except:
            self.textBrowser_2.append("Network Error")
    def verify(self):
        try:
            uid =self.lineEdit.text()
            q = self.lineEdit_2.text()
            answer_id = self.lineEdit_8.text()
            answer = self.lineEdit_9.text()
            rew=self.lineEdit_10.text()
            if(rew.lower()=='yes'):
                if uid in l3:
                    if q in l4:
                        if answer_id in l1:
                            if answer in l2:
                                values = {'UserID': uid, 'ans_by': answer_id, 'ans': answer, 'verified': rew, 'question': q}
                                data = requests.post("https://melvinmathew0102.000webhostapp.com/ans_group.php", values)
                                if (data):
                                    self.label_4.setText("Entered Successfully")
                                    reward = [5, 10, 15, 20]
                                    ran_reward = random.choice(reward)
                                    values = {'userid': answer_id, 'reward': ran_reward}
                                    data = requests.post("https://melvinmathew0102.000webhostapp.com/reward.php", values)
                                    if (data):
                                        self.label_4.setText("Rewarded Successfully")
                            else:
                                 self.label_4.setText("Check Values entered")
                        else:
                                self.label_4.setText("Check Values entered")
                    else:
                        self.label_4.setText("Check Values entered")
                else:
                    self.label_4.setText("Check Values entered")

            elif (rew == 'no'):
                if uid in l3:
                    if q in l4:
                        if answer_id in l1:
                            if answer in l2:
                                values = {'UserID': uid, 'ans_by': 'None', 'ans': '', 'verified': 'NO', 'question': q}
                                requests.post("https://melvinmathew0102.000webhostapp.com/ans_group.php", values)
                                self.label_4.setText("Entered Successfully")
                            else:
                                self.label_4.setText("Check Values entered")
                        else:
                            self.label_4.setText("Check Values entered")
                    else:
                        self.label_4.setText("Check Values entered")
                else:
                    self.label_4.setText("Check Values entered")
        except:
            self.label_4.setText("Network Error")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Teacher()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

