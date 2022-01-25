import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox


class Stats():
    def __init__(self) -> None:
        self.window = QMainWindow()
        self.window.resize(800, 400)
        self.window.move(300, 310)
        self.window.setWindowTitle('510Robot')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入啥")
        self.textEdit.move(25,25)
        self.textEdit.resize(500,350)

        self.button = QPushButton('电我', self.window)
        self.button.resize(80,60)
        self.button.move(600,150)

        self.button.clicked.connect(self.handleClick)

        self.window.show()
    
    def handleClick(self):
        print("阿，我被电击了!")
        QMessageBox.about(self.window,"tt","阿，我被电击了")

    def handleClick2(self):
        get_text = self.textEdit.toPlainText()
    

if __name__ == '__main__':    
    app = QApplication([])
    anInstance = Stats()
    anInstance.window.show()
    sys.exit(app.exec_())