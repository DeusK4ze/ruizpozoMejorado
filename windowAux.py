import facturas
from calendarWindow import *
from dlgSalir import *
from dlgAcercaDe import *
from dlgBuscar import *
from dlgAltaNueva import *
from dlgBajaNueva import *
from datetime import datetime

import var, conductores, eventos, ddbb, clientes

class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_ventanaCalendario()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        anho = datetime.now().year
        var.calendar.calendar.setSelectedDate(QtCore.QDate(anho, mes, dia))
        var.calendar.calendar.clicked.connect(conductores.Conductores.cargarFecha)

class CalendarBaja(QtWidgets.QDialog):
    def __init__(self):
        super(CalendarBaja, self).__init__()
        var.calendarBaja = Ui_ventanaCalendario()
        var.calendarBaja.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        anho = datetime.now().year
        var.calendarBaja.calendar.setSelectedDate(QtCore.QDate(anho, mes, dia))
        var.calendarBaja.calendar.clicked.connect(conductores.Conductores.borrarConductor)

class CalendarBajaCliente(QtWidgets.QDialog):
    def __init__(self):
        super(CalendarBajaCliente, self).__init__()
        var.calendarBajaCliente = Ui_ventanaCalendario()
        var.calendarBajaCliente.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        anho = datetime.now().year
        var.calendarBajaCliente.calendar.setSelectedDate(QtCore.QDate(anho, mes, dia))
        var.calendarBajaCliente.calendar.clicked.connect(clientes.Clientes.borrarCliente)

class CalendarAltaFactura(QtWidgets.QDialog):
    def __init__(self):
        super(CalendarAltaFactura, self).__init__()
        var.calendarAltaFacturas = Ui_ventanaCalendario()
        var.calendarAltaFacturas.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        anho = datetime.now().year
        var.calendarAltaFacturas.calendar.setSelectedDate(QtCore.QDate(anho, mes, dia))
        var.calendarAltaFacturas.calendar.clicked.connect(facturas.Facturas.cargarFecha)

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()


class AltaNueva(QtWidgets.QDialog):
    def __init__(self):
        super(AltaNueva, self).__init__()
        var.altaNueva = Ui_dlgAltaNueva()
        var.altaNueva.setupUi(self)

        var.altaNueva.btnAltaNueva.clicked.connect(ddbb.DDBB.altaNueva)
        var.altaNueva.btnAltaNueva.clicked.connect(ddbb.DDBB.modificarConductor)
        var.altaNueva.btnAltaCerrar.clicked.connect(eventos.Eventos.cerrarAltaNueva)

class BajaNueva(QtWidgets.QDialog):
    def __init__(self):
        super(BajaNueva, self).__init__()
        var.bajaNueva = Ui_dlgBajaNueva()
        var.bajaNueva.setupUi(self)

        var.bajaNueva.btnBajaNueva.clicked.connect(eventos.Eventos.abrirCalendarBaja)
        var.bajaNueva.btnBajaNueva.clicked.connect(eventos.Eventos.cerrarBajaNueva)
        var.bajaNueva.btnBajaCerrar.clicked.connect(eventos.Eventos.cerrarBajaNueva)

class BajaNuevaCliente(QtWidgets.QDialog):
    def __init__(self):
        super(BajaNuevaCliente, self).__init__()
        var.bajaNuevaCliente = Ui_dlgBajaNueva()
        var.bajaNuevaCliente.setupUi(self)

        var.bajaNuevaCliente.btnBajaNueva.clicked.connect(eventos.Eventos.abrirCalendarBajaCliente)
        var.bajaNuevaCliente.btnBajaNueva.clicked.connect(eventos.Eventos.cerrarBajaNuevaCliente)
        var.bajaNuevaCliente.btnBajaCerrar.clicked.connect(eventos.Eventos.cerrarBajaNuevaCliente)

class AcercaDe(QtWidgets.QDialog):
    def __init__(self):
        super(AcercaDe, self).__init__()
        var.acercaDe = Ui_dlgAcercaDe()
        var.acercaDe.setupUi(self)

        #Acciones de los botones
        var.acercaDe.btnCerrarAcercaDe.clicked.connect(eventos.Eventos.cerrarAcercaDe)

class Salir(QtWidgets.QDialog):
    def __init__(self):
        super(Salir, self).__init__()
        var.salir = Ui_dlgSalir()
        var.salir.setupUi(self)

        #Acciones de los botones
        var.salir.btnSalirSalir.clicked.connect(eventos.Eventos.salir)
        var.salir.btnSalirCancelar.clicked.connect(eventos.Eventos.cerrarSalir)