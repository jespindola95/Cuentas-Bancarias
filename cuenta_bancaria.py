class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo, titular):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.titular = titular

    def __str__(self):
        return f"CuentaBancaria(numero_cuenta={self.numero_cuenta}, saldo={self.saldo}, titular={self.titular})"

class CuentaBancariaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, titular, descubierto_permitido):
        super().__init__(numero_cuenta, saldo, titular)
        self.descubierto_permitido = descubierto_permitido

    def __str__(self):
        return (f"CuentaBancariaCorriente(numero_cuenta={self.numero_cuenta}, saldo={self.saldo}, "
                f"titular={self.titular}, descubierto_permitido={self.descubierto_permitido})")

class CuentaBancariaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, titular, tasa_interes):
        super().__init__(numero_cuenta, saldo, titular)
        self.tasa_interes = tasa_interes

    def __str__(self):
        return (f"CuentaBancariaAhorro(numero_cuenta={self.numero_cuenta}, saldo={self.saldo}, "
                f"titular={self.titular}, tasa_interes={self.tasa_interes})")
        