from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self,nom,cel,tel):
        self.nombre = nom
        self.cedula = cel
        self.telefono = tel

    @abstractmethod
    def getCedula(self):
        return self.cedula

class ClientePersonal(Cliente):
    def __init__(self, nom, cel, tel):
        super().__init__(nom, cel, tel)

    @property
    def contrato(self):
        return self.__contrato
    @contrato.setter
    def contrato(self,value):
        if value:
            self.__contrato=value
        else:
            self.__contrato='Sin contrato'

    def getCedula(self):
        return super().getCedula()


class InterfaceSistemaPago(ABC):
    @abstractmethod
    def pago(self):
        pass

    @abstractmethod
    def saldo(self):
        pass

class PagoTarjeta(InterfaceSistemaPago):
    def pago(self):
        return 'Pago Tarjeta'

    def saldo(self):
        return 'Saldo Tarjeta'
class ImplementsPagoContrato(InterfaceSistemaPago):
    def pago(self):
        return 'Pago contrato'

    def saldo(self):
        return 'Saldo contrato'

class Vendedor:
    def __init__(self,nombre):
        self.nombre = nombre

    def modulopago(self,contrato):
        return contrato.pago()

pagoContrato = ImplementsPagoContrato()
# print(pagoContrato.pago())
vendedor1 = Vendedor('Josue')
print(vendedor1.modulopago(pagoContrato))