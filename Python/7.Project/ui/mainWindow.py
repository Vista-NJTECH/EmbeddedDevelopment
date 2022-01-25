from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import cv2
import sys, os, time
from threading import Thread
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0] + '/ui'
sys.path.append(rootPath)
import DBM

class Backstage():
    a = DBM.loginDB()
    def __init__(self):
        super().__init__()
        self.ifRun = 1
        self.initUI()
        
    def initUI(self):
        self.mainWindow = QMainWindow()
        self.mainWindow.resize(1000, 600)
        self.mainWindow.move(1600, 800)
        self.mainWindow.setWindowTitle('后台')

        self.dblistWindow = QTextBrowser(self.mainWindow)
        self.dblistWindow.move(50,350)
        self.dblistWindow.resize(150,200)
        self.dblistWindow.ensureCursorVisible()

        self.infoWindow = QTextBrowser(self.mainWindow)
        self.infoWindow.move(250,350)
        self.infoWindow.resize(400,200)

        self.checkUser_LineEdit = QLineEdit(self.mainWindow)
        self.checkUser_LineEdit.setPlaceholderText("输入账户")
        self.checkUser_LineEdit.move(700,350)
        self.checkUser_LineEdit.resize(150,25)

        self.checkUser_Button = QPushButton('Check', self.mainWindow)
        self.checkUser_Button.move(860,350)
        self.checkUser_Button.resize(50,25)

        self.allUser_Button = QPushButton('ALL', self.mainWindow)
        self.allUser_Button.move(920,350)
        self.allUser_Button.resize(50,25)

        self.camera_Label = QLabel(self.mainWindow)
        self.camera_Label.setFixedSize(480, 270)
        self.camera_Label.move(50, 50)
        self.camera_Label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}")

        self.camera_Button = QPushButton('Camera', self.mainWindow)
        self.camera_Button.move(600,60)
        self.camera_Button.resize(80,25)

        self.cameraStop_Button = QPushButton('Stop', self.mainWindow)
        self.cameraStop_Button.move(600,100)
        self.cameraStop_Button.resize(80,25)
        self.cameraStop_Button.setEnabled(False)

        self.allUser_Button.clicked.connect(self.dblist)
        self.checkUser_Button.clicked.connect(self.handlecheck)
        self.camera_Button.clicked.connect(self.getCameraT)
        self.cameraStop_Button.clicked.connect(self.stopCamera)
        
    def dblist(self):
        self.dblistWindow.clear()
        self.dblistWindow.append('user')
        self.dblistWindow.append('------------------------------')
        dataList = self.a.getAllData()
        for p in dataList:
            usertxt = p[1]
            self.dblistWindow.append(usertxt)

    def handlecheck(self):
        data = self.a.getPasswd(self.checkUser_LineEdit.text())
        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        if data:
            self.infoWindow.append("["+ localtime +"] " + self.checkUser_LineEdit.text()+' 的 密码是 : '+data)
        else:
            QMessageBox.warning(self.mainWindow, "Wrong", "无该用户记录")
            self.checkUser_LineEdit.clear()

    def getCameraT(self):
        self.ifRun = 1
        self.sub_thread = Thread(target = self.openCamera)
        self.sub_thread.start()

    def openCamera(self):
        self.camera_Button.setEnabled(False)
        self.cameraStop_Button.setEnabled(True)
        self.cap = cv2.VideoCapture(0)
        while self.ifRun == 1:
            ret, frame = self.cap.read()
            frame = cv2.resize(frame, (480, 270), interpolation=cv2.INTER_CUBIC)
            image_height, image_width, image_depth = frame.shape
            QIm = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            QIm = QImage(QIm.data, image_width, image_height,
                    image_width * image_depth,
                    QImage.Format_RGB888)
            self.camera_Label.setPixmap(QPixmap.fromImage(QIm))
        self.cap.release()
        cv2.destroyAllWindows()
    
    def stopCamera(self):
        self.ifRun = 0
        self.camera_Button.setEnabled(True)
        self.cameraStop_Button.setEnabled(False)

