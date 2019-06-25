# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'int_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from int_main_ui import *
from hist_ui import *
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import csv
import ibm_db
from statsmodels.tsa.statespace.sarimax import SARIMAX

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 316)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(146, 200, 104);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 110, 47, 13))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.txtDesde = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDesde.setGeometry(QtCore.QRect(110, 110, 113, 20))
        self.txtDesde.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDesde.setObjectName("txtDesde")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 110, 47, 13))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.txtHasta = QtWidgets.QLineEdit(self.centralwidget)
        self.txtHasta.setGeometry(QtCore.QRect(290, 110, 113, 20))
        self.txtHasta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtHasta.setObjectName("txtHasta")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 10, 551, 71))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 110, 71, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.cmbVariable = QtWidgets.QComboBox(self.centralwidget)
        self.cmbVariable.setGeometry(QtCore.QRect(500, 110, 91, 22))
        self.cmbVariable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cmbVariable.setObjectName("cmbVariable")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 150, 91, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 220, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.btnhist = QtWidgets.QPushButton(self.centralwidget)
        self.btnhist.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.btnhist.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);")
        self.btnhist.setObjectName("btnhist")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionpronosticos = QtWidgets.QAction(MainWindow)
        self.actionpronosticos.setCheckable(True)
        self.actionpronosticos.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.actionpronosticos.setFont(font)
        self.actionpronosticos.setObjectName("actionpronosticos")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.grafica)
        self.btnhist.clicked.connect(self.ventanaHist)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pronosticos Rent A Car"))
        self.label.setText(_translate("MainWindow", "Desde:"))
        self.label_2.setText(_translate("MainWindow", "Hasta:"))
        self.label_3.setText(_translate("MainWindow", "PRONOSTICOS RENT A CAR"))
        self.label_4.setText(_translate("MainWindow", "Variable:"))
        self.label_5.setText(_translate("MainWindow", "Pronostico:"))
        self.pushButton.setText(_translate("MainWindow", "ver grafica"))
        self.btnhist.setText(_translate("MainWindow", "Historial"))
        self.actionpronosticos.setText(_translate("MainWindow", "pronosticos"))

    def ventanaHist(self):
        self.historialVentana = QtWidgets.QMainWindow()
        self.ui = Ui_historialVentana()
        self.ui.setupUi(self.historialVentana)
        self.historialVentana.show()

    def grafica(self):

        """conn = ibm_db.connect(
            "DATABASE=RENTACAR;HOSTNAME=190.62.243.204;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=2525;", "", "")

        sql = 'SELECT c.sexo, integer(floor((current date - c.fecha_nacimiento)/10000 )) EDAD ,a.PLACA, a.ALQUILER_ID, a.FECHA_SALIDA, a.HORA_SALIDA,a.FECHA_ENTRADA,a.HORA_ENTRADA FROM "rentacar".ALQUILER a,  "rentacar".CLIENTES c where  a.CLIENTE_ID=c.CLIENTE_ID ORDER BY a.FECHA_SALIDA'
        stmt = ibm_db.exec_immediate(conn, sql)
        dictionary = (ibm_db.fetch_assoc(stmt))

        with open('prueba.csv', 'w', newline='') as csvfile:
            fieldnames = ['Genero_Usuario', 'Edad_Usuario', 'Placa', 'Alquiler_Id',
                          'Fecha_Retiro', 'Hora_Retiro', 'Fecha_Arribo', 'Hora_Arribo']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            while dictionary != False:
                writer.writerow({'Genero_Usuario': dictionary["SEXO"], 'Edad_Usuario': dictionary["EDAD"],
                                 'Placa': dictionary["PLACA"], 'Alquiler_Id': dictionary["ALQUILER_ID"],
                                 'Fecha_Retiro': dictionary["FECHA_SALIDA"], 'Hora_Retiro': dictionary["HORA_SALIDA"],
                                 'Fecha_Arribo': dictionary["FECHA_ENTRADA"],
                                 'Hora_Arribo': dictionary["HORA_ENTRADA"]})
                dictionary = ibm_db.fetch_assoc(stmt)"""

        viajes = pd.read_csv('prueba.csv')
        # concatenar Hora_Retiro y Fecha_Retiro
        viajes['fecha_hora_retiro'] = viajes.Fecha_Retiro + ' ' + viajes.Hora_Retiro

        # cambiar de str a datetime
        viajes['fecha_hora'] = viajes.fecha_hora_retiro \
            .map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

        # reindexar el dataframe
        viajes.index = viajes.fecha_hora

        # limpiar valores de otros años
        viajes = viajes.loc['2019-06']

        # resample y agregacion por dia de mes
        viajes_resample_day = viajes.Placa.resample('H').count()

        # asignar día de la semana
        df_resample = pd.concat([viajes_resample_day], axis=1)
        df_resample['dayofweek'] = df_resample.index.dayofweek  # 0 es lunes

        # lunes a viernes
        df_mon_to_fri = df_resample[df_resample.dayofweek.isin([0, 1, 2, 3, 4])].Placa

        # definir conjunto de datos
        x = df_mon_to_fri

        # instanciar modelo
        sarima_model = SARIMAX(x, order=(1, 1, 1), seasonal_order=(1, 1, 1, 24))

        # ajustar modelo
        results = sarima_model.fit()

        # mirar el AIC
        results.aic

        # tomar de datos originales dias 29-oct, 30-oct, y 31-oct
        df_29_31 = df_mon_to_fri.loc['2019-06-19':'2019-06-22']
        df_29_31.plot()

        # agregar bandas de confianza
        pred_1_2_conf = results.get_forecast(steps=24 * 2).conf_int()
        pred_1_2_conf.index = pd.date_range(start='2019-06-23', end='2019-06-25', freq='H')[:-1]
        x = pd.date_range(start='2019-06-23', end='2019-06-25', freq='H')[:-1]
        y1 = pred_1_2_conf['lower Placa']
        y2 = pred_1_2_conf['upper Placa']
        plt.fill_between(x, y1, y2, alpha=0.6)

        # predecir para 1-nov y 2-nov
        pred_1_2 = results.get_forecast(steps=24 * 2).predicted_mean
        pred_1_2.index = pd.date_range(start='2019-06-23', end='2019-06-25', freq='H')[:-1]
        pred_1_2.plot()

        # formato de la grafica final
        plt.title('Pronóstico de viajes')
        plt.ylabel('Cantidad de viajes')
        plt.xlabel('Semana lun-29-oct al vie-02-nov')
        plt.legend(('Datos originales octubre', 'Pronóstico noviembre'),
                   loc='lower left')
        plt.savefig('pronostico.png')
        plt.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

