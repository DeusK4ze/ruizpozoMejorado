# Form implementation generated from reading ui file '.\Templates\dlgBuscar.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgBuscar(object):
    def setupUi(self, dlgBuscar):
        dlgBuscar.setObjectName("dlgBuscar")
        dlgBuscar.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        dlgBuscar.resize(400, 70)
        dlgBuscar.setMinimumSize(QtCore.QSize(400, 70))
        dlgBuscar.setMaximumSize(QtCore.QSize(400, 70))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Templates\\../img/lupa.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgBuscar.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=dlgBuscar)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 321, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textoBuscarDlg = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.textoBuscarDlg.setObjectName("textoBuscarDlg")
        self.horizontalLayout.addWidget(self.textoBuscarDlg)
        self.botonBuscarDlg = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.botonBuscarDlg.setIcon(icon)
        self.botonBuscarDlg.setObjectName("botonBuscarDlg")
        self.horizontalLayout.addWidget(self.botonBuscarDlg)
        self.lblBuscarInfo = QtWidgets.QLabel(parent=dlgBuscar)
        self.lblBuscarInfo.setGeometry(QtCore.QRect(30, 10, 201, 16))
        self.lblBuscarInfo.setObjectName("lblBuscarInfo")

        self.retranslateUi(dlgBuscar)
        QtCore.QMetaObject.connectSlotsByName(dlgBuscar)

    def retranslateUi(self, dlgBuscar):
        _translate = QtCore.QCoreApplication.translate
        dlgBuscar.setWindowTitle(_translate("dlgBuscar", "Buscar"))
        self.botonBuscarDlg.setText(_translate("dlgBuscar", "Buscar"))
        self.lblBuscarInfo.setText(_translate("dlgBuscar", "Escribe el DNI del conductor:"))