from gestion_cuentas import GestionCuentas
from cuenta_bancaria import CuentaBancariaCorriente, CuentaBancariaAhorro

def main():
    gestion_cuentas = GestionCuentas()

    while True:
        print("\n1. Agregar cuenta")
        print("2. Listar cuentas")
        print("3. Actualizar cuenta")
        print("4. Eliminar cuenta")
        print("5. Guardar datos")
        print("6. Cargar datos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                tipo = input("Tipo de cuenta (corriente/ahorro): ")
                numero_cuenta = input("Número de cuenta: ")
                saldo = float(input("Saldo: "))
                titular = input("Titular: ")

                if tipo == 'corriente':
                    descubierto_permitido = float(input("Descubierto permitido: "))
                    cuenta = CuentaBancariaCorriente(numero_cuenta, saldo, titular, descubierto_permitido)
                elif tipo == 'ahorro':
                    tasa_interes = float(input("Tasa de interés: "))
                    cuenta = CuentaBancariaAhorro(numero_cuenta, saldo, titular, tasa_interes)
                else:
                    print("Tipo de cuenta no válido.")
                    continue

                gestion_cuentas.agregar_cuenta(cuenta)

            elif opcion == '2':
                gestion_cuentas.listar_cuentas()

            elif opcion == '3':
                numero_cuenta = input("Número de cuenta a actualizar: ")
                saldo = input("Nuevo saldo (presione enter para dejar igual): ")
                titular = input("Nuevo titular (presione enter para dejar igual): ")

                gestion_cuentas.actualizar_cuenta(
                    numero_cuenta,
                    saldo=float(saldo) if saldo else None,
                    titular=titular if titular else None
                )

            elif opcion == '4':
                numero_cuenta = input("Número de cuenta a eliminar: ")
                gestion_cuentas.eliminar_cuenta(numero_cuenta)

            elif opcion == '5':
                filename = input("Nombre del archivo para guardar: ")
                gestion_cuentas.guardar_datos(filename)

            elif opcion == '6':
                filename = input("Nombre del archivo para cargar: ")
                gestion_cuentas.cargar_datos(filename)

            elif opcion == '7':
                break

            else:
                print("Opción no válida. Por favor, intente de nuevo.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()