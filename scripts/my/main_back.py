from p2design import Ui_Form
from PySide2 import QtWidgets, QtGui


class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setMouseTracking(True)

        self.ui.comboBox.addItems(["HEX", "DEC", "OCT", "BIN"])
        self.ui.pushButtonGET.setShortcut(QtGui.QKeySequence("F1"))

# signals
        self.ui.pushButtonLT.clicked.connect(self.onPBLTclicked)
        self.ui.pushButtonRT.clicked.connect(self.onPBRTclicked)
        self.ui.pushButtonLD.clicked.connect(self.onPBLDclicked)
        self.ui.pushButtonRD.clicked.connect(self.onPBRDclicked)

    def onPBLTclicked(self):
        self.move(0, 0)

    def onPBRTclicked(self):
        print(QtWidgets.QApplication.screenAt(self.pos()).size().width())
        print(self.width())
        self.move(QtWidgets.QApplication.screenAt(self.pos()).size().width() - self.width(), 0)

    def onPBLDclicked(self):
        print(QtWidgets.QApplication.screenAt(self.pos()).size().height())
        print(self.height())
        self.move(0, QtWidgets.QApplication.screenAt(self.pos()).size().height() - self.height() - 75)

    def onPBRDclicked(self):
        print(QtWidgets.QApplication.screenAt(self.pos()).size().height())
        print(self.height())
        self.move(QtWidgets.QApplication.screenAt(self.pos()).size().width() - self.width(), QtWidgets.QApplication.screenAt(self.pos()).size().height() - self.height() - 75)





if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MyWindow()
    win.show()

    app.exec_()