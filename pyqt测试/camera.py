# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    timer_camera = QtCore.QTimer()
    cap = cv2.VideoCapture()
    CAM_NUM = 0
    Picture_Num = 0
    Video_Num = 0
    flag = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 620)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 761, 471))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 530, 75, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 530, 75, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(44, 530, 181, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 530, 75, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer_camera.timeout.connect(self.show_camera)
        # 打开相机
        self.pushButton_4.clicked.connect(self.opencamera)
        # 截图
        self.pushButton_2.clicked.connect(self.screen)
        # 退出
        self.pushButton_5.clicked.connect(self.exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "魔法相机"))
        self.pushButton_2.setText(_translate("MainWindow", "截图"))
        self.pushButton_3.setText(_translate("MainWindow", "录像"))
        self.pushButton_4.setText(_translate("MainWindow", "打开相机"))
        self.pushButton_5.setText(_translate("MainWindow", "退出"))

    def opencamera(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == True:
                self.timer_camera.start(30)
                self.pushButton_4.setText(u'关闭相机')
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.label.clear()
            self.pushButton_4.setText(u'打开相机')

    def show_camera(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def screen(self):
        self.Picture_Num += 1
        self.pushButton_2.setText("继续")
        flag, self.image = self.cap.read()
        cv2.imwrite('./'+str(self.Picture_Num)+'.jpg',self.image)

    def videotape(self):
        pass

    def exit(self):
            QtCore.QCoreApplication.instance().quit()
            self.cap.release()
            self.timer_camera.stop()




