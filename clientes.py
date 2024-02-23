from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets, QtSql, QtCore, QtGui

import ddbb, eventos
import main, conductores
import var
class Clientes():

    def cargarCliente(registro):
        """
            Carga los datos de un cliente en los campos correspondientes de la interfaz gráfica.
            Recibe como parámetro un registro que contiene los datos del cliente, y luego actualiza los campos de la interfaz con esta información.
            :param registro: Registro que contiene los datos del cliente a cargar en la interfaz.
            :type registro: tuple
            :return: None
            :rtype: None
        """
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
        """
        Carga los datos del cliente seleccionado en la tabla de clientes en los campos correspondientes de la interfaz gráfica.

        Obtiene la fila seleccionada en la tabla de clientes, luego recupera los datos del cliente asociados a esa fila y finalmente carga estos datos en los campos de la interfaz.

        :return: None
        :rtype: None
        """
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
        """
        Obtiene los datos actualizados del cliente desde los campos de la interfaz gráfica.

        Lee los datos ingresados o seleccionados en los campos correspondientes de la interfaz gráfica para el cliente y los retorna en una lista. Los datos se convierten en mayúsculas y el título se aplica a cada palabra en los campos de texto.

        :return: Lista de datos actualizados del cliente
        :rtype: list[str] or None
        """
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
        """
        Colorea la fila de la tabla de clientes correspondiente al código dado.

        Recorre todas las filas de la tabla de clientes y compara el valor en la columna del código con el código proporcionado. Si encuentra una coincidencia, colorea toda la fila de esa celda en la tabla de clientes con un color amarillo claro.

        :param codigo: El código del cliente a colorear la fila.
        :type codigo: str
        """
        for fila in range(var.ui.tablaClientes.rowCount()):
            if var.ui.tablaClientes.item(fila, 0).text() == str(codigo):
                for columna in range(var.ui.tablaClientes.columnCount()):
                    item = var.ui.tablaClientes.item(fila, columna)
                    if item is not None:
                        item.setBackground(QtGui.QColor(255, 241, 150))

    def cargarTablaClientes(registros):
        """
        Carga los datos de los clientes en la tabla de clientes.

        Recorre la lista de registros proporcionada y agrega cada registro a la tabla de clientes. Los registros deben contener información sobre el código, DNI, razón social, dirección, teléfono y localidad del cliente.

        :param registros: Lista de registros de clientes a cargar en la tabla.
        :type registros: list
        """
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
        """
        Realiza el alta de un nuevo cliente en la base de datos.

        Recoge los datos del cliente ingresados en la interfaz de usuario y los guarda en la base de datos. Se verifica que se hayan completado el DNI y el teléfono del cliente antes de realizar el alta.

        :return: None
        :rtype: None
        """
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
        """
        Valida el formato del DNI del cliente.

        Lee el DNI ingresado en la interfaz de usuario, lo convierte a mayúsculas y verifica su validez utilizando el método `validarDNI` del módulo `Conductores`. Si el DNI es válido, se muestra un icono de "correcto"; de lo contrario, se muestra un icono de "incorrecto" y se borra el campo DNI.

        :return: None
        :rtype: None
        """
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
        """
            Elimina un cliente de la base de datos según la fecha especificada.

            Obtiene la fecha de la interfaz de calendario (`qDate`) y la convierte al formato 'dd/mm/yyyy'. Luego oculta la ventana de confirmación de eliminación (`var.bajaCliente`).
            Se recupera el DNI del cliente de la interfaz de usuario y se llama al método `borrarCliente` del módulo `DDBB` para eliminar el cliente de la base de datos con la fecha proporcionada. Finalmente, se actualiza la tabla de clientes en la interfaz.

            :param qDate: Fecha de la baja del cliente.
            :type qDate: QDate
            :return: None
            :rtype: None
        """
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
        """
        Formatea el número de teléfono del cliente en el formato '123 45 67' o '123 456 789'.

        Extrae el número de teléfono de la interfaz de usuario (`var.ui.textoTelefonoCliente.text()`) y valida que solo contenga caracteres numéricos y los caracteres especiales '+', '(', ')', '-', y ' ' (espacio).
        Luego, verifica la longitud del número de teléfono y, si es válido, lo formatea agregando espacios en posiciones específicas.
        Si la longitud del número no es válida o no cumple con el formato esperado, se muestra un mensaje de error y se borra el contenido del campo de texto.

        :return: None
        :rtype: None
        """
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