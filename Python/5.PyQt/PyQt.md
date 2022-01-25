# PyQt
PyQt的本质便是Qt，只是通过Python进行了封装。
我们先来来安装一个pyqt5
For linux:
```shell
pip install pyqt5-tools
```
虽然pyside2是亲儿子，但pyqt发布早，影响广泛，我们就用pyqt5了，其实二者的接口几乎一样，没啥改的。
## 0.一个例子

```python
#导入QT库
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit，QMessageBox

#实例化一个管家QApplication,用于调配系统资源，管理接口，分派用户任务给各个控件。
app = QApplication([])

#定义一个主窗口对象
window = QMainWindow()
#决定主窗口大小
window.resize(800, 400)
#出现在显示器屏幕的位置（x,y）----（0.0）原点为左上角
window.move(300, 310)
#标题
window.setWindowTitle('510Robot')

#定义文本编辑框对象（在window主窗口中）
textEdit = QPlainTextEdit(window)
#提示文本
textEdit.setPlaceholderText("请输入啥")

textEdit.resize(500,350)
#相对于主窗口对象的位置
textEdit.move(25,25)

#定义一个按钮对象
button = QPushButton('电我', window)
button.resize(80,60)
button.move(600,150)

#展现窗口
window.show()

#进入事件处理循环
app.exec_()
```

## 1.signal

当控件被（点击了，输入文本了......）会发出一个 `signal`

#### button控件

我们先定义一个函数

```python
def handleClick():
    print("阿，我被电击了！")
```

ok,在第一个例子中，我们定义了一个按钮 `button`,然后电它。

```python
def handleClick():
    print("阿，我被电击了！")

button = QPushButton('电我', window)
button.resize(80,60)
button.move(600,150)

button.clicked.connect(handleClick)
```

#### text控件

来来来

```python
def handleClick2():
    get_text = textEdit.toPlainText()
    QMessageBox.about(window,"阿"，"我被电了")
```
这样，当你点击`点我`是，就是弹出消息框。
about函数定义如下
```
about(主窗口，"消息窗口名","消息")
```
它属于QMessageBox类，因此在开头我们还要
```python
from PyQt5.QtWidgets import QMessageBox
```
#### 其他控件
由于控件比较多，我们遵循 了解基础，即查即用 的原则，这里不一一赘述了。
## 2.封装
学过了之前python的函数及类，我们也可以对qt进行封装以方便阅读与便携代码。
```python
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
```
上述代码便是封装完的，注意观察区别。
然后是调用。
```python
此if判断表示改.py文件为主文件，只有用户执行才能执行改语句块
if __name__ == '__main__':    
    app = QApplication([])
    #实例化一个对象
    anInstance = Stats()
    #调用对象的函数
    anInstance.window.show()

    sys.exit(app.exec_())
```