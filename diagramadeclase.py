from datetime import date


class Empresa:
    def __init__(self, nom='MORTADELA', ruc='0000000', tel='000000', dir=''):
        self.nombre = nom
        self.ruc = ruc
        self.tel = tel
        self.dir = dir

    def mostrarEmpresa(self):
        print('Empresa: {:17} Ruc:{}'.format(self.nombre, self.ruc))


class Cliente:
    def __init__(self, nom, ced, tel):
        self.nombre = nom
        self.cedula = ced
        self.telefono = tel

    def mostrarCliente(self):
        print(self.nombre, self.cedula, self.telefono)


class ClienteCorporativo(Cliente):
    def __init__(self, nom, ced, tel, contrato):
        super().__init__(nom, ced, tel)
        self.__contrato = contrato

    @property
    def contrato(self):
        return self.__contrato

    @contrato.setter
    def contrato(self, value):
        if value:
            self.__contrato = value
        else:
            self.__contrato = 'Sin contrato'

    def mostrarCliente(self):
        print(self.nombre, self.__contrato)


class ClientePersonal(Cliente):
    def __init__(self, nom, ced, tel, promocion=True):
        super().__init__(nom, ced, tel)
        self.__promocion = promocion

    @property
    def promocion(self):
        if self.__promocion == True:
            return '10% descuento'
        else:
            return 'No hay promocion'

    def mostrarCliente(self):
        print(self.nombre, self.promocion)


class Articulo:
    secuencia = 0
    iva = 0.12

    def __init__(self, des, pre, sto):
        Articulo.secuencia += 1
        self.codigo = Articulo.secuencia
        self.descripcion = des
        self.precio = pre
        self.stock = sto

    def mostrararticulo(self):
        print(self.codigo, self.descripcion)


class DetVenta:
    linea = 0

    def __init__(self, articulo, cantidad):
        DetVenta.linea += 1
        self.lineadetalle = DetVenta.linea
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = articulo.precio


class CabVenta:
    def __init__(self, fac, fecha, cliente, tot=0):
        self.factura = fac
        self.fecha = fecha
        self.cliente = cliente
        self.total = tot
        self.detalleVen = []

    def agregardetalle(self, articulo, cantidad):
        detalle = DetVenta(articulo, cantidad)
        self.total += detalle.precio * detalle.cantidad
        self.detalleVen.append(detalle)

    def mostrarventa(self, empNombre, empRuc):
        print('Empresa: {:15} Ruc:{}'.format(empNombre, empRuc))
        print('Factura#: {:15}Fecha:{}'.format(self.factura, self.fecha))
        self.cliente.mostrarCliente()
        print('Linea Articulo      Precio Cantidad Subtotal')
        for det in self.detalleVen:
            print('{:5} {:15} {} {:6} {:7}'.format(det.linea, det.articulo.descripcion, det.precio, det.cantidad,
                                                   det.precio * det.cantidad))
        print('total venta : {:25}'.format(self.total))


empresa = Empresa()
cli1 = ClientePersonal('Erick', 1250277215, 00000, False)
art1 = Articulo('Aceite', 2, 100)
art2 = Articulo('Coca Cola', 3, 100)
today = date.today()
venta = CabVenta('F0001', today, cli1)
venta.agregardetalle(art1, 3)
venta.agregardetalle(art2, 2)
venta.mostrarventa(empresa.nombre, empresa.ruc)