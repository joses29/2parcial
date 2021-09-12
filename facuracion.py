from _typeshed import Self
from datetime import date

class Empresa:
    def __init__(self, nom="El mas Barato", ruc="0999999999", telf="042971234", dir="Milagro"):
        self.nombre= nom
        self.ruc= ruc
        self.telefono= telf
        self.direccion= dir
    
    def Mostrar_Empresa(self):
        print("Empresa: {:17} Ruc:{}".format(self.nombre,self.ruc))

from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self, nom, ced, telf):
        self.nombre= nom
        self.cedula= ced
        self.telefono= telf
    
    def mostrarCliente(self):
        print(self.nombre,self.cedula,self.telefono)
    
class Cliente_Corporativo(Cliente):
    def __init__(self, nom, ced, telf,contrato):
        super().__init__(self, nom, ced, telf)
        self._contrato= contrato

    @property
    def contrato(self): #getter: obtener el valor del atributo privado
        return self._contrato
    @contrato.setter
    def contrato(self,value): #setter: asigna un valor al atributo privado
        if value:
            self._contrato= value
        else:
            self._contrato= "Sin contrato"
    
    def mostrarCliente(self):
        print(self.nombre,self._contrato)

class ClientePersonal(Self):
    def __init__(self, nom, ced, telf, promocion=True):
        super().__init__(nom, ced, telf)
        self._promocion= promocion

    @property
    def promocion(self): #getter: obtener el valor del atributo
        return self._promocion
    @promocion.setter
    def promocion(self,value): #getter: obtener el valor de
        self._promocion= value

    def mostrarCliente(self):
        print(self.nombre,self.promocion)

class Articulo:
    secuencia= 0
    iva = 0.12
    def __init__(self,des,pre,sto):
        Articulo.secuencia += 1
        self.codigo= Articulo.secuencia
        self.descripcion= des
        self.precio= pre
        self.stock= sto
    def mostrarArticulo(self):
        print(self.codigo, self.descripcion)

class DetVenta:
    linea= 0
    def __init__(self, articulo, cantidad):
        DetVenta.linea += 1
        self.lineaDetalle= DetVenta.linea
        self.articulo= articulo
        self.precio= articulo.precio
        self.cantidad= cantidad

class CabVenta:
    def __init__(self,fac,empresa,fecha, cliente,tot=0):
        self.empresa= empresa
        self.factura= fac
        self.fecha= fecha
        self.cliente= cliente
        self.total= tot
        self.detalleVen= []

    def agregarDetalle(self, articulo, cantidad):
        detalle = DetVenta(articulo,cantidad)
        self.total += detalle.precio * detalle.cantidad
        self.detalleVen.append(detalle)
    
    def mostrarVenta(self,empNombre,empRuc):
        print("Empresa: {:17}Ruc:{}".format(empNombre,empRuc))
        print("Factura#: {:13}Fecha: {}".format(self.factura,self.cliente.mostrarCliente()))
        print("Linea Articulo , Precio Cantidad Subtotal")
        for det in self.detalleVen:
            print("{:5} {:15} {} {:6} {:7}".format(det.linea,))
        print("Total Venta:{:26}".format(self.total))

empresa= Empresa()
cli1 = ClientePersonal("Daniel","0992214888","099214847",False)
print(cli1.getCedula())
art1=Articulo("Aceite",3,100)
art2= Articulo("Coca Cola",1,200)
today= date.today()
fecha= date(2021,8,15)
venta= CabVenta('F0001',date.today(),cli1)
venta.agregarDetalle(art1,3)
venta.agregarDetalle(art1,2)
venta.mostrarVenta(empresa.nombre,empresa.ruc)

class InterfaceSistemaPago(ABC):
    @abstractmethod
    def pago(self):
        