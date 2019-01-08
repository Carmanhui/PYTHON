# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class SerialThread(QtCore.QThread):
    dataReadoutSignal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None, portName='COM3', baudrate=9600, parity='N', bytesize=8, stopbits=1, timeout=None):
        super(SerialThread, self).__init__(parent)
        self.m_serialPort = serial.Serial()
        self.m_serialPort.port = portName
        self.m_serialPort.baudrate = baudrate
        self.m_serialPort.parity = parity
        self.m_serialPort.bytesize = bytesize
        self.m_serialPort.stopbits = stopbits
        self.m_serialPort.timeout = timeout
        self.OpenScom()

    def OpenScom(self):
        try:
            self.m_serialPort.open()
            self.m_serialPort.setRTS(True)
            self.m_serialPort.setDTR(True)
        except Exception as ex:
            print(ex)
        return ex

    def ScomSendOneData(self, datain):
        if isinstance(datain, int):
            listTemp = []
            listTemp.append(datain)
            d = bytes(listTemp)
            self.m_serialPort.write(d)
        elif isinstance(datain, str):
                d = datain.encode('utf-8')
                self.m_serialPort.write(d)

    def ScomGetintData(self):
        n = self.m_serialPort.inWaiting()
        if n:
            data = self.m_serialPort.read(n).hex()  # writefile
            print(data)

    def ScomGetstrData(self):
        if self.m_serialPort.is_open:
            n = self.m_serialPort.inWaiting()
            if n > 0:
                data = self.m_serialPort.read(n).decode('GB2312', errors='ignore')
        return data

    def run(self):
        cnt = 50
        while cnt <= 3000:
            sendstr = str(cnt)
            if len(sendstr) == 2:
                sendstr = '00' + sendstr
            elif len(sendstr) == 3:
                    sendstr = '0' + sendstr
            self.ScomSendOneData('SET' + sendstr + 'V')
            cnt = cnt + 5
            print('此时设置电压为：' + sendstr + 'V')
            time.sleep(2)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 511, 441))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 510, 271, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(550, 260, 241, 241))
        self.textEdit_2.setObjectName("textEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCaiji = QtWidgets.QAction(MainWindow)
        self.actionCaiji.setObjectName("actionCaiji")
        self.menu_2.addSeparator()
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "版权所有：河南科技大学"))
        self.pushButton.setText(_translate("MainWindow", "connect"))
        self.pushButton_2.setText(_translate("MainWindow", "添加数据"))
        self.label_2.setText(_translate("MainWindow", "数据记录表"))
        self.label_3.setText(_translate("MainWindow", "使用说明"))
        self.menu.setTitle(_translate("MainWindow", "开始"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.actionCaiji.setText(_translate("MainWindow", "caiji"))

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.scomList = []
        self.threadList = []
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.openMsg)
        self.actionSave.triggered.connect(self.saveMsg)
        self.pushButton.clicked.connect(self.ScomAutoFind)
        self.addDataButton.clicked.connect(self.getRHandT)

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels(['11', '22', '33', '44', '55'])
        self.tableRowCnt = 0
        self.tableColumnCnt = 0
        self.ThreadComID = 0
        self.addDatasignal = pyqtSignal(str)
        self.datadict = {'RHldy': 0, 'Tldy': 0, 'meaRT': 0, 'voltport': 0}

    def getMCUdata(self):
        if self.ThreadComID == 0:
            self.showMsgbox('请先连接串口')
        else:
            self.ThreadComID.ScomSendOneData(' 5501AA')
            time.sleep(0.1)
            strt = self.ThreadComID.ScomGetstrData()
            if strt is None:
                self.showMsgbox('请将串口线连接到电路板')
                return None
            print(strt)
            self.datadict['voltport'] = strt[4:-3] + '.' + strt[-3:-2]
            self.ThreadComID.ScomSendOneData(' 5502AA')
            time.sleep(0.1)
            strt = self.ThreadComID.ScomGetstrData()
            if strt is None:
                self.showMsgbox('请将串口线连接到电路板')
                return None
            print(strt)
            self.datadict['meaRT'] = strt[4:-4] + '.' + strt[-4:-2]
            return 1

    def insertTableNewLine(self):
        self.tableWidget.setItem(self.tableRowCnt, 0, QTableWidgetItem(self.datadict['RHldy']))
        self.tableWidget.setItem(self.tableRowCnt, 1, QTableWidgetItem(self.datadict['Tldy']))
        self.tableWidget.setItem(self.tableRowCnt, 2, QTableWidgetItem(self.datadict['meaRT']))
        self.tableWidget.setItem(self.tableRowCnt, 3, QTableWidgetItem(self.datadict['voltport']))
        self.tableWidget.setItem(self.tableRowCnt, 4, QTableWidgetItem(
            str(datetime.date.today()) + ' ' + str(datetime.datetime.today().hour) + ':' + str(
                datetime.datetime.today().minute)))
        self.tableRowCnt += 1
        self.tableWidget.insertRow(self.tableRowCnt)

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开记录表", "C:/", ".txt")

    def getRHandT(self):
        if self.ThreadComID == 0:
            self.showMsgbox('请先连接串口')
        else:
            data, ok = QInputDialog.getText(self, "露点仪数据",
                                            "按如下格式记录：\n  RH空格T\n示例：\n  RH(0~100):66.6\n  T(0~200):9.8\n  输入：66.6 9.8",
                                            QLineEdit.Normal, "66.6 9.8")
            if ok == True:
                data = re.findall('^[0-9]+\.[0-9]+\s+[0-9]+\.[0-9]+$', data.rstrip())
                if len(data) == 0:
                    self.showMsgbox('数据格式有误，重新录入')
                else:
                    data = data[0].split()
                    print(data)
                    self.datadict['RHldy'] = data[0]
                    self.datadict['Tldy'] = data[1]
                    if self.getMCUdata() is None:
                        return None
                        print(self.datadict)
                        self.insertTableNewLine()
                    else:
                        self.showMsgbox('请重新录入数据')

    def showMsgbox(self, strtoshow):
        QMessageBox.warning(self, '提示', strtoshow, QMessageBox.Ok)

    def saveMsg(self):
        file, ok = QFileDialog.getSaveFileName(self, "保存记录表", "C:/", ".txt")

    def ScomAutoFind(self):
        self.pushButton.setDisabled(True)
        self.scomList = list(serial.tools.list_ports.comports())
        if len(self.scomList) <= 0:
            self.showMsgbox('未发现串口，请检查线缆连接')
            self.pushButton.setDisabled(False)
        else:
            comNum = len(self.scomList)
            print(str(comNum) + 'Scom is found')
            while comNum:
                comNum = comNum - 1
                if "USB" in str(self.scomList[comNum]):
                    self.ThreadComID = SerialThread(portName=self.scomList[comNum][0])
                    self.ThreadComID.start()
                    self.graphicsView.setStyleSheet("background-color: rgb(0, 255, 0);")
                    print(str(self.scomList[comNum]) + ' is added')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    print('程序终止')
    sys.exit(app.exec_())