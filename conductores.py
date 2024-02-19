from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets, QtCore, QtGui

import ddbb, eventos
import main
import var

class Conductores():

    def cargarFecha(qDate):
        """

        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.textoFechaAlta.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print(f"Error en conductores: {str(error)}")

    def cargarDesdeTabla(self):
        """

        """
        try:
            row = var.ui.tablaConductores.selectedItems()
            fila = [dato.text() for dato in row]
            registro = ddbb.DDBB.oneConductor(fila[0])
            Conductores.cargarConductor(registro)
            ddbb.DDBB.mostrarConductores()
            Conductores.colorearFila(registro[0])
        except Exception as error:
            print("error en cargarDesdeTabla", error)

    def cargarConductor(registro):
        """

        """
        try:
            eventos.Eventos.limpiarPanel(main.Main)

            datos = [var.ui.lblCodigoBD, var.ui.textoDNI, var.ui.textoFechaAlta, var.ui.textoApellidos, var.ui.textoNombre, var.ui.textoDireccion,
                     var.ui.comboProvincia, var.ui.comboLocalidad, var.ui.textoTelefono, var.ui.textoSalario]

            for i, dato in enumerate(datos):
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))

            if "A" in registro[10]:
                var.ui.checkA.setChecked(True)
            if "B" in registro[10]:
                var.ui.checkB.setChecked(True)
            if "C" in registro[10]:
                var.ui.checkC.setChecked(True)
            if "D" in registro[10]:
                var.ui.checkD.setChecked(True)
            Conductores.validarDNI(var.ui.textoDNI.text().upper())
        except Exception as error:
            print("error en cargar conductor", error)

    def altaConductor(self):
        """

        """
        try:
            if var.ui.lblCodigoBD.text() == "":
                driver = [var.ui.textoDNI, var.ui.textoFechaAlta, var.ui.textoApellidos, var.ui.textoNombre, var.ui.textoDireccion, var.ui.textoTelefono, var.ui.textoSalario]
                newDriver = []
                for i in driver:
                    newDriver.append(i.text().title())

                newDriver.insert(5, var.ui.comboProvincia.currentText())
                newDriver.insert(6, var.ui.comboLocalidad.currentText())

                licencias = []
                if var.ui.checkA.isChecked():
                    licencias.append('A')
                if var.ui.checkB.isChecked():
                    licencias.append('B')
                if var.ui.checkC.isChecked():
                    licencias.append('C')
                if var.ui.checkD.isChecked():
                    licencias.append('D')
                newDriver.append('-'.join(licencias))

                if not all([var.ui.textoDNI.text(), var.ui.textoFechaAlta.text(), var.ui.textoApellidos.text(), var.ui.textoTelefono.text(), var.ui.textoNombre.text()]):
                    eventos.Eventos.mostrarMensaje("Completa todos los datos")
                else:
                    ddbb.DDBB.guardarConductor(newDriver, 0)
            else:
                var.altaNueva.show()
        except Exception as error:
            print("error en alta conductor: ",error)

    @staticmethod
    def getActualizacionDriver():
        """

        :return:
        :rtype:
        """
        try:
            driver = [var.ui.lblCodigoBD,var.ui.textoDNI, var.ui.textoFechaAlta, var.ui.textoApellidos, var.ui.textoNombre, var.ui.textoDireccion, var.ui.textoTelefono, var.ui.textoSalario]
            modiDriver = []
            for i in driver:
                modiDriver.append(i.text().title())

            modiDriver.insert(6, var.ui.comboProvincia.currentText())
            modiDriver.insert(7, var.ui.comboLocalidad.currentText())

            licencias = []
            if var.ui.checkA.isChecked():
                licencias.append('A')
            if var.ui.checkB.isChecked():
                licencias.append('B')
            if var.ui.checkC.isChecked():
                licencias.append('C')
            if var.ui.checkD.isChecked():
                licencias.append('D')
            modiDriver.append('-'.join(licencias))

            if not var.ui.lblCodigoBD.text():
                eventos.Eventos.mostrarMensaje("Elige un usuario")
                return None
            elif not all([var.ui.textoDNI.text(), var.ui.textoFechaAlta.text(), var.ui.textoApellidos.text(), var.ui.textoTelefono.text(), var.ui.textoNombre.text()]):
                eventos.Eventos.mostrarMensaje("Completa todos los datos")
                return None
            else:
                return modiDriver

        except Exception as error:
            print("error en modificar conductor: ",error)

    def validarDNI(dni):
        """

        :return:
        :rtype:
        """
        try:
            tabla = "TRWAGMYFPDXBNJZSKVHLCKE"
            digExt = "XYZ"
            reempDigExt = {"X": '0', "Y": '1', "Z": '2'}
            numeros = "1234567890"

            if len(dni) == 9:
                digControl = dni[8]
                dni = dni[:8]
                if dni[0] in digExt:
                    dni = dni.replace(dni[0], reempDigExt[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == digControl:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as error:
            print(error, " en validar conductores")
            return False

    def colorearFila(codigo):
        """

        """
        for fila in range(var.ui.tablaConductores.rowCount()):
            if var.ui.tablaConductores.item(fila, 0).text() == str(codigo):
                for columna in range(var.ui.tablaConductores.columnCount()):
                    item = var.ui.tablaConductores.item(fila, columna)
                    if item is not None:
                        item.setBackground(QtGui.QColor(255, 241, 150))

    def cargarTablaConductores(registros):
        """

        """
        try:
            var.ui.tablaConductores.clearContents()
            var.ui.tablaConductores.setRowCount(0)

            index = 0
            for registro in registros:
                var.ui.tablaConductores.setRowCount(index + 1)
                var.ui.tablaConductores.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaConductores.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tablaConductores.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tablaConductores.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tablaConductores.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tablaConductores.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))

                var.ui.tablaConductores.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaConductores.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaConductores.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print("error en cargarTabalaConductores", error)

    def borrarConductor(qDate):
        """

        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.calendarBaja.hide()

            dni = var.ui.textoDNI.text()
            ddbb.DDBB.borrarConductor(dni, str(data))
            ddbb.DDBB.mostrarConductores()
            ddbb.DDBB.cargarConductores()

        except Exception as error:
            eventos.Eventos.mostrarMensaje("No se puede dar de baja a el conductor")
