import sys
sys.path[0] = sys.path[0] + '/ui'
#print(sys.path)
from login import loginUi
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':    
    app = QApplication([])
    anInstance = loginUi()
    anInstance.window.show()
    sys.exit(app.exec_())