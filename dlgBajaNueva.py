# Form implementation generated from reading ui file '.\Templates\dlgBajaNueva.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgBajaNueva(object):
    def setupUi(self, dlgBajaNueva):
        dlgBajaNueva.setObjectName("dlgBajaNueva")
        dlgBajaNueva.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        dlgBajaNueva.resize(400, 86)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Templates\\../img/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgBajaNueva.setWindowIcon(icon)
        self.lblBajaNueva = QtWidgets.QLabel(parent=dlgBajaNueva)
        self.lblBajaNueva.setGeometry(QtCore.QRect(70, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblBajaNueva.setFont(font)
        self.lblBajaNueva.setStyleSheet("")
        self.lblBajaNueva.setObjectName("lblBajaNueva")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=dlgBajaNueva)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 40, 221, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBajaNueva = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btnBajaNueva.setMinimumSize(QtCore.QSize(100, 0))
        self.btnBajaNueva.setObjectName("btnBajaNueva")
        self.horizontalLayout.addWidget(self.btnBajaNueva)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnBajaCerrar = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btnBajaCerrar.setObjectName("btnBajaCerrar")
        self.horizontalLayout.addWidget(self.btnBajaCerrar)

        self.retranslateUi(dlgBajaNueva)
        QtCore.QMetaObject.connectSlotsByName(dlgBajaNueva)

    def retranslateUi(self, dlgBajaNueva):
        _translate = QtCore.QCoreApplication.translate
        dlgBajaNueva.setWindowTitle(_translate("dlgBajaNueva", "Cambiar fecha baja"))
        self.lblBajaNueva.setText(_translate("dlgBajaNueva", "¿Quieres cambiar la fecha de baja?"))
        self.btnBajaNueva.setText(_translate("dlgBajaNueva", "Cambiar fecha"))
        self.btnBajaCerrar.setText(_translate("dlgBajaNueva", "Cerrar"))