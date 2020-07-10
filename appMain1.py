import sys

from PyQt5 import QtWidgets
import ui_formhello

app =QtWidgets.QApplication(sys.argv)
baseWidget = QtWidgets.QWidget()

ui = ui_formhello.Ui_Form()
ui.setupUi(baseWidget)

baseWidget.show()
ui.label.setText("Hello,被程序修改")
sys.exit(app.exec_())