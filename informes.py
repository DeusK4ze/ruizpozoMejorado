import os, var, shutil
from PIL import Image
from PyQt6 import QtSql, QtWidgets, QtGui
from reportlab.pdfgen import canvas
from datetime import datetime
from svglib.svglib import svg2rlg
import ddbb

class Informes:

    def encriptarDNI(dni):
        """
        Encripta parcialmente el DNI ocultando parte de sus dígitos.
        :return:
            str: El DNI encriptado.
        :rtype:
        """
        dni = "******" + dni[6:]
        dni_lista = list(dni)
        dni_lista[8] = "*"
        dni_modificado = ''.join(dni_lista)
        return dni_modificado
    @staticmethod
    def reportclientes():
        """
        Genera un informe en formato PDF con un listado de clientes.

        Returns:
            None
        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadoclientes.pdf'
            var.report = canvas.Canvas('informes/' + nombre)
            titulo = 'LISTADO CLIENTES'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            items = 'CODIGO', 'DNI', 'RAZON SOCIAL', 'MUNICIPIO', 'TELEFONO', 'FECHA BAJA'
            var.report.setFont('Helvetica-Bold', size=9)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(120, 675, str(items[1]))
            var.report.drawString(170, 675, str(items[2]))
            var.report.drawString(290, 675, str(items[3]))
            var.report.drawString(390, 675, str(items[4]))
            var.report.drawString(460, 675, str(items[5]))
            var.report.line(50, 670, 525, 670)
            # obtencion datos de la base de datos
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, dni, razon_social, municipio, telefono, baja from clientes order by razon_social')
            var.report.setFont('Helvetica', size=9)
            if query.exec():
                i = 60
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(450, 80, 'Pagina siguiente...')
                        var.report.showPage()  # crea una pagina nueva
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo)
                        var.report.setFont('Helvetica', size=10)
                        var.report.drawString(60, 675, str(items[0]))
                        var.report.drawString(120, 675, str(items[1]))
                        var.report.drawString(170, 675, str(items[2]))
                        var.report.drawString(290, 675, str(items[3]))
                        var.report.drawString(390, 675, str(items[4]))
                        var.report.drawString(460, 675, str(items[5]))
                        var.report.line(50, 670, 525, 670)
                        i = 60
                        j = 655
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawCentredString(i, j, str(query.value(0)))
                    var.report.drawString(i + 40, j, Informes.encriptarDNI(str(query.value(1))))
                    var.report.drawString(i + 115, j, str(query.value(2)))
                    var.report.drawString(i + 235, j, str(query.value(3)))
                    var.report.drawString(i + 335, j, str(query.value(4)))
                    var.report.drawString(i + 405, j, str(query.value(5)))
                    j = j - 20
            var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith(nombre):
                    os.startfile('%s\\%s' % (rootPath, file))
        except Exception as error:
            print('Error LISTADO CLIENTES :', error)

    @staticmethod
    def reportdrivers():
        """
        Genera un informe en formato PDF con un listado de conductores.

        Returns:
            None
        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadoconductores.pdf'
            var.report = canvas.Canvas('informes/' + nombre)
            titulo = 'LISTADO CONDUCTORES'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            items = 'CODIGO', 'APELLIDOS', 'NOMBRE', 'TELEFONO', 'LICENCIAS', 'FECHA BAJA'
            var.report.setFont('Helvetica-Bold', size=9)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(120, 675, str(items[1]))
            var.report.drawString(210, 675, str(items[2]))
            var.report.drawString(290, 675, str(items[3]))
            var.report.drawString(390, 675, str(items[4]))
            var.report.drawString(460, 675, str(items[5]))
            var.report.line(50, 670, 525, 670)
            # obtencion datos de la base de datos
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, apellidos, nombre, telefono, carnet, baja from conductores order by apellidos')
            var.report.setFont('Helvetica', size=9)
            if query.exec():
                i = 60
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(450, 80, 'Pagina siguiente...')
                        var.report.showPage()  # crea una pagina nueva
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo)
                        var.report.setFont('Helvetica', size=10)
                        var.report.drawString(60, 675, str(items[0]))
                        var.report.drawString(120, 675, str(items[1]))
                        var.report.drawString(210, 675, str(items[2]))
                        var.report.drawString(290, 675, str(items[3]))
                        var.report.drawString(390, 675, str(items[4]))
                        var.report.drawString(460, 675, str(items[5]))
                        var.report.line(50, 670, 525, 670)
                        i = 60
                        j = 655
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawCentredString(i, j, str(query.value(0)))
                    var.report.drawString(i + 50, j, str(query.value(1)))
                    var.report.drawString(i + 155, j, str(query.value(2)))
                    var.report.drawString(i + 235, j, str(query.value(3)))
                    var.report.drawCentredString(i + 345, j, str(query.value(4)))
                    var.report.drawString(i + 405, j, str(query.value(5)))
                    j = j - 20
            var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith(nombre):
                    os.startfile('%s\\%s' % (rootPath, file))
        except Exception as error:
            print('Error LISTADO conductores :', error)

    def topInforme(titulo):
        """
        Dibuja la cabecera del informe en el documento PDF.

        Args:
            titulo (str): El título del informe.

        Returns:
            None
        """
        try:
            ruta_logo = '.\\img\\logo.ico'
            logo = Image.open(ruta_logo)

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'Transportes Teis')
                var.report.drawString(240, 695, titulo)
                var.report.line(50, 690, 525, 690)

                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - España')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: cartesteisr@mail.com')
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')
        except Exception as error:
            print('Error en cabecera informe:', error)

    def footInforme(titulo):
        """
        Dibuja el pie de página del informe en el documento PDF.

        Args:
            titulo (str): El título del informe.

        Returns:
            None
        """
        try:
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

    @staticmethod
    def checkboxinforme():
        """
        Muestra un cuadro de diálogo para seleccionar los informes que se desean generar y genera los informes correspondientes.

        Returns:
            None
        """
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Realizar Informe")
            mbox.setWindowIcon(QtGui.QIcon("img/informe.ico"))
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setText("Seleccione informe/es")

            conductorcheck = QtWidgets.QCheckBox("Informe de conductores")
            clientecheck = QtWidgets.QCheckBox("Informe de clientes")

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(conductorcheck)
            layout.addWidget(clientecheck)

            container = QtWidgets.QWidget()
            container.setLayout(layout)

            mbox.layout().addWidget(container, 1, 1, 1, mbox.layout().columnCount())

            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Aceptar')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('Cancelar')

            resultado = mbox.exec()

            if resultado == QtWidgets.QMessageBox.StandardButton.Yes:
                if conductorcheck.isChecked():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Informe de conductores creado')
                    msg.exec()
                    Informes.reportdrivers()
                if clientecheck.isChecked():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Informe de clientes creado')
                    msg.exec()
                    Informes.reportclientes()

                if not (conductorcheck.isChecked() or clientecheck.isChecked()):
                    eventos.Eventos.error("Aviso", "No se ha seleccionado ningún informe")

        except Exception as error:
            print("Error en checkbox_informe", error)


