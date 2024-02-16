from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets, QtSql, QtCore, QtGui

import ddbb, eventos
import main, conductores
import var
class Clientes():

    def cargarCliente(registro):
        try:
            eventos.Eventos.limpiarPanelClientes(main.Main)

            datos = [var.ui.lblCodigoCliente, var.ui.textoDNICliente, var.ui.textoRazonSocialCliente, var.ui.textoDireccionCliente, var.ui.textoTelefonoCliente, var.ui.comboProvinciaCliente,
                     var.ui.comboLocalidadCliente]
            for i, dato in enumerate(datos):
                if i == 5 or i == 6:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))

            Clientes.validarDNI(var.ui.textoDNICliente.text().upper())
        except Exception as error:
            print("error en cargar conductor", error)

    def cargarDesdeTabla(self):
        try:
            row = var.ui.tablaClientes.selectedItems()
            fila = [dato.text() for dato in row]
            registro = ddbb.DDBB.oneCliente(fila[0])
            Clientes.cargarCliente(registro)
            ddbb.DDBB.mostrarClientes()
            Clientes.colorearFila(registro[0])
        except Exception as error:
            print("error en cargarDesdeTabla", error)

    @staticmethod
    def getActualizacionCliente():
        try:
            cliente = [var.ui.lblCodigoCliente, var.ui.textoDNICliente, var.ui.textoRazonSocialCliente, var.ui.textoDireccionCliente, var.ui.textoTelefonoCliente]
            modiCliente = []
            for i in cliente:
                modiCliente.append(i.text().title())

            modiCliente.append(var.ui.comboProvinciaCliente.currentText())
            modiCliente.append(var.ui.comboLocalidadCliente.currentText())

            if not var.ui.lblCodigoCliente.text():
                eventos.Eventos.mostrarMensaje("Elige un cliente")
                return None
            elif not all([var.ui.textoDNICliente.text(), var.ui.textoTelefonoCliente.text()]):
                eventos.Eventos.mostrarMensaje("Completa todos los datos")
                return None
            else:
                return modiCliente

        except Exception as error:
            print("error en modificar conductor: ", error)

    def colorearFila(codigo):
        for fila in range(var.ui.tablaClientes.rowCount()):
            if var.ui.tablaClientes.item(fila, 0).text() == str(codigo):
                for columna in range(var.ui.tablaClientes.columnCount()):
                    item = var.ui.tablaClientes.item(fila, columna)
                    if item is not None:
                        item.setBackground(QtGui.QColor(255, 241, 150))

    def cargarTablaClientes(registros):
        try:
            var.ui.tablaClientes.clearContents()
            var.ui.tablaClientes.setRowCount(0)

            index = 0
            for registro in registros:
                var.ui.tablaClientes.setRowCount(index + 1)
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tablaClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tablaClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tablaClientes.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))

                var.ui.tablaClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print("error en cargarTablaclientes", error)
    def altaCliente(self):
        try:
            cliente = [var.ui.textoDNICliente, var.ui.textoRazonSocialCliente, var.ui.textoDireccionCliente,
                       var.ui.textoTelefonoCliente]
            nuevoCliente = []
            for i in cliente:
                nuevoCliente.append(i.text().title())

            nuevoCliente.append(var.ui.comboProvinciaCliente.currentText())
            nuevoCliente.append(var.ui.comboLocalidadCliente.currentText())

            if not all([var.ui.textoDNICliente.text(), var.ui.textoTelefonoCliente.text()]):
                eventos.Eventos.mostrarMensaje("Completa todos los datos")
            else:
                ddbb.DDBB.guardarCliente(nuevoCliente, 0)

        except Exception as error:
            eventos.Eventos.mostrarMensaje("El conductor ya esta dado de alta")

    def validarDNI(self=None):
        try:
            imgCorrecto = QPixmap('./img/correcto.ico')
            imgIncorrecto = QPixmap('./img/incorrecto.ico')

            dni = var.ui.textoDNICliente.text()
            dni = dni.upper()
            var.ui.textoDNICliente.setText(dni)
            if conductores.Conductores.validarDNI(dni):
                var.ui.lblValidarCliente.setPixmap(imgCorrecto)
                var.ui.textoDireccionCliente.setFocus()
            else:
                var.ui.lblValidarCliente.setPixmap(imgIncorrecto)
                var.ui.textoDNI.setText(None)
        except Exception as error:
            print(error)

    def borrarCliente(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.bajaCliente.hide()

            dni = var.ui.textoDNICliente.text()
            ddbb.DDBB.borrarCliente(dni, str(data))
            ddbb.DDBB.mostrarClientes()
        except Exception as error:
            eventos.Eventos.mostrarMensaje("No se puede dar de baja a el cliente")

    @staticmethod
    def formatTelefonoClientes():
        try:
            numero = var.ui.textoTelefonoCliente.text()
            numeros_validos = "+1234567890"
            esNumero = (len(numero) == len([n for n in numero if n in numeros_validos]))

            if len(numero) == 9 and esNumero:
                numero_con_espacios = numero[:3] + ' ' + numero[3:5] + ' ' + numero[5:]
                var.ui.textoTelefonoCliente.setText(numero_con_espacios)
            elif len(numero) == 12 and esNumero:
                numero_con_espacios = numero[:3] + ' ' + numero[3:6] + ' ' + numero[6:8] + ' ' + numero[8:]
                var.ui.textoTelefonoCliente.setText(numero_con_espacios)
            elif len(numero) == 0:
                pass
            else:
                raise Exception
        except Exception as error:
            eventos.Eventos.mostrarMensaje('Formato de teléfono incorrecto (123 45 67)')
            var.ui.textoTelefonoCliente.setText("")