# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'S:\PM\ter\ets\Inter_Setor\COMPARTILHADO\PROJETOS\Mecatrônica_2_Turma\Grupo_4\5_PROGRAMAÇÃO\CODIGO\Programa\Registros_historico_utilizacao.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cadastros_historico_utilizacao(object):
    def setupUi(self, cadastros_historico_utilizacao):
        cadastros_historico_utilizacao.setObjectName("cadastros_historico_utilizacao")
        cadastros_historico_utilizacao.resize(1290, 841)
        cadastros_historico_utilizacao.setMinimumSize(QtCore.QSize(1290, 841))
        cadastros_historico_utilizacao.setMaximumSize(QtCore.QSize(1290, 841))
        cadastros_historico_utilizacao.setStyleSheet("background-color: rgb(255, 255, 255);")
        cadastros_historico_utilizacao.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(cadastros_historico_utilizacao)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_Borda = QtWidgets.QLabel(self.centralwidget)
        self.Label_Borda.setGeometry(QtCore.QRect(0, 783, 1290, 18))
        self.Label_Borda.setText("")
        self.Label_Borda.setPixmap(QtGui.QPixmap("S:\\PM\\ter\\ets\\Inter_Setor\\COMPARTILHADO\\PROJETOS\\Mecatrônica_2_Turma\\Grupo_4\\5_PROGRAMAÇÃO\\CODIGO\\Programa\\Imagens/Borda.png"))
        self.Label_Borda.setScaledContents(True)
        self.Label_Borda.setObjectName("Label_Borda")
        self.tabela_utilizacao = QtWidgets.QTableWidget(self.centralwidget)
        self.tabela_utilizacao.setGeometry(QtCore.QRect(30, 10, 1231, 611))
        self.tabela_utilizacao.setStyleSheet("font: 75 20pt \"Bosch Sans Bold\";")
        self.tabela_utilizacao.setObjectName("tabela_utilizacao")
        self.tabela_utilizacao.setColumnCount(2)
        self.tabela_utilizacao.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_utilizacao.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_utilizacao.setHorizontalHeaderItem(1, item)
        self.botao_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_voltar.setGeometry(QtCore.QRect(100, 635, 271, 131))
        self.botao_voltar.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"border-radius: 30px;\n"
"\n"
"font: 75 34pt \"Bosch Sans Bold\";\n"
"background-color: rgb(255,207,0);")
        self.botao_voltar.setObjectName("botao_voltar")
        self.botao_analisar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_analisar.setGeometry(QtCore.QRect(910, 635, 271, 131))
        self.botao_analisar.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"border-radius: 30px;\n"
"\n"
"font: 75 35pt \"Bosch Sans Bold\";\n"
"background-color: rgb(0,136,74);")
        self.botao_analisar.setObjectName("botao_analisar")
        cadastros_historico_utilizacao.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cadastros_historico_utilizacao)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 21))
        self.menubar.setObjectName("menubar")
        cadastros_historico_utilizacao.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cadastros_historico_utilizacao)
        self.statusbar.setObjectName("statusbar")
        cadastros_historico_utilizacao.setStatusBar(self.statusbar)

        self.retranslateUi(cadastros_historico_utilizacao)
        QtCore.QMetaObject.connectSlotsByName(cadastros_historico_utilizacao)

    def retranslateUi(self, cadastros_historico_utilizacao):
        _translate = QtCore.QCoreApplication.translate
        cadastros_historico_utilizacao.setWindowTitle(_translate("cadastros_historico_utilizacao", "MainWindow"))
        item = self.tabela_utilizacao.horizontalHeaderItem(0)
        item.setText(_translate("cadastros_historico_utilizacao", "DATA"))
        item = self.tabela_utilizacao.horizontalHeaderItem(1)
        item.setText(_translate("cadastros_historico_utilizacao", "EDV"))
        self.botao_voltar.setWhatsThis(_translate("cadastros_historico_utilizacao", "<html><head/><body><p><span style=\" color:#ffffff;\">OI</span></p></body></html>"))
        self.botao_voltar.setText(_translate("cadastros_historico_utilizacao", "VOLTAR"))
        self.botao_analisar.setWhatsThis(_translate("cadastros_historico_utilizacao", "<html><head/><body><p><span style=\" color:#ffffff;\">OI</span></p></body></html>"))
        self.botao_analisar.setText(_translate("cadastros_historico_utilizacao", "ANALISAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cadastros_historico_utilizacao = QtWidgets.QMainWindow()
    ui = Ui_cadastros_historico_utilizacao()
    ui.setupUi(cadastros_historico_utilizacao)
    cadastros_historico_utilizacao.show()
    sys.exit(app.exec_())
