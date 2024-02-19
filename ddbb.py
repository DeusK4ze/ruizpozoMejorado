from PyQt6 import QtWidgets, QtSql, QtCore, QtGui
from datetime import date, datetime

import conductores
import ddbb, clientes
import eventos
import facturas
import var


class DDBB():
    def conexion(self=None):
        """
        Establece conexión col la base de datos
        """
        var.base = 'ddbb.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.base)

        if not db.open():
            print("error de conexion con la ddbb")
        else:
            print("conexion correcta con la ddbb")

    def cargarLocalidades(self=None):
        """
        Carga las localidades correspondientes a la provincia seleccionada en el comboProvincia en el comboLocalidad.

        Args:
            self: Referencia a la instancia de la clase (puede ser None si no se usa).

        Returns:
            None
        """
        try:
            id = 0
            var.ui.comboLocalidad.clear()
            prov = var.ui.comboProvincia.currentText()
            query = QtSql.QSqlQuery()
            query.prepare("select id from provincias where provincia = :prov")
            query.bindValue(":prov", prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare("select municipio from municipios where id_provincia = :id")
            query1.bindValue(":id", int(id))
            if query1.exec():
                var.ui.comboLocalidad.addItem("Seleccione provincia")
                while query1.next():
                    var.ui.comboLocalidad.addItem(query1.value(0))

        except Exception as error:
            print("Error en cargarLocalidades:", error)

    def cargarProvincia(self=None):
        """
        Carga las provincias disponibles en la base de datos en el comboProvincia.

        Args:
            self: Referencia a la instancia de la clase (puede ser None si no se usa).

        Returns:
            None
        """
        try:
            var.ui.comboProvincia.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.comboProvincia.addItem('')
                while query.next():
                    var.ui.comboProvincia.addItem(query.value(0))
        except Exception as error:
            print("Error en cargarProvincia:", error)

    def cargarLocalidadesClientes(self=None):
        """
        Carga las localidades correspondientes a la provincia seleccionada en el comboProvinciaCliente en el comboLocalidadCliente.

        Args:
            self: Referencia a la instancia de la clase (puede ser None si no se usa).

        Returns:
            None
        """
        try:
            id = 0
            var.ui.comboLocalidadCliente.clear()
            prov = var.ui.comboProvinciaCliente.currentText()
            query = QtSql.QSqlQuery()
            query.prepare("select id from provincias where provincia = :prov")
            query.bindValue(":prov", prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare("select municipio from municipios where id_provincia = :id")
            query1.bindValue(":id", int(id))
            if query1.exec():
                var.ui.comboLocalidadCliente.addItem("Seleccione provincia")
                while query1.next():
                    var.ui.comboLocalidadCliente.addItem(query1.value(0))

        except Exception as error:
            print("Error en cargarLocalidadesClientes:", error)

    def cargarProvinciaClientes(self=None):
        """
        Carga las provincias disponibles en la base de datos en el comboProvinciaCliente.

        Args:
            self: Referencia a la instancia de la clase (puede ser None si no se usa).

        Returns:
            None
        """
        try:
            var.ui.comboProvinciaCliente.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.comboProvinciaCliente.addItem('')
                while query.next():
                    var.ui.comboProvinciaCliente.addItem(query.value(0))
        except Exception as error:
            print("error en cagarProvincia", error)

    def cargarLocalidadesFacturas(self=None):
        """
        Carga las localidades correspondientes a la provincia seleccionada en el cmbProvinciasVentas en el cmbMunicipiosVentas.

        Args:
            self: Referencia a la instancia de la clase (puede ser None si no se usa).

        Returns:
            None
        """
        try:
            id = 0
            var.ui.cmbMunicipiosVentas.clear()
            prov = var.ui.cmbProvinciasVentas.currentText()
            query = QtSql.QSqlQuery()
            query.prepare("select id from provincias where provincia = :prov")
            query.bindValue(":prov", prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare("select municipio from municipios where id_provincia = :id")
            query1.bindValue(":id", int(id))
            if query1.exec():
                var.ui.cmbMunicipiosVentas.addItem("Seleccione provincia")
                while query1.next():
                    var.ui.cmbMunicipiosVentas.addItem(query1.value(0))
        except Exception as error:
            print("Error en cargarLocalidadesFacturas:", error)

    def cargarProvinciaFacturas(self=None):
        """
        Carga las provincias disponibles en la base de datos en el cmbProvinciasVentas.

        Args:
            self: Referencia a la instancia de la clase (puede ser None si no se usa).

        Returns:
            None
        """
        try:
            var.ui.cmbProvinciasVentas.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProvinciasVentas.addItem('')
                while query.next():
                    var.ui.cmbProvinciasVentas.addItem(query.value(0))
        except Exception as error:
            print("Error en cargarProvinciaFacturas:", error)

    def cargarLocalidadesFacturas2(self=None):
        """
        Carga las localidades correspondientes a la provincia seleccionada en el cmbProvinciasVentas_2 en el cmbMunicipiosVentas_2.

        Args:
            self: Referencia a la instancia de la clase (puede ser None si no se usa).

        Returns:
            None
        """
        try:
            id = 0
            var.ui.cmbMunicipiosVentas_2.clear()
            prov = var.ui.cmbProvinciasVentas_2.currentText()
            query = QtSql.QSqlQuery()
            query.prepare("select id from provincias where provincia = :prov")
            query.bindValue(":prov", prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare("select municipio from municipios where id_provincia = :id")
            query1.bindValue(":id", int(id))
            if query1.exec():
                var.ui.cmbMunicipiosVentas_2.addItem("Seleccione provincia")
                while query1.next():
                    var.ui.cmbMunicipiosVentas_2.addItem(query1.value(0))
        except Exception as error:
            print("Error en cargarLocalidadesFacturas2:", error)

    def cargarProvinciaFacturas2(self=None):
        """
            Carga las provincias disponibles en la base de datos en el cmbProvinciasVentas_2.
            Args:
                self: Referencia a la instancia de la clase (puede ser None si no se usa).
            Returns:
                None
        """

        try:

            var.ui.cmbProvinciasVentas_2.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProvinciasVentas_2.addItem('')
                while query.next():
                    var.ui.cmbProvinciasVentas_2.addItem(query.value(0))
        except Exception as error:
            print("error en cagarProvincia", error)

    @staticmethod
    def selectDriversAll():
        """
    Selecciona todos los registros de conductores en la base de datos y los devuelve como una lista de listas.

    Returns:
        list: Una lista de listas que contiene los registros de conductores.
    """
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from conductores order by apellidos")
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            return registros
        except Exception as error:
            print("error en select all drivers", error)

    def oneConductor(id):
        """
    Selecciona un conductor específico de la base de datos según su identificador y devuelve sus detalles como una lista.

    Args:
        id (int): El identificador del conductor que se desea seleccionar.

    Returns:
        list: Una lista que contiene los detalles del conductor seleccionado.
    """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from conductores where codigo = :id")
            query.bindValue(":id", int(id))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("error en oneConductor", error)

    def oneCliente(id):
        """
    Selecciona un cliente específico de la base de datos según su identificador y devuelve sus detalles como una lista.

    Args:
        id (int): El identificador del cliente que se desea seleccionar.

    Returns:
        list: Una lista que contiene los detalles del cliente seleccionado.
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from clientes where codigo = :id")
            query.bindValue(":id", int(id))
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("error en oneCliente", error)

    def codCli(id):
        """
    Busca y devuelve el código del cliente asociado a un DNI específico en la base de datos.

    Args:
        id (str): El DNI del cliente del cual se desea obtener el código.

    Returns:
        list: Una lista que contiene el código del cliente y otros detalles asociados.
    """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from clientes where dni = :id")
            query.bindValue(":id", id)  # No es necesario convertir a entero aquí
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("Error en oneCliente:", error)

    def oneFactura(numfac):
        """

        :return:
        :rtype:
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from facturas where numfac = :numfac")
            query.bindValue(":numfac", numfac)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))
            else:
                print("La consulta no se ejecutó correctamente.")
            return registro
        except Exception as error:
            print("error en oneFactura", error)

    def oneviaje(id):
        """

        :return:
        :rtype:
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from viajes where idViaje = :id')
            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(6):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print('error en oneviaje ', error)

    def mostrarClientes(self=None):
        """

        """
        try:
            registros = []
            query = QtSql.QSqlQuery()
            if var.ui.radioAltaCliente.isChecked():
                query.prepare(
                    "select codigo, razon_social, direccion, provincia, telefono, baja from clientes where baja is null")
            else:
                query.prepare("select codigo, razon_social, direccion, provincia, telefono, baja from clientes")
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            if registros:
                clientes.Clientes.cargarTablaClientes(registros)
            else:
                var.ui.tablaClientes.setRowCount(0)
        except Exception as error:
            print("error en mostrarConductores", error)

    def mostrarConductores(self=None):
        """

        """
        try:
            registros = []
            query = QtSql.QSqlQuery()
            if var.ui.radioAlta.isChecked():
                query.prepare(
                    "select codigo, apellidos, nombre, telefono, carnet, baja from conductores where baja is null")
            elif var.ui.radioBaja.isChecked():
                query.prepare(
                    "select codigo, apellidos, nombre, telefono, carnet, baja from conductores where baja is not null")
            else:
                query.prepare("select codigo, apellidos, nombre, telefono, carnet, baja from conductores")
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            if registros:
                conductores.Conductores.cargarTablaConductores(registros)
            else:
                var.ui.tablaConductores.setRowCount(0)
        except Exception as error:
            print("error en mostrarConductores", error)

    def mostrarFacturas(self=None):
        """

        """
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare("select numfac, dnicliente from facturas")
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            facturas.Facturas.cargarTablaFacturas(registros)
        except Exception as error:
            print("error en mostrarFacturas", error)

    def borrarConductor(dni, fechaBaja):
        """

        :param fechaBaja:
        :type fechaBaja:
        """
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare("select baja from conductores where dni = :dni")
            query1.bindValue(":dni", str(dni))
            valor = ""
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)

            query = QtSql.QSqlQuery()
            query.prepare("update conductores set baja = :fechaBaja where dni = :dni")
            query.bindValue(":fechaBaja", fechaBaja)
            query.bindValue(":dni", str(dni))
            if query.exec():
                if str(valor) == "":
                    eventos.Eventos.mostrarMensaje("Usuario dado de baja")
                else:
                    eventos.Eventos.mostrarMensaje("Fecha de baja actualizada")

            else:
                eventos.Eventos.mostrarMensaje("No se ha podido dar de baja")

        except Exception as error:
            print("error en borrarConductor", error)

    def borrarCliente(dni, fechaBaja):
        """

        :param fechaBaja:
        :type fechaBaja:
        """
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare("select baja from clientes where dni = :dni")
            query1.bindValue(":dni", str(dni))
            valor = ""
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)

            query = QtSql.QSqlQuery()
            query.prepare("update clientes set baja = :fechaBaja where dni = :dni")
            query.bindValue(":fechaBaja", fechaBaja)
            query.bindValue(":dni", str(dni))
            if query.exec():
                if str(valor) == "":
                    eventos.Eventos.mostrarMensaje("Cliente dado de baja")
                else:
                    eventos.Eventos.mostrarMensaje("Fecha de baja actualizada")
            else:
                eventos.Eventos.mostrarMensaje("No se ha podido dar de baja")

        except Exception as error:
            print("error en borrar cliente", error)

    def buscarConductor(self=None):
        """

        """
        try:
            dni = var.ui.textoDNI.text().upper()
            query = QtSql.QSqlQuery()
            query.prepare("select codigo from conductores where dni = :dni")
            query.bindValue(":dni", str(dni))
            if query.exec():
                while query.next():
                    codigo = query.value(0)
            registro = DDBB.oneConductor(codigo)

            conductores.Conductores.cargarConductor(registro)
            var.ui.tablaConductores.scrollToItem(var.ui.tablaConductores.item(codigo, 0))

            DDBB.mostrarConductores()
            conductores.Conductores.colorearFila(codigo)
            #eventos.Eventos.cerrarBuscar(self)

        except Exception as error:
            eventos.Eventos.mostrarMensaje("No se ha encontrado el conductor")


    def buscarCliente(self=None):
        """

        """
        try:
            dni = var.ui.textoDNICliente.text().upper()
            query = QtSql.QSqlQuery()
            query.prepare("select codigo from clientes where dni = :dni")
            query.bindValue(":dni", str(dni))
            if query.exec():
                while query.next():
                    codigo = query.value(0)
            registro = DDBB.oneCliente(codigo)
            print(codigo)
            print(registro)
            clientes.Clientes.cargarCliente(registro)
            var.ui.tablaClientes.scrollToItem(var.ui.tablaClientes.item(codigo, 0))
            DDBB.mostrarClientes()
            clientes.Clientes.colorearFila(codigo)
        except Exception as error:
            eventos.Eventos.mostrarMensaje("No se ha encontrado el cliente")

    @staticmethod
    def guardarConductor(newDriver, estado):
        """

        :param newDriver:
        :type newDriver:
        :param estado:
        :type estado:
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("insert into conductores (dni, alta, apellidos, nombre,  "
                          " direccion, provincia, municipio, telefono, salario, carnet) "
                          " VALUES (:dni, :alta, :apellidos, :nombre, :direccion, :provincia, "
                          " :municipio, :telefono, :salario, :carnet)")
            query.bindValue(":dni", str(newDriver[0]))
            query.bindValue(":alta", str(newDriver[1]))
            query.bindValue(":apellidos", str(newDriver[2]))
            query.bindValue(":nombre", str(newDriver[3]))
            query.bindValue(":direccion", str(newDriver[4]))
            query.bindValue(":provincia", str(newDriver[5]))
            query.bindValue(":municipio", str(newDriver[6]))
            query.bindValue(":telefono", str(newDriver[7]))
            query.bindValue(":salario", str(newDriver[8]))
            query.bindValue(":carnet", str(newDriver[9]))

            if query.exec():
                if estado == 0:
                    eventos.Eventos.mostrarMensaje("Empleado dado de alta")
                    eventos.Eventos.limpiarPanel()
                    ddbb.DDBB.mostrarConductores()
            else:
                eventos.Eventos.mostrarMensaje(query.lastError().text())

        except Exception as error:
            print("error en guardar conductor", error)

    @staticmethod
    def guardarCliente(cliente, estado):
        """

        :param cliente:
        :type cliente:
        :param estado:
        :type estado:
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("insert into clientes (dni, razon_social, direccion, telefono,  "
                          " provincia, municipio) VALUES (:dni, :razon_social, :direccion, :telefono, :provincia, :municipio)")
            query.bindValue(":dni", str(cliente[0]))
            query.bindValue(":razon_social", str(cliente[1]))
            query.bindValue(":direccion", str(cliente[2]))
            query.bindValue(":telefono", str(cliente[3]))
            query.bindValue(":provincia", str(cliente[4]))
            query.bindValue(":municipio", str(cliente[5]))

            if query.exec():
                if estado == 0:
                    eventos.Eventos.mostrarMensaje("Cliente dado de alta")
                    eventos.Eventos.limpiarPanelClientes()
                    ddbb.DDBB.mostrarClientes()
            else:
                if estado == 0:
                    eventos.Eventos.mostrarMensaje(query.lastError().text())

        except Exception as error:
            print("error en guardar conductor", error)

    @staticmethod
    def altaNueva():
        """

        """
        modiDriver = conductores.Conductores.getActualizacionDriver()
        if modiDriver is not None:
            query = QtSql.QSqlQuery()
            query.prepare("update conductores set alta = :alta, baja = :baja where codigo = :codigo")
            query.bindValue(":codigo", int(modiDriver[0]))
            query.bindValue(":alta", str(modiDriver[2]))
            query.bindValue(":baja", None)

            if query.exec():
                var.altaNueva.hide()
                DDBB.mostrarConductores()
                DDBB.cargarConductores()
            else:
                eventos.Eventos.mostrarMensaje("Error al dar otra vez de alta")

    @staticmethod
    def modificarConductor():
        """

        """
        try:
            modiDriver = conductores.Conductores.getActualizacionDriver()
            if modiDriver is not None:
                registro = DDBB.oneConductor(int(modiDriver[0]))
                query = QtSql.QSqlQuery()
                query.prepare(
                    "update conductores set dni = :dni, alta = :alta, apellidos = :apellidos, nombre = :nombre, "
                    " direccion = :direccion, provincia = :provincia, municipio = :municipio, telefono = :telefono, "
                    "salario = :salario, carnet = :carnet where codigo = :codigo")
                query.bindValue(":codigo", int(modiDriver[0]))
                query.bindValue(":dni", str(modiDriver[1]))
                query.bindValue(":alta", str(modiDriver[2]))
                query.bindValue(":apellidos", str(modiDriver[3]))
                query.bindValue(":nombre", str(modiDriver[4]))
                query.bindValue(":direccion", str(modiDriver[5]))
                query.bindValue(":provincia", str(modiDriver[6]))
                query.bindValue(":municipio", str(modiDriver[7]))
                query.bindValue(":telefono", str(modiDriver[8]))
                query.bindValue(":salario", str(modiDriver[9]))
                query.bindValue(":carnet", str(modiDriver[10]))

                if modiDriver[2] != registro[2] and registro[11] != "":
                    var.altaNueva.show()
                else:
                    if query.exec():
                        eventos.Eventos.mostrarMensaje("Datos del conductor modificados")
                        DDBB.mostrarConductores()
                        eventos.Eventos.limpiarPanel()
                    else:
                        eventos.Eventos.mostrarMensaje(query.lastError().text())

        except Exception as error:
            print("error en modificar conductor", error)

    @staticmethod
    def modificarCliente():
        """

        """
        try:
            modiCliente = clientes.Clientes.getActualizacionCliente()
            if modiCliente is not None:
                query = QtSql.QSqlQuery()
                query.prepare(
                    "update clientes set dni = :dni, razon_social = :razon_social, direccion = :direccion, "
                    " telefono = :telefono, provincia = :provincia, municipio = :municipio where codigo = :codigo")
                query.bindValue(":codigo", int(modiCliente[0]))
                query.bindValue(":dni", str(modiCliente[1]))
                query.bindValue(":razon_social", str(modiCliente[2]))
                query.bindValue(":direccion", str(modiCliente[3]))
                query.bindValue(":telefono", str(modiCliente[4]))
                query.bindValue(":provincia", str(modiCliente[5]))
                query.bindValue(":municipio", str(modiCliente[6]))

                if query.exec():
                    eventos.Eventos.mostrarMensaje("Datos del cliente modificados")
                    DDBB.mostrarClientes()
                    eventos.Eventos.limpiarPanelClientes()
                else:
                    eventos.Eventos.mostrarMensaje(query.lastError().text())

        except Exception as error:
            print("error en modificar cliente", error)

    def cargarConductores(self=None):
        """

        """
        try:
            var.ui.cmbConductor.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, apellidos from conductores where baja is null order by codigo')
            if query.exec():
                var.ui.cmbConductor.addItem('')
                while query.next():
                    var.ui.cmbConductor.addItem(str(query.value(0)) + '. ' + query.value(1))
        except Exception as error:
            print("error en cargarConductor", error)

    def altafacturacion(registro):
        """

        """
        try:
            if not all(
                    [var.ui.txtCIFcliente.text(), var.ui.txtAltaFacturacion.text(),
                     var.ui.cmbConductor.currentText().split('. ')[0]]):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Faltan datos por introducir')
                msg.exec()
            else:
                dni = var.ui.txtCIFcliente.text()
                if DDBB.verificarClibaja(dni):
                    query = QtSql.QSqlQuery()
                    query.prepare('insert into facturas(dnicliente, fecha, conductor) values(:dni, :fecha, :driver)')
                    query.bindValue(":dni", str(registro[0]))
                    query.bindValue(":fecha", str(registro[1]))
                    query.bindValue(":driver", str(registro[2]))
                    if query.exec():
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle('Aviso')
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText('Factura grabada')
                        msg.exec()
                        DDBB.mostrarFacturas()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText('Error al grabar la factura')
                    msg.exec()
        except Exception as error:
            print(error, " cargar cond")

    def verificarClibaja(dni):
        """

        :return:
        :rtype:
        """
        try:
            query = QtSql.QSqlQuery()
            consulta = "SELECT COUNT(*) FROM clientes WHERE dni = :dni and baja is null"
            query.prepare(consulta)
            query.bindValue(':dni', dni)
            if query.exec():
                query.next()
                cantidad = query.value(0)
                return cantidad > 0
        except Exception as error:
            print("Error:", str(error))

    def comprobarCliente(self, dato):
        """

        :param dato:
        :type dato:
        :return:
        :rtype:
        """
        try:
            if self.existeCli(dato):
                query = QtSql.QSqlQuery()
                query.prepare('select * from clientes where dni = :dni and baja is not null')
                query.bindValue(':dni', str(dato))
                if query.exec():
                    if query.next():
                        return True
                    else:
                        return False
                else:
                    print('Error al ejecutar la consulta')
            else:
                print('El cliente no existe')
        except Exception as error:
            print("Error en comprobarCliente: " + str(error))


        except Exception as error:
            print("error en comprobarCliente " + error)

    def existeCli(self, dato):
        """

        :param dato:
        :type dato:
        :return:
        :rtype:
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select * from clientes where dni = :dni')
            query.bindValue(':dni', str(dato))
            if query.exec():
                if query.next():
                    return True
                else:
                    return False
                    print('devuelve false')
        except Exception as error:
            print("error en existeCli " + error)

    def datosViaje(self):
        """

        :return:
        :rtype:
        """
        try:
            tarifas = [0.20, 0.40, 0.80]
            datosviaje = [var.ui.cmbProvinciasVentas.currentText(), var.ui.cmbMunicipiosVentas.currentText(),
                          var.ui.cmbProvinciasVentas_2.currentText(), var.ui.cmbMunicipiosVentas_2.currentText()]
            if str(datosviaje[0]) == str(datosviaje[2]):
                if str(datosviaje[1]) == str(datosviaje[3]):
                    var.ui.rbtLocal.setChecked(True)
                    var.ui.rbtNacional.setChecked(False)
                    var.ui.rbtProvincial.setChecked(False)
                    datosviaje.append(str(tarifas[2]))
                    return datosviaje
                else:
                    var.ui.rbtProvincial.setChecked(True)
                    var.ui.rbtNacional.setChecked(False)
                    var.ui.rbtLocal.setChecked(False)
                    datosviaje.append(str(tarifas[1]))
                    return datosviaje
            else:
                var.ui.rbtNacional.setChecked(True)
                var.ui.rbtLocal.setChecked(False)
                var.ui.rbtProvincial.setChecked(False)
                datosviaje.append(str(tarifas[0]))
                return datosviaje
        except Exception as error:
            print('error en datos viaje ' + error)

    def cargarLineaViaje(registro):
        """

        """
        try:
            if any(not elemento.strip() for elemento in registro):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle(':(')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText('Faltan datos del viaje o numero factura')
                mbox.exec()
            else:
                query = QtSql.QSqlQuery()
                query.prepare('insert into viajes(factura, origen, destino, tarifa, km)'
                              'VALUES (:factura, :origen, :destino, :tarifa, :km)')
                query.bindValue(':factura', int(registro[5]))
                query.bindValue(':origen', str(registro[1]))
                query.bindValue(':destino', str(registro[3]))
                query.bindValue(':tarifa', str(registro[4]))
                query.bindValue(':km', str(registro[6]))
                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle(':-)')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText('Viaje grabado en la base de datos')
                    mbox.exec()
                    facturas.Facturas.cargarTablaViajes(self=None)
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle(':(')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText('Error al grabar el viaje en la base de datos')
                    mbox.exec()
        except Exception as error:
            print("error cargar linea viaje", error)

    def viajesFactura(dato):
        """

        :return:
        :rtype:
        """
        try:
            valores = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from viajes where factura = :dato")
            query.bindValue(':dato', int(dato))
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]  # funcion lambda
                    valores.append(row)
            return valores
        except Exception as error:
            print("ERROR CARGAR viaje a la vista", error)

    def getProvincia(dato):
        """

        :return:
        :rtype:
        """
        query = QtSql.QSqlQuery()
        query.prepare(
            'SELECT provincias.provincia from provincias join municipios On provincias.idprov = municipios where municipios.municipio = :dato')
        query.bindValue(':dato', str(dato))
        if query.exec():
            while query.next():
                municipio = [query.value(0)]
        return municipio

    @staticmethod
    def borrarviaje():
        """

        """
        try:

            mbox = QtWidgets.QMessageBox()
            mbox.setStyleSheet("QDialog{background-color: #84b6f4;} "
                               "QLabel {color: rgb(0, 0, 0);} ")
            mbox.setWindowTitle("Borrar")
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("¿Desea Borrar el viaje?")

            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

            resultado = mbox.exec()

            if resultado == QtWidgets.QMessageBox.StandardButton.Yes:
                row = var.ui.tabViajes.selectedItems()
                query = QtSql.QSqlQuery()
                query.prepare('delete from viajes where idViaje = :id')
                query.bindValue(':id', int(row[0].text()))
                if query.exec():
                    query.next()
                facturas.Facturas.cargarTablaViajes(self=None)
            elif resultado == QtWidgets.QMessageBox.StandardButton.No:
                mbox.close()
        except Exception as error:
            print('error al borrar viaje', error)
