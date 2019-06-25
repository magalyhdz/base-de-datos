# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       login.py
# Autor:        LUIS JOSE IRAHETA MEDRANO
# Copyright:    (c) 2019 LUIS IRAHETA
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *login* tiene como objetivo mostrar la forma de crear una ventana de login
sencilla.
"""

from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox, QApplication, QMainWindow, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton)

from int_main_ui import *
from hist_ui import *
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import csv
import ibm_db
from statsmodels.tsa.statespace.sarimax import SARIMAX
import ibm_db


#conn = ibm_db.connect("DATABASE=RENTACAR;HOSTNAME=190.62.243.204;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=2525;", "", "")

#ibm_db.close(conn)



# ===================== CLASE ventanaLogin =========================

class ventanaLogin(QMainWindow):
    def __init__(self, parent=None):
        super(ventanaLogin, self).__init__(parent)

        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("./assets/icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 500)

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(243, 243, 243))
        self.setPalette(paleta)
        self.initUI()


    def initUI(self):

      # ==================== FRAME ENCABEZADO ====================

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(51, 0, 102))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(400)
        frame.setFixedHeight(84)
        frame.move(0, 0)

        labelIcono = QLabel(frame)
        labelIcono.setFixedWidth(40)
        labelIcono.setFixedHeight(40)
        labelIcono.setPixmap(QPixmap("./assets/icono.png").scaled(40, 40, Qt.KeepAspectRatio,
                                                                  Qt.SmoothTransformation))
        labelIcono.move(37, 22)

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(20)
        fuenteTitulo.setBold(True)

        labelTitulo = QLabel("<font color='white'>Proyección</font>", frame)
        labelTitulo.setFont(fuenteTitulo)
        labelTitulo.move(90, 20)

        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(12)

        labelSubtitulo = QLabel("<font color='white'>Pronósticos de ventas"
                                ".</font>", frame)
        labelSubtitulo.setFont(fuenteSubtitulo)
        labelSubtitulo.move(115, 50)

        # ========================================================

        labelUsuario = QLabel("Usuario", self)
        labelUsuario.move(60, 170)

        frameUsuario = QFrame(self)
        frameUsuario.setFrameShape(QFrame.StyledPanel)
        frameUsuario.setFixedWidth(280)
        frameUsuario.setFixedHeight(28)
        frameUsuario.move(60, 196)

        imagenUsuario = QLabel(frameUsuario)
        imagenUsuario.setPixmap(QPixmap("./assets/usuario.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                       Qt.SmoothTransformation))
        imagenUsuario.move(10, 4)

        self.lineEditUsuario = QLineEdit(frameUsuario)
        self.lineEditUsuario.setFrame(False)
        self.lineEditUsuario.setTextMargins(8, 0, 4, 1)
        self.lineEditUsuario.setFixedWidth(238)
        self.lineEditUsuario.setFixedHeight(26)
        self.lineEditUsuario.move(40, 1)

        # ========================================================

        labelContrasenia = QLabel("Contraseña", self)
        labelContrasenia.move(60, 224)

        frameContrasenia = QFrame(self)
        frameContrasenia.setFrameShape(QFrame.StyledPanel)
        frameContrasenia.setFixedWidth(280)
        frameContrasenia.setFixedHeight(28)
        frameContrasenia.move(60, 250)

        imagenContrasenia = QLabel(frameContrasenia)
        imagenContrasenia.setPixmap(QPixmap("./assets/contrasena.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation))
        imagenContrasenia.move(10, 4)

        self.lineEditContrasenia = QLineEdit(frameContrasenia)
        self.lineEditContrasenia.setFrame(False)
        self.lineEditContrasenia.setEchoMode(QLineEdit.Password)
        self.lineEditContrasenia.setTextMargins(8, 0, 4, 1)
        self.lineEditContrasenia.setFixedWidth(238)
        self.lineEditContrasenia.setFixedHeight(26)
        self.lineEditContrasenia.move(40, 1)

      # ================== WIDGETS QPUSHBUTTON ===================

        buttonLogin = QPushButton("Iniciar sesión", self)
        buttonLogin.setFixedWidth(135)
        buttonLogin.setFixedHeight(28)
        buttonLogin.move(60, 286)

        buttonCancelar = QPushButton("Cancelar", self)
        buttonCancelar.setFixedWidth(135)
        buttonCancelar.setFixedHeight(28)
        buttonCancelar.move(205, 286)

      # ==================== MÁS INFORMACIÓN =====================

        labelInformacion = QLabel(
            "<a href='https://github.com/liluisjose1'>Más información</a>.", self)
        labelInformacion.setOpenExternalLinks(True)
        labelInformacion.setToolTip("Help")
        labelInformacion.move(15, 344)

      # ==================== SEÑALES BOTONES =====================

        buttonLogin.clicked.connect(self.Login)
        buttonCancelar.clicked.connect(self.close)

  # ======================= FUNCIONES ============================

    def Login(self):
        usuario = self.lineEditUsuario.text()
        contrasenia = self.lineEditContrasenia.text()

        """if conn:
            sql = 'select * from "rentacar".usuarios where usuario_id="admin" and contrasenia="admin1"'
            stmt = ibm_db.exec_immediate(conn, sql)
            result = ibm_db.fetch_both(stmt)
            while (result):
                print("Resultado", result)
                result = ibm_db.fetch_both(stmt)"""

        QMessageBox.warning(
        self, "info", "Conecto")
        self.lineEditUsuario.clear()
        self.lineEditContrasenia.clear()

        self.Ventana = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Ventana)
        self.Ventana.show()
        """else:
            QMessageBox.warning(
            self, "info", "Error")
            self.lineEditUsuario.clear() 
            self.lineEditContrasenia.clear()"""
        self.destroy()


    def keyPressEvent(self, event):
      if event.key() == Qt.Key_Return:
        self.Login()
      elif event.key() == Qt.Key_Escape:
        self.close()
      elif event.key() == Qt.Key_F1:
        QMessageBox.question(
            self, "Mensaje", "Oprimiste la tecla F1")

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
                             .map(lambda x : datetime.strptime(x, '%d/%m/%Y %H:%M:%S'))

        # reindexar el dataframe
        viajes.index = viajes.fecha_hora

        # limpiar valores de otros años
        viajes = viajes.loc['2019-06']

        # resample y agregacion por dia de mes
        viajes_resample_day = viajes.Placa.resample('H').count()

        # asignar día de la semana
        df_resample = pd.concat([viajes_resample_day], axis=1)
        df_resample['dayofweek'] = df_resample.index.dayofweek # 0 es lunes

        # lunes a viernes
        df_mon_to_fri = df_resample[df_resample.dayofweek.isin([0, 1, 2, 3, 4])].Placa



        # definir conjunto de datos
        x = df_mon_to_fri

        # instanciar modelo
        sarima_model = SARIMAX(x, order=(2, 0, 1), seasonal_order=(2, 1, 0, 24))

        # ajustar modelo
        results = sarima_model.fit()

        # mirar el AIC
        results.aic

        # tomar de datos originales dias 29-oct, 30-oct, y 31-oct
        df_29_31 = df_mon_to_fri.loc['2019-06-19':'2019-06-22']
        df_29_31.plot()

        # agregar bandas de confianza
        pred_1_2_conf = results.get_forecast(steps=24*2).conf_int()
        pred_1_2_conf.index = pd.date_range(start='2019-06-23', end='2019-06-25', freq='H')[:-1]
        x = pd.date_range(start='2019-06-23', end='2019-06-25', freq='H')[:-1]
        y1 = pred_1_2_conf['lower Placa']
        y2 = pred_1_2_conf['upper Placa']
        plt.fill_between(x, y1, y2, alpha=0.6)

        # predecir para 1-nov y 2-nov
        pred_1_2 = results.get_forecast(steps=24*2).predicted_mean
        pred_1_2.index = pd.date_range(start='2019-06-23', end='2019-06-25', freq='H')[:-1]
        pred_1_2.plot()

        # formato de la grafica final
        plt.title('Pronóstico de viajes')
        plt.ylabel('Cantidad de viajes')
        plt.xlabel('Semana lun-29-oct al vie-02-nov')
        plt.legend(('Datos originales junio', 'pronóstico junio'),
           loc='lower left')
        plt.savefig('pronostico.png')
        plt.show()

# ================================================================


if __name__ == '__main__':

    import sys
    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")

    aplicacion.setFont(fuente)

    ventana = ventanaLogin()
    ventana.show()

    sys.exit(aplicacion.exec_())
