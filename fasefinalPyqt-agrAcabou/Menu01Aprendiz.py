# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu01Aprendiz.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu01Aprendiz(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1290, 841)
        MainWindow.setMinimumSize(QtCore.QSize(1275, 841))
        MainWindow.setMaximumSize(QtCore.QSize(1290, 841))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Botao_Documentos = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_Documentos.setGeometry(QtCore.QRect(672, 240, 240, 240))
        self.Botao_Documentos.setStyleSheet("border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;")
        self.Botao_Documentos.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/DOCUMENTOS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Botao_Documentos.setIcon(icon)
        self.Botao_Documentos.setIconSize(QtCore.QSize(220, 220))
        self.Botao_Documentos.setObjectName("Botao_Documentos")
        self.Botao_Liberar_Maquina = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_Liberar_Maquina.setGeometry(QtCore.QRect(63, 240, 240, 240))
        self.Botao_Liberar_Maquina.setStyleSheet("border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;")
        self.Botao_Liberar_Maquina.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagens/CADEADO_FECHADO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Botao_Liberar_Maquina.setIcon(icon1)
        self.Botao_Liberar_Maquina.setIconSize(QtCore.QSize(220, 220))
        self.Botao_Liberar_Maquina.setObjectName("Botao_Liberar_Maquina")
        self.Botao_Interface_Didatica = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_Interface_Didatica.setGeometry(QtCore.QRect(365, 240, 240, 240))
        self.Botao_Interface_Didatica.setStyleSheet("border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;")
        self.Botao_Interface_Didatica.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagens/INTERFACE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Botao_Interface_Didatica.setIcon(icon2)
        self.Botao_Interface_Didatica.setIconSize(QtCore.QSize(220, 220))
        self.Botao_Interface_Didatica.setObjectName("Botao_Interface_Didatica")
        self.Botao_Registros = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_Registros.setGeometry(QtCore.QRect(980, 240, 240, 240))
        self.Botao_Registros.setStyleSheet("border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;")
        self.Botao_Registros.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imagens/REGISTROS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Botao_Registros.setIcon(icon3)
        self.Botao_Registros.setIconSize(QtCore.QSize(220, 220))
        self.Botao_Registros.setObjectName("Botao_Registros")
        self.Label_Borda = QtWidgets.QLabel(self.centralwidget)
        self.Label_Borda.setGeometry(QtCore.QRect(0, 783, 1290, 18))
        self.Label_Borda.setText("")
        self.Label_Borda.setPixmap(QtGui.QPixmap("Imagens/Borda.png"))
        self.Label_Borda.setScaledContents(True)
        self.Label_Borda.setObjectName("Label_Borda")
        self.Label_Menu_De_Usuario = QtWidgets.QLabel(self.centralwidget)
        self.Label_Menu_De_Usuario.setGeometry(QtCore.QRect(210, 40, 875, 121))
        self.Label_Menu_De_Usuario.setStyleSheet("border-style: outset;\n"
"\n"
"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:0px;\n"
"\n"
"font: 75 65pt \"Bosch Sans Bold\";")
        self.Label_Menu_De_Usuario.setObjectName("Label_Menu_De_Usuario")
        self.Label_Colaborador = QtWidgets.QLabel(self.centralwidget)
        self.Label_Colaborador.setGeometry(QtCore.QRect(60, 650, 591, 41))
        self.Label_Colaborador.setStyleSheet("border-style: outset;\n"
"\n"
"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:0px;\n"
"\n"
"font: 75 15pt \"Bosch Sans Bold\";")
        self.Label_Colaborador.setObjectName("Label_Colaborador")
        self.Label_EDV = QtWidgets.QLabel(self.centralwidget)
        self.Label_EDV.setGeometry(QtCore.QRect(60, 700, 371, 41))
        self.Label_EDV.setStyleSheet("border-style: outset;\n"
"\n"
"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:0px;\n"
"\n"
"font: 75 15pt \"Bosch Sans Bold\";")
        self.Label_EDV.setObjectName("Label_EDV")
        self.Botao_Sair = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_Sair.setGeometry(QtCore.QRect(1110, 630, 121, 121))
        self.Botao_Sair.setStyleSheet("border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"borde:none;")
        self.Botao_Sair.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imagens/SAIR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Botao_Sair.setIcon(icon4)
        self.Botao_Sair.setIconSize(QtCore.QSize(130, 150))
        self.Botao_Sair.setObjectName("Botao_Sair")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Botao_Liberar_Maquina.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Label_Menu_De_Usuario.setText(_translate("MainWindow", "ACCESS CONTROL"))
        self.Label_Colaborador.setText(_translate("MainWindow", "COLABORADOR:"))
        self.Label_EDV.setText(_translate("MainWindow", "EDV:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Menu01Aprendiz()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())