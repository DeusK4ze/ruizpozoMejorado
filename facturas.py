import ddbb
import var
import time
from PyQt6 import QtWidgets,QtCore, QtGui,  QtSql
from reportlab.pdfgen import canvas
import os, var, shutil
from PIL import Image
from datetime import datetime

class Facturas():

    def cargarFecha(qDate):
        """
        Carga la fecha seleccionada en un objeto QDate a un campo de texto y oculta el calendario.
        Args:
            qDate (QDate): Objeto QDate que representa la fecha seleccionada.
        Returns:
            None
        """
        try:
            print("Entro aqui")
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtAltaFacturacion.setText(str(data))
            var.calendarAltaFacturas.hide()
        except Exception as error:
            print(f"Error en facturas: {str(error)}")

    def validarDNI(self=None):
        """
        Valida y formatea el DNI introducido en el campo de texto txtCIFcliente.
        Args:
            self: Referencia a la instancia de la clase (puede ser None si no se usa).
        Returns:
            None
        """
        try:
            dni = var.ui.txtCIFcliente.text()
            dni = dni.upper()
            var.ui.txtCIFcliente.setText(dni)
            if not conductores.Conductores.validarDNI(dni):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Dni Incorrecto')
                msg.exec()
                var.ui.textoDNI.setText(None)
            else:
                var.ui.txtAltaFacturacion.setFocus()
        except Exception as error:
            print(error)

    def altaFactura(self):
        """
        Realiza el registro de una nueva factura en la base de datos con la información proporcionada en la interfaz.
        Args:
            self: Referencia a la instancia de la clase.
        Returns:
            None
        """
        try:
            registro = [var.ui.txtCIFcliente.text(), var.ui.txtAltaFacturacion.text(), var.ui.cmbConductor.currentText().split('.')[0]]
            ddbb.DDBB.altafacturacion(registro)
        except Exception as error:
            print('error alta en factura' + error)

    def cargarTablaFacturas(registros):
        """
        Carga los datos de las facturas en la tabla de facturas de la interfaz gráfica.

        :param registros: Lista de registros de facturas para mostrar en la tabla.
        :type registros: list
        :return: None
        :rtype: None
        """
        try:
            var.ui.tablaFacturas.clearContents()
            index = 0
            for registro in registros:
                var.ui.tablaFacturas.setRowCount(index + 1)
                var.ui.tablaFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tablaFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1
        except Exception as error:
            print("error en cargarTablaFacturas", error)

    def cargarFacturas(registro):
        """
        Carga los datos de una factura en los elementos de la interfaz gráfica correspondientes.

        :param registro: Registro de factura a cargar en la interfaz gráfica.
        :type registro: list
        :return: None
        :rtype: None
        """
        try:
            registro2 = ddbb.DDBB.oneConductor(registro[3])
            driver = str(registro2[0]) + ". " + registro2[3]

            datos = [var.ui.lblFactutaciontxt, var.ui.txtCIFcliente, var.ui.txtAltaFacturacion, var.ui.cmbConductor]
            for i, dato in enumerate(datos):
                if i == 3:
                    dato.setCurrentText(str(driver))

                else:
                    dato.setText(str(registro[i]))
        except Exception as error:
            print("error en cargar facturas", error)

    def cargarDesdeTabla(self):
        """
        Carga los datos de una factura seleccionada en la tabla de facturas en la interfaz gráfica.

        :return: None
        :rtype: None
        """
        try:
            row = var.ui.tablaFacturas.selectedItems()
            fila = [dato.text() for dato in row]
            registro = ddbb.DDBB.oneFactura(fila[0])
            Facturas.cargarFacturas(registro)
            #ddbb.DDBB.mostrarFacturasDesdebtn()
            #Facturas.colorearFila(registro[0])
            Facturas.cargarTablaViajes(self)
        except Exception as error:
            print("error en cargarDesdeTabla", error)

    def colorearFila(codigo):
        """
        Colorea la fila correspondiente al código de factura dado en la tabla de facturas de la interfaz gráfica.

        :param codigo: El código de la factura a colorear la fila.
        :type codigo: str
        :return: None
        :rtype: None
        """
        for fila in range(var.ui.tablaFacturas.rowCount()):
            if var.ui.tablaFacturas.item(fila, 0).text() == str(codigo):
                for columna in range(var.ui.tablaFacturas.columnCount()):
                    item = var.ui.tablaFacturas.item(fila, columna)
                    if item is not None:
                        item.setBackground(QtGui.QColor(255, 241, 150))

    def cargarLineaVenta(self):
        """
        Carga una línea de venta utilizando los datos del viaje y la factura actualmente seleccionada en la interfaz gráfica.

        :return: None
        :rtype: None
        """
        try:
            viaje = ddbb.DDBB.datosViaje(self)
            factura = var.ui.lblFactutaciontxt.text()
            viaje.append(factura)
            if viaje[5] == str(0.8):
                km = 10
                viaje.append(str(km))
            else:
                km = var.ui.txtKm.text()
                viaje.append(str(km))
            ddbb.DDBB.cargarLineaViaje(viaje)
        except Exception as error:
            print("AAAAAAAAAAAA")

    def numMunicipio(nombre):
        """
        Consulta y devuelve el número de municipio asociado al nombre de un municipio.

        :param nombre: El nombre del municipio.
        :return: El número de municipio asociado al nombre especificado.
        :rtype: int or None
        """
        query = QtSql.QSqlQuery()
        query.prepare('select id_provincia from municipios where municipio == :municipio')
        query.bindValue(":municipio", nombre)
        if query.exec():
            while query.next():
                return query.value(0)

    def cargarViaje(self):
        """
        Carga los detalles de un viaje seleccionado en la interfaz gráfica.

        Selecciona las provincias y municipios correspondientes a los puntos de origen y destino del viaje, así como la distancia en kilómetros.

        :return: None
        :rtype: None
        """
        try:
            provincia = None
            provincia2 = None
            row = var.ui.tabViajes.selectedItems()
            fila = [dato.text() for dato in row]
            registro = ddbb.DDBB.oneviaje(fila[0])
            print(registro)
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias where id == :id_provincia')
            query.bindValue(":id_provincia", Facturas.numMunicipio(registro[2]))
            if query.exec():
                while query.next():
                    print(str(query.value(0)))
                    provincia = query.value(0)
            query2 = QtSql.QSqlQuery()
            query2.prepare('select provincia from provincias where id == :id_provincia')
            query2.bindValue(":id_provincia", Facturas.numMunicipio(registro[3]))
            if query2.exec():
                while query2.next():
                    print(str(query2.value(0)))
                    provincia2 = str(query2.value(0))
            var.ui.txtIDViaje.setText(registro[0])
            var.ui.cmbProvinciasVentas.setCurrentText(provincia)
            var.ui.cmbMunicipiosVentas.setCurrentText(registro[2])
            var.ui.cmbProvinciasVentas_2.setCurrentText(provincia2)
            var.ui.cmbMunicipiosVentas_2.setCurrentText(registro[3])
            var.ui.txtKm.setText(registro[5])
        except Exception as error:
            print(str(error) + " en cargarviaje")

    def cargarTablaViajes(self):
        """
        Carga la tabla de viajes asociados a una factura en la interfaz gráfica.

        Los detalles de los viajes se obtienen de la base de datos y se muestran en la tabla. Además, se calcula el subtotal, el IVA y el total de la factura.

        :return: None
        :rtype: None
        """
        try:
            var.ui.tabViajes.clearContents()
            datos = ddbb.DDBB.viajesFactura(var.ui.lblFactutaciontxt.text())
            index = 0
            subtotal = 0.0

            for registro in datos:
                var.ui.tabViajes.setRowCount(index + 1)  # crea una fila
                var.ui.tabViajes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabViajes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabViajes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabViajes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tabViajes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[5])))

                valor_pos4 = float(registro[4])
                valor_pos5 = float(registro[5])
                total = valor_pos4 * valor_pos5
                total_str = "{:.2f}".format(total)
                var.ui.tabViajes.setItem(index, 5, QtWidgets.QTableWidgetItem(total_str))

                var.ui.tabViajes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                btn_borrar = QtWidgets.QPushButton()
                btn_borrar.setFixedSize(30, 28)
                btn_borrar.setIcon(QtGui.QIcon('./img/basura.png'))
                var.ui.tabViajes.horizontalHeader().setSectionResizeMode(6,
                                                                         QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

                var.ui.tabViajes.setColumnWidth(6, 50)
                var.ui.tabViajes.setCellWidget(index, 6, btn_borrar)
                btn_borrar.clicked.connect(ddbb.DDBB.borrarviaje)
                # Sumar el subtotal
                subtotal += total
                index += 1
            iva_porc = 0.21
            iva = subtotal * iva_porc
            total_iva = subtotal + iva
            # Asignar el subtotal al QLabel después del bucle
            var.ui.lbl_subTotal.setText("{:.2f}".format(subtotal) + " \u20AC")
            var.ui.lbl_iva.setText("{:.2f}".format(iva) + " \u20AC")
            var.ui.lbl_total.setText("{:.2f}".format(total_iva) + " \u20AC")
        except Exception as error:
            print("error cargar TABLA VIAJES", error)

    def reportfactura(self=None):
        """
            Genera un informe en formato PDF de la factura seleccionada.

            Si no se ha seleccionado ninguna factura, muestra una advertencia.

            Si se selecciona una factura, se crea un archivo PDF con los detalles de la factura, incluidos los viajes asociados.

            :return: None
            :rtype: None
        """
        try:
            numFact = var.ui.lblFactutaciontxt.text()
            if numFact == "" or numFact.isspace():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Selecciona una factura.")
                mbox.exec()
            else:
                nombre = str(numFact) + '_factura.pdf'
                var.report = canvas.Canvas('informes/' + nombre)
                titulo = 'FACTURA'
                Facturas.topFactura(titulo)
                Facturas.footFactura(titulo)

                items = ["ID VIAJE", "ORIGEN", "DESTINO", "KM", "TARIFA", "TOTAL"]
                var.report.setFont('Helvetica-Bold', size=10)
                var.report.drawString(50, 650, str(items[0]))
                var.report.drawString(130, 650, str(items[1]))
                var.report.drawString(250, 650, str(items[2]))
                var.report.drawString(390, 650, str(items[3]))
                var.report.drawString(430, 650, str(items[4]))
                var.report.drawString(480, 650, str(items[5]))
                var.report.line(50, 645, 525, 645)
                # obtención datos en la base de datos
                query = QtSql.QSqlQuery()
                query.prepare("select idViaje, origen, destino, km, tarifa from viajes where factura = :factura")
                query.bindValue(":factura", int(numFact))
                var.report.setFont("Helvetica", size=9)
                if query.exec():
                    i = 55
                    j = 630
                    while query.next():
                        if j <= 130:
                            var.report.drawString(450, 140, "Página siguiente...")
                            var.report.showPage()  # crea una nueva página
                            Facturas.topFactura(titulo)
                            Facturas.footFactura(titulo)
                            var.report.setFont('Helvetica-Bold', size=10)
                            var.report.drawString(50, 650, str(items[0]))
                            var.report.drawString(130, 650, str(items[1]))
                            var.report.drawString(250, 650, str(items[2]))
                            var.report.drawString(390, 650, str(items[3]))
                            var.report.drawString(430, 650, str(items[4]))
                            var.report.drawString(480, 650, str(items[5]) + " €")
                            var.report.line(50, 645, 525, 645)
                            i = 55
                            j = 630
                        var.report.setFont("Helvetica", size=9)
                        var.report.drawCentredString(i + 15, j, str(query.value(0)))
                        var.report.drawString(i + 70, j, Facturas.ajustarTamanho(str(query.value(1)), 25))
                        var.report.drawString(i + 190, j, Facturas.ajustarTamanho(str(query.value(2)), 25))
                        var.report.drawString(i + 335, j, str(query.value(3)))
                        var.report.drawString(i + 385, j, str(query.value(4)))
                        totalViaje = float(query.value(3)) * float(query.value(4))
                        totalViaje = round(totalViaje, 2)
                        var.report.drawString(i + 430, j, str('{:.2f}'.format(totalViaje)) + " €")
                        j -= 25

                var.report.save()
                rootPath = '.\\informes'
                for file in os.listdir(rootPath):
                    if file.endswith(nombre):
                        os.startfile('%s\\%s' % (rootPath, file))
        except Exception as error:
            print('Error Informe Factura :', error)

    def topFactura(titulo):
        """
            Configura la parte superior del informe de la factura.

            :param titulo: El título del informe.
            :type titulo: str
        """
        try:
            ruta_logo = '.\\img\\logo.ico'
            logo = Image.open(ruta_logo)

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'Transportes Teis')
                var.report.drawString(230, 670, titulo)
                var.report.line(50, 665, 525, 665)

                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40, mask='auto')

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - España')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: cartesteisr@mail.com')

                Facturas.cargarCabeceraFactura()
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')
        except Exception as error:
            print('Error en cabecera factura:', error)

    def cargarCabeceraFactura(self=None):
        """
        Carga la cabecera del informe de la factura.

        :param self: Referencia a la instancia actual de la clase. Por defecto es None.
        :type self: None or Class instance
        """
        try:
            numFact = var.ui.lblFactutaciontxt.text()
            factura = ddbb.DDBB.oneFactura(numFact)
            cliente = ddbb.DDBB.codCli(str(factura[1]))
            var.report.setFont('Helvetica-Bold', size=8)
            var.report.drawString(290, 785, 'NÚMERO FACTURA: ' + numFact)
            var.report.drawString(400, 785, 'Fecha: ' + factura[2])
            var.report.drawString(290, 770, 'CLIENTE')
            var.report.setFont('Helvetica', size=8)
            var.report.drawString(290, 755, 'CIF: ' + factura[1])
            var.report.drawString(290, 740, 'Razón Social: ' + cliente[2])
            var.report.drawString(290, 725, 'Dirección: ' + cliente[3])
            var.report.drawString(290, 710, 'Provincia: ' + cliente[5])
            var.report.drawString(290, 695, 'Teléfono: ' + cliente[4])
        except Exception as error:
            print('Error en cargar cabecera factura:', error)

    def footFactura(titulo):
        """
        Carga el pie del informe de la factura.
        :param titulo: El título del informe.
        :type titulo: str
        """
        try:
            Facturas.cargarPieFactura()
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

    def cargarPieFactura(self=None):
        """
        Carga el pie de la factura en el informe PDF.
        """
        try:
            var.report.line(50, 125, 525, 125)
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(385, 110, 'SUBTOTAL: ')
            var.report.drawString(450, 110, var.ui.lbl_subTotal.text())
            var.report.drawString(423, 95, 'IVA: ')
            var.report.drawString(450, 95, var.ui.lbl_iva.text())
            var.report.drawString(407, 80, 'TOTAL: ')
            var.report.drawString(450, 80, var.ui.lbl_total.text())

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

    def ajustarTamanho(texto, maximo):
        """
        Ajusta la longitud de un texto para que no exceda un máximo dado, truncando el texto si es necesario.

            :param texto: El texto que se desea ajustar.
            :type texto: str
            :param maximo: La longitud máxima permitida para el texto.
            :type maximo: int
            :return: El texto ajustado.
            :rtype: str
        """
        try:
            mensaje = str(texto)
            if len(mensaje) > maximo:
                mensaje = mensaje[:(maximo - 1)] + "..."
            return mensaje
        except Exception as error:
            print('Error al ajustar el tamaño del texto: ', error)



