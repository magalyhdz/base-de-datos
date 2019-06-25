# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hist.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_historialVentana(object):
    def setupUi(self, historialVentana):
        historialVentana.setObjectName("historialVentana")
        historialVentana.resize(550, 476)
        historialVentana.setStyleSheet("background-color: rgb(146, 200, 104);")
        self.centralwidget = QtWidgets.QWidget(historialVentana)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 511, 61))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        historialVentana.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(historialVentana)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        historialVentana.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(historialVentana)
        self.statusbar.setObjectName("statusbar")
        historialVentana.setStatusBar(self.statusbar)

        self.retranslateUi(historialVentana)
        QtCore.QMetaObject.connectSlotsByName(historialVentana)

    def retranslateUi(self, historialVentana):
        _translate = QtCore.QCoreApplication.translate
        historialVentana.setWindowTitle(_translate("historialVentana", "Historial"))
        self.label_3.setText(_translate("historialVentana", "HISTORIAL DE PRONOSTICOS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    historialVentana = QtWidgets.QMainWindow()
    ui = Ui_historialVentana()
    ui.setupUi(historialVentana)
    historialVentana.show()
    sys.exit(app.exec_())

