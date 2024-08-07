import json
from cuenta_bancaria import CuentaBancaria, CuentaBancariaCorriente, CuentaBancariaAhorro

class GestionCuentas:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def obtener_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        return None

    def actualizar_cuenta(self, numero_cuenta, saldo=None, titular=None):
        cuenta = self.obtener_cuenta(numero_cuenta)
        if cuenta:
            if saldo is not None:
                cuenta.saldo = saldo
            if titular is not None:
                cuenta.titular = titular

    def eliminar_cuenta(self, numero_cuenta):
        cuenta = self.obtener_cuenta(numero_cuenta)
        if cuenta:
            self.cuentas.remove(cuenta)

    def listar_cuentas(self):
        for cuenta in self.cuentas:
            print(cuenta)

    def guardar_datos(self, filename):
        with open(filename, 'w') as file:
            json.dump([cuenta.__dict__ for cuenta in self.cuentas], file)

    def cargar_datos(self, filename):
        try:
            with open(filename, 'r') as file:
                cuentas_data = json.load(file)
                for cuenta_data in cuentas_data:
                    if 'descubierto_permitido' in cuenta_data:
                        cuenta = CuentaBancariaCorriente(**cuenta_data)
                    elif 'tasa_interes' in cuenta_data:
                        cuenta = CuentaBancariaAhorro(**cuenta_data)
                    else:
                        cuenta = CuentaBancaria(**cuenta_data)
                    self.cuentas.append(cuenta)
        except FileNotFoundError:
            print("Archivo no encontrado.")