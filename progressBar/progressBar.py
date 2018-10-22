from PySide import QtGui
from PySide import QtCore
import sys
import os

class MainWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        
        self.progressBar = QtGui.QProgressBar()
        
        self.execButton  = QtGui.QPushButton()
        self.execButton.setText("Execute!")
        
        itemLayout = QtGui.QHBoxLayout()
        itemLayout.addWidget(self.progressBar)
        itemLayout.addWidget(self.execButton)
        
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(itemLayout)

        self.setLayout(mainLayout)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWidget = MainWidget()
    mainWidget.show()
    app.exec_()
