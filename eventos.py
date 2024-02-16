from PyQt6.QtGui import QPixmap
from datetime import datetime
from PyQt6 import QtWidgets, QtCore, QtSql, QtGui
import sys, var, locale, re, zipfile, shutil, xlwt, xlrd

import conductores, clientes
import ddbb

locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Eventos():
    def salir(self):
        """
            Evento que cierra la aplicación
        """
        try:
            sys.exit(0)
        except Exception as error:
            print(error," en modulo eventos")

    def cerrarAcercaDe(self):
        """
            Evento que cierra la ventana acerca de
        """
        try:
            var.acercaDe.hide()
        except Exception as error:
            print(error," en modulo eventos")

    def abrirCalendar(self):
        """
            Evento que abre una pestaña con calendario
        """
        try:
            var.calendar.show()
        except Exception as error:
            print(error," en modulo eventos")

    def abrirCalendarBaja(self):
        """
            Evento que abre una pestaña de calendario
        """
        try:
            if var.ui.lblCodigoBD.text() != "":
                var.calendarBaja.show()
            else:
                Eventos.mostrarMensaje("Elige un conductor")
        except Exception as error:
            print(error," en modulo eventos")

    def abrirCalendarAltaFactura(self):
        """
            Evento que abre una pestaña de calendario
        """
        try:
            var.calendarAltaFacturas.show()
        except Exception as error:
            print(error," en modulo eventos")

    def abrirAcercaDe(self):
        """
            Evento que abre la pestaña acerca de
        """
        try:
            var.acercaDe.show()
        except Exception as error:
            print(error," en modulo eventos")

    def abrirBajaNueva(self):
        """
        Abre la ventana para dar de baja a un conductor existente o programar una nueva baja.

        Args:
            self: Referencia a la instancia de la clase.

        Returns:
            None
        """
        try:
            if var.ui.lblCodigoBD.text():
                conductor = ddbb.DDBB.oneConductor(str(var.ui.lblCodigoBD.text()))
                if conductor[11] != "":
                    var.bajaNueva.show()
                else:
                    Eventos.abrirCalendarBaja(self)
        except Exception as error:
            print(error," en modulo eventos")

    def abrirCalendarBajaCliente(self):
        """
        Abre la ventana para programar la baja de un cliente seleccionado.

        Args:
            self: Referencia a la instancia de la clase.

        Returns:
            None
        """
        try:
            if var.ui.lblCodigoCliente.text() != "":
                var.bajaCliente.show()
            else:
                Eventos.mostrarMensaje("Elige un cliente")
        except Exception as error:
            print(error," en modulo eventos")

    def abrirBajaCliente(self):
        """
        Abre la ventana para dar de baja a un cliente existente o programar una nueva baja.

        Args:
            self: Referencia a la instancia de la clase.

        Returns:
            None
        """
        try:
            if var.ui.lblCodigoCliente.text():
                cliente = ddbb.DDBB.oneCliente(str(var.ui.lblCodigoCliente.text()))
                if cliente[7] != "":
                    var.bajaNuevaCliente.show()
                else:
                    Eventos.abrirCalendarBajaCliente(self)
        except Exception as error:
            print(error," en modulo eventos")

    def abrirSalir(self=None):
        """
        Muestra un mensaje de confirmación para salir de la aplicación.

        Args:
            self: Referencia a la instancia de la clase (puede ser None si no se usa).

        Returns:
            None
        """
        mbox = QtWidgets.QMessageBox()
        mbox.setWindowTitle('Salida')
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
        mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
        mbox.setText('¿Seguro que deseas salir?')
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            mbox.hide()

    def cerrarBuscar(self):
        """
            Evento que esconde la pestaña de buscar
        """
        try:
            var.buscar.hide()
        except Exception as error:
            print(error," en modulo eventos")

    def cerrarAltaNueva(self):
        """
            Esconde la ventana alta nueva
        """
        try:
            var.altaNueva.hide()
        except Exception as error:
            print(error)

    def cerrarBajaNueva(self):
        """
            Esconde la ventana para una baja
        """
        try:
            var.bajaNueva.hide()
        except Exception as error:
            print(error)

    def cerrarBajaNuevaCliente(self):
        """
            Esconde la ventana baja nueva cliente
        """
        try:
            var.bajaNuevaCliente.hide()
        except Exception as error:
            print(error)

    def cerrarSalir(self):
        """
            Esconde la ventana de salir
        """
        try:
            var.salir.hide()
        except Exception as error:
            print(error," en modulo eventos")

    def abrirBuscar(self):
        """
            Abre la pestaña para buscar
        """
        try:
            var.buscar.show()
        except Exception as error:
            print(error, " en abrir buscar")

    def validarDNI(self=None):
        """
            valida el DNI y cambia la imagen de una a otra dependiendo de si es o no correcto
        """
        try:
            imgCorrecto = QPixmap('./img/correcto.ico')
            imgIncorrecto = QPixmap('./img/incorrecto.ico')

            dni = var.ui.textoDNI.text()
            dni = dni.upper()
            var.ui.textoDNI.setText(dni)
            if conductores.Conductores.validarDNI(dni):
                var.ui.lblValidarDNI.setPixmap(imgCorrecto)
                var.ui.textoFechaAlta.setFocus()
            else:
                var.ui.lblValidarDNI.setPixmap(imgIncorrecto)
                var.ui.textoDNI.setText(None)
        except Exception as error:
            print(error)

    def importarCondutoresExcel(self):
        """
        Importa conductores desde un archivo Excel seleccionado.

    Args:
        self: Referencia a la instancia de la clase.

    Returns:
        None
        """
        try:
            filename = var.dlgAbrir.getOpenFileName(None, "Importar conductores", "", "*.xls;;All File(*)")
            if filename[0]:
                file = filename[0]
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols
                numFallo = 0
                for i in range(filas):
                    if i == 0:
                        pass
                    else:
                        new = []
                        for j in range(columnas):
                            if j != 0:
                                new.append(str(datos.cell_value(i, j)))
                        if conductores.Conductores.validarDNI(str(new[0])):
                            ddbb.DDBB.guardarConductor(new, 1)
                        else:
                            numFallo += 1
                        if i == filas -1:
                            Eventos.mostrarMensaje("Todos los conductores han sido importados, han fallado "+str(numFallo)+" datos")
                ddbb.DDBB.mostrarConductores()
        except Exception as error:
            print(error)

    def importarClientesExcel(self):
        """
        Importa clientes desde un archivo Excel seleccionado.

        Args:
            self: Referencia a la instancia de la clase.

        Returns:
            None
        """
        try:
            filename = var.dlgAbrir.getOpenFileName(None, "Importar clientes", "", "*.xls;;All File(*)")
            if filename[0]:
                file = filename[0]
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols
                numFallo = 0
                for i in range(filas):
                    if i == 0:
                        pass
                    else:
                        new = []
                        for j in range(columnas):
                            if j == 3:
                                new.append(int(datos.cell_value(i, j)))
                            else:
                                new.append(str(datos.cell_value(i, j)))
                        if conductores.Conductores.validarDNI(str(new[0])):
                            ddbb.DDBB.guardarCliente(new, 1)
                        else:
                            numFallo += 1
                        if i == filas -1:
                            Eventos.mostrarMensaje("Todos los clientes han sido importados, han fallado "+str(numFallo)+" datos")
                ddbb.DDBB.mostrarClientes()
        except Exception as error:
            print(error)

    def limpiarPanel(self=None):
        """
            Limpia los campos del panel de información del conductor.

            Args:
                self: Referencia a la instancia de la clase (puede ser None si no se usa).

            Returns:
                None
        """
        imgIncorrecto = QPixmap('./img/incorrecto.ico')
        try:
            listaWidgets = [var.ui.textoDNI, var.ui.textoFechaAlta, var.ui.textoApellidos, var.ui.textoNombre,
                            var.ui.textoDireccion, var.ui.textoTelefono, var.ui.textoSalario, var.ui.lblCodigoBD]
            for i in listaWidgets:
                i.setText(None)
            var.ui.lblValidarDNI.setPixmap(imgIncorrecto)

            checkLicencia = [var.ui.checkA, var.ui.checkB, var.ui.checkC, var.ui.checkD]
            for i in checkLicencia:
                i.setChecked(False)

            var.ui.comboProvincia.setCurrentText('')
            var.ui.comboLocalidad.setCurrentText('')

        except Exception as error:
            print(error," en modulo eventos")

    def limpiarPanelClientes(self=None):
        """
        Limpia los campos del panel de información del cliente.

        Args:
            self: Referencia a la instancia de la clase (puede ser None si no se usa).

        Returns:
            None
        """
        imgIncorrecto = QPixmap('./img/incorrecto.ico')
        try:
            listaWidgets = [var.ui.textoDNICliente, var.ui.textoRazonSocialCliente, var.ui.textoTelefonoCliente,
                            var.ui.textoDireccionCliente, var.ui.lblCodigoCliente]
            for i in listaWidgets:
                i.setText(None)
            var.ui.lblValidarCliente.setPixmap(imgIncorrecto)

            var.ui.comboProvinciaCliente.setCurrentText('')
            var.ui.comboLocalidadCliente.setCurrentText('')

        except Exception as error:
            print(error," en modulo eventos")


    def limpiarPanelFacturas(self=None):
        """
        Limpia los campos del panel de facturas del cliente.

        Args:
            self: Referencia a la instancia de la clase (puede ser None si no se usa).

        Returns:
            None
        """
        imgIncorrecto = QPixmap('./img/incorrecto.ico')
        try:
            listaWidgets = [var.ui.lblFactutaciontxt, var.ui.txtAltaFacturacion, var.ui.txtCIFcliente, var.ui.txtKm ]
            for i in listaWidgets:
                i.setText(None)
            var.ui.lblValidarCliente.setPixmap(imgIncorrecto)
            var.ui.cmbConductor.setCurrentText('')
            var.ui.cmbProvinciasVentas.setCurrentText('')
            var.ui.cmbMunicipiosVentas.setCurrentText('')
            var.ui.cmbProvinciasVentas_2.setCurrentText('')
            var.ui.cmbMunicipiosVentas_2.setCurrentText('')
        except Exception as error:
            print(error," en modulo eventos")

    @staticmethod
    def importarCopia():
        """
            Importa una copia de seguridad de la base de datos.

            Returns:
                None
        """
        try:
            filename = var.dlgAbrir.getOpenFileName(None, "Restaurar Copia de Seguridad", "", "*.zip;;All Files(*)")
            if filename[0]:
                with zipfile.ZipFile(str(filename[0]), "r") as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
                Eventos.mostrarMensaje("Copia restaurada")
                ddbb.DDBB.mostrarConductores()
                ddbb.DDBB.mostrarFacturas()
                ddbb.DDBB.mostrarClientes()
                ddbb.DDBB.cargarConductores()
            else:
                Eventos.mostrarMensaje("Elige un archivo")
        except Exception as error:
            Eventos.mostrarMensaje(error)

    def exportarExcel(self):
        """
        Exporta los datos de conductores a un archivo Excel.

        Args:
            self: Referencia a la instancia de la clase.

        Returns:
            None
        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%S")
            file = (str(fecha)+"_datos.xls")
            directorio, filename = var.dlgAbrir.getSaveFileName(None, "Exportar datos", file, ".xls")
            if var.dlgAbrir.accept and filename:
                wb = xlwt.Workbook()
                sheet1 = wb.add_sheet("Conductores")
                sheet1.write(0, 0, "ID")
                sheet1.write(0, 1, "DNI")
                sheet1.write(0, 2, "Fecha alta")
                sheet1.write(0, 3, "Apellidos")
                sheet1.write(0, 4, "Nombre")
                sheet1.write(0, 5, "Direccion")
                sheet1.write(0, 6, "Provincia")
                sheet1.write(0, 7, "Municipio")
                sheet1.write(0, 8, "Movil")
                sheet1.write(0, 9, "Salario")
                sheet1.write(0, 10, "Carnets")
                sheet1.write(0, 11, "Fecha baja")
                registros = ddbb.DDBB.selectDriversAll()

                for fila, registro in enumerate(registros, 1):
                    for i, valor in enumerate(registro):
                        sheet1.write(fila, i, str(valor))
                    fila += 1

                wb.save(directorio)
                Eventos.mostrarMensaje("Guardado")

        except Exception as error:
            print(error)
            Eventos.mostrarMensaje("Error en la exportacion")

    @staticmethod
    def crearCopia():
        """
        Crea una copia de seguridad de la base de datos.

        Returns:
            None
        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%S")
            copia = str(fecha)+"_backup.zip"
            directorio, filename = var.dlgAbrir.getSaveFileName(None, "Guardar Copia Seguridad", copia, ".zip")
            print(directorio)
            if var.dlgAbrir.accept and filename != "":
                fileZip = zipfile.ZipFile(copia, "w")
                fileZip.write(var.base), zipfile.ZIP_DEFLATED
                fileZip.close()
                shutil.move(str(copia),str(directorio))
                Eventos.mostrarMensaje("Copia de seguridad creada")

        except Exception as error:
            Eventos.mostrarMensaje(error)

    def resizeTablaConductores(self):
        """
             Ajusta el tamaño de las columnas de la tabla de conductores.

            Args:
                self: Referencia a la instancia de la clase.

            Returns:
                None
        """
        try:
            header = var.ui.tablaConductores.horizontalHeader()
            for i in range(5):
                if i == 0 or i == 3 or i == 4:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("error en resize tabla conductores", error)

    def resizeTablaClientes(self):
        """
        Ajusta el tamaño de las columnas de la tabla de clientes.

        Args:
            self: Referencia a la instancia de la clase.

        Returns:
            None
        """
        try:
            header = var.ui.tablaClientes.horizontalHeader()
            for i in range(5):
                if i == 0 or i == 3 or i == 4:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("error en resize tabla conductores", error)

    def resizeTablaFacturas(self):
        """
        Ajusta el tamaño de las columnas de la tabla de facturas.

        Args:
            self: Referencia a la instancia de la clase.

        Returns:
            None
        """
        try:
            header = var.ui.tablaFacturas.horizontalHeader()
            for i in range(5):
                if i == 0:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("error en resize tabla conductores", error)

    def resizeTabViajes(self):
        """
            Ajusta el tamaño de las columnas de la tabla de viajes.

            Args:
                self: Referencia a la instancia de la clase.

            Returns:
                None
        """
        try:
            header = var.ui.tabViajes.horizontalHeader()
            for i in range(5):
                if i==0 or i==3 or i==6:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i==1 or i==2 :
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print(error," en resize tabViajes")

    @staticmethod
    def formatCajaTexto():
        """
        Formatea el texto en los campos de apellidos y nombre para que la primera letra de cada palabra esté en mayúscula.

        Returns:
            None
        """
        try:
            var.ui.textoApellidos.setText(var.ui.textoApellidos.text().title())
            var.ui.textoNombre.setText(var.ui.textoNombre.text().title())
        except Exception as error:
            print("erros en letra capital", error)

    @staticmethod
    def formatSalario():
        """
            Formatea el salario.

            Returns:
                None
        """
        try:
            if len(var.ui.textoSalario.text()) != 0:
                var.ui.textoSalario.setText(str(locale.currency(float(var.ui.textoSalario.text().replace(",", ".")), grouping=True)))
        except Exception as error:
            Eventos.mostrarMensaje('Valor de Salario Incorrecto (00000000.00)')
            var.ui.textoSalario.setText("")

    @staticmethod
    def formatTelefono():
        """
            Le da formato al telefono y solo deja que tenga 9 numeros

            Returns:
                None
        """
        try:
            numero = var.ui.textoTelefono.text()
            numeros_validos = "+1234567890"
            esNumero = (len(numero) == len([n for n in numero if n in numeros_validos]))

            if len(numero) == 9 and esNumero:
                numero_con_espacios = numero[:3] + ' ' + numero[3:5] + ' ' + numero[5:]
                var.ui.textoTelefono.setText(numero_con_espacios)
            elif len(numero) == 12 and esNumero:
                numero_con_espacios = numero[:3] + ' ' + numero[3:6] + ' ' + numero[6:8] + ' ' + numero[8:]
                var.ui.textoTelefono.setText(numero_con_espacios)
            elif len(numero) == 0:
                pass
            else:
                raise Exception
        except Exception as error:
            Eventos.mostrarMensaje('Formato de teléfono incorrecto (123 45 67)')
            var.ui.textoTelefono.setText("")

    def mostrarMensaje(mensaje):
        """
        Muestra un mensaje de información en un cuadro de diálogo.

        Args:
            mensaje (str): El mensaje que se desea mostrar.

        Returns:
            None
        """
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Aviso')
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(mensaje)
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
        msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    @staticmethod
    def acercade():
        """

        """
        try:
            pass
        except Exception as error:
            print(error," en abrir acercade")


