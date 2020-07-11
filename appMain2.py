#多继承方法
import sys
from PyQt5.QtWidgets import QWidget,QApplication
from ui_formhello import Ui_Form

class QmyWidget(QWidget,Ui_Form):
     def __init__(self,parent=None):
         super(QmyWidget, self).__init__(parent)    #调用父类构造函数，创建QWidget窗体

         self.Lab="多重继承的QmyWidget"    #新定义的一个变量
         self.setupUi(self)       #self是QWidget窗体，可作为参数传给setupUi()
         self.label.setText(self.Lab)


if __name__ == "__main__":
    app = QApplication(sys.argv)  #创建app
    myWidget = QmyWidget()
    myWidget.show()
    myWidget.pushButton.setText("不关闭了")
    sys.exit(app.exec())