import sys

from PyQt5 import QtWidgets
import ui_formhello

app =QtWidgets.QApplication(sys.argv)
baseWidget = QtWidgets.QWidget()

ui = ui_formhello.Ui_Form()
ui.setupUi(baseWidget)

baseWidget.show()

sys.exit(app.exec_())