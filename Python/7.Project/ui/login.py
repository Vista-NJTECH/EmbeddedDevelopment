import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox, QLineEdit

import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0] + '/ui'
sys.path.append(rootPath)
import DBM, mainWindow

class loginUi():
    a = DBM.loginDB()

    def __init__(self):
        super().__init__()
        self.initUI()
            
    def initUI(self):
        self.nextWindow = mainWindow.Backstage()
        self.window = QMainWindow()
        self.window.resize(400, 200)
        self.window.move(1600, 1000)
        self.window.setWindowTitle('Login')

        self.registerWindow = QMainWindow()
        self.registerWindow.resize(400, 200)
        self.registerWindow.move(1600, 1000)
        self.registerWindow.setWindowTitle('Register')
        
        self.account_LineEdit = QLineEdit(self.window)
        self.account_LineEdit.setPlaceholderText("请输入账号")
        self.account_LineEdit.move(125,25)
        self.account_LineEdit.resize(150,25)

        self.passwd_LineEdit = QLineEdit(self.window)
        self.passwd_LineEdit.setPlaceholderText("请输入密码")
        self.passwd_LineEdit.move(125,60)
        self.passwd_LineEdit.resize(150,25)

        self.register_account_LineEdit = QLineEdit(self.registerWindow)
        self.register_account_LineEdit.setPlaceholderText("请输入账号")
        self.register_account_LineEdit.move(125,25)
        self.register_account_LineEdit.resize(150,25)

        self.register_passwd_LineEdit = QLineEdit(self.registerWindow)
        self.register_passwd_LineEdit.setPlaceholderText("请输入密码")
        self.register_passwd_LineEdit.move(125,60)
        self.register_passwd_LineEdit.resize(150,25)

        self.loginButton = QPushButton('Login', self.window)
        self.loginButton.resize(80,40)
        self.loginButton.move(100,120)

        self.registerButton = QPushButton('Register', self.window)
        self.registerButton.resize(80,40)
        self.registerButton.move(220,120)

        self.confirmButton = QPushButton('Confirm', self.registerWindow)
        self.confirmButton.resize(80,40)
        self.confirmButton.move(160,120)

        self.loginButton.clicked.connect(self.loginClick)
        self.registerButton.clicked.connect(self.registerClick)
        self.confirmButton.clicked.connect(self.confirmClick)

    def loginClick(self):
        account = self.account_LineEdit.text()
        passwd = self.passwd_LineEdit.text()

        checkResult = self.a.checkDB(account, passwd)
        if checkResult == None:
            QMessageBox.about(self.window, "结果", '没有该用户')
            self.account_LineEdit.clear()
            self.passwd_LineEdit.clear()
        elif checkResult == 0:
            QMessageBox.about(self.window, "结果", '密码错误')
            self.account_LineEdit.clear()
            self.passwd_LineEdit.clear()
        elif checkResult == 1:
            QMessageBox.about(self.window, "结果", '登陆成功')
            self.window.close()
            self.nextWindow.mainWindow.show()


    def registerClick(self):
        self.registerWindow.show()

    def confirmClick(self):
        self.registerWindow.show()
        register_account = self.register_account_LineEdit.text()
        register_passwd = self.register_passwd_LineEdit.text()
        checkResult = self.a.checkDB(register_account, register_passwd)
        if checkResult != None:
            QMessageBox.about(self.registerWindow, "结果", '该用户已存在')
        elif register_account == None or register_passwd == None:
            QMessageBox.about(self.registerWindow, "结果", '创建失败，请重新输入')
        else:
            self.a.insertDB(register_account, register_passwd)
            QMessageBox.about(self.registerWindow, "结果", '创建成功')
            self.registerWindow.close()

    def __del__(self):
        self.nextWindow.ifRun = 0