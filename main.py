from PyQt6.QtCore import QTimer, QSize

import clientes
import ddbb
import facturas
import informes
from mainWindows import *
from datetime import datetime

import sys, var, conductores, eventos, windowAux, locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.calendar = windowAux.Calendar()
        var.salir = windowAux.Salir()
        var.calendarBaja = windowAux.CalendarBaja()
        var.calendarAltaFacturas = windowAux.CalendarAltaFactura()
        var.conductores = conductores.Conductores()
        var.acercaDe = windowAux.AcercaDe()
        var.altaNueva = windowAux.AltaNueva()
        var.bajaCliente = windowAux.CalendarBajaCliente()
        var.bajaNuevaCliente = windowAux.BajaNuevaCliente()
        var.bajaNueva = windowAux.BajaNueva()
        var.ddbb = ddbb.DDBB()
        var.ddbb.conexion()
        ddbb.DDBB.mostrarConductores(self)
        ddbb.DDBB.mostrarClientes(self)
        ddbb.DDBB.mostrarFacturas(self)
        var.dlgAbrir = windowAux.FileDialogAbrir()

        #Eventos de tablas
        eventos.Eventos.resizeTablaConductores(self)
        eventos.Eventos.resizeTablaClientes(self)
        eventos.Eventos.resizeTablaFacturas(self)
        eventos.Eventos.resizeTabViajes(self)


        #Cargar combos
        var.ddbb.cargarProvincia()
        var.ui.comboProvincia.currentIndexChanged.connect(ddbb.DDBB.cargarLocalidades)
        var.ddbb.cargarProvinciaClientes()
        var.ui.comboProvinciaCliente.currentIndexChanged.connect(var.ddbb.cargarLocalidadesClientes)
        var.ddbb.cargarConductores()

        var.ddbb.cargarProvinciaFacturas()
        var.ui.cmbProvinciasVentas.currentIndexChanged.connect(ddbb.DDBB.cargarLocalidadesFacturas)

        var.ddbb.cargarProvinciaFacturas2()
        var.ui.cmbProvinciasVentas_2.currentIndexChanged.connect(ddbb.DDBB.cargarLocalidadesFacturas2)
        var.ui.cmbMunicipiosVentas.currentIndexChanged.connect(ddbb.DDBB.datosViaje)
        var.ui.cmbMunicipiosVentas_2.currentIndexChanged.connect(ddbb.DDBB.datosViaje)
        var.ui.cmbProvinciasVentas.currentIndexChanged.connect(ddbb.DDBB.datosViaje)
        var.ui.cmbProvinciasVentas_2.currentIndexChanged.connect(ddbb.DDBB.datosViaje)




        #Acciones de los botones

        var.ui.btnBuscar.clicked.connect(ddbb.DDBB.buscarConductor)
        var.ui.btnBuscarCliente.clicked.connect(ddbb.DDBB.buscarCliente)
        var.ui.btnCalendario.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.actionSalir.triggered.connect(eventos.Eventos.abrirSalir)
        var.ui.actionAcercaDe.triggered.connect(eventos.Eventos.abrirAcercaDe)
        var.ui.botonAltaConductor.clicked.connect(conductores.Conductores.altaConductor)
        var.ui.botonAltaCliente.clicked.connect(clientes.Clientes.altaCliente)
        var.ui.botonModificarConductor.clicked.connect(ddbb.DDBB.modificarConductor)
        var.ui.botonModificarCliente.clicked.connect(ddbb.DDBB.modificarCliente)
        var.ui.botonBajaConductor.clicked.connect(eventos.Eventos.abrirBajaNueva)
        var.ui.botonBajaCliente.clicked.connect(eventos.Eventos.abrirBajaCliente)
        var.ui.btnCalendarioFacturacion.clicked.connect(eventos.Eventos.abrirCalendarAltaFactura)
        var.ui.btnFacturar.clicked.connect(facturas.Facturas.altaFactura)
        var.ui.btnGrabar.clicked.connect(facturas.Facturas.cargarLineaVenta)




        #Eventos plaintext
        var.ui.textoDNI.editingFinished.connect(eventos.Eventos.validarDNI)
        var.ui.textoDNICliente.editingFinished.connect(clientes.Clientes.validarDNI)
        var.ui.textoNombre.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.textoApellidos.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.textoSalario.editingFinished.connect(eventos.Eventos.formatSalario)
        var.ui.textoTelefono.editingFinished.connect(eventos.Eventos.formatTelefono)
        var.ui.textoTelefonoCliente.editingFinished.connect(clientes.Clientes.formatTelefonoClientes)

        #Eventos tabla & actions
        var.ui.actionBarSalir.triggered.connect(eventos.Eventos.abrirSalir)
        var.ui.actionBarLimpiarPanel.triggered.connect(eventos.Eventos.limpiarPanel)
        var.ui.actionBarLimpiarPanel.triggered.connect(eventos.Eventos.limpiarPanelClientes)
        var.ui.actionBarLimpiarPanel.triggered.connect(eventos.Eventos.limpiarPanelFacturas)
        var.ui.actionCrearCopia.triggered.connect(eventos.Eventos.crearCopia)
        var.ui.actionImportarCopia.triggered.connect(eventos.Eventos.importarCopia)
        var.ui.actionExportarExcel.triggered.connect(eventos.Eventos.exportarExcel)
        var.ui.actionImportarDatosExcel.triggered.connect(eventos.Eventos.importarCondutoresExcel)
        var.ui.actionImportarClientesExcel.triggered.connect(eventos.Eventos.importarClientesExcel)
        var.ui.tablaConductores.clicked.connect(conductores.Conductores.cargarDesdeTabla)
        var.ui.tablaClientes.clicked.connect(clientes.Clientes.cargarDesdeTabla)
        var.ui.actionLISTADO_CLIENTES.triggered.connect(informes.Informes.reportclientes)
        var.ui.actionLISTADO_CONDUCTORES.triggered.connect(informes.Informes.reportdrivers)
        var.ui.tablaFacturas.clicked.connect(facturas.Facturas.cargarDesdeTabla)
        var.ui.tabViajes.clicked.connect(facturas.Facturas.cargarViaje)
        var.ui.actionCreaerInformeBarra.triggered.connect(informes.Informes.checkboxinforme)
        var.ui.actionFACTURAS.triggered.connect(facturas.Facturas.reportfactura)

        self.cargarStatusbar()

        radioConductor = [var.ui.radioTodos, var.ui.radioAlta, var.ui.radioBaja]
        for i in radioConductor:
            i.toggled.connect(ddbb.DDBB.mostrarConductores)
        radioCliente = [var.ui.radioTodosCliente, var.ui.radioAltaCliente]
        for i in radioCliente:
            i.toggled.connect(ddbb.DDBB.mostrarClientes)


    def cargarStatusbar(self):
        self.labelVersion = QtWidgets.QLabel("0.1.0", self)
        self.labelVersion.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelVersion.setStyleSheet("margin-left: 10px;")
        var.ui.statusbar.addPermanentWidget(self.labelVersion, 1)

        self.actualizarFecha()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizarFecha)
        self.timer.start(60000)

    def actualizarFecha(self):
        if hasattr(self, 'labelstatus') and self.labelstatus is not None:
            var.ui.statusbar.removeWidget(self.labelstatus)
            self.labelstatus = None
        self.labelstatus = QtWidgets.QLabel("Hora: " + datetime.now().strftime('%H:%M')+" Fecha: " + datetime.now().strftime('%A - %d/%m/%Y'), self)
        self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        var.ui.statusbar.addPermanentWidget(self.labelstatus, 2)

    def closeEvent(self, event):
        mbox = QtWidgets.QMessageBox.information(self, 'Salida', '¿Seguro que deseas salir?',
                                         QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())