from abc import ABC, abstractmethod


class CuentaBancaria(ABC):  # Clase abstracta
    @abstractmethod
    def calcular_interes(self) -> float: ...  # Método abstracto


class CuentaAhorro(CuentaBancaria):
    def calcular_interes(self):  # Obligatorio implementarlo
        return 50


class CuentaCorriente(CuentaBancaria):
    def calcular_interes(self):  # Obligatorio implementarlo
        return 0


if __name__ == "__main__":
    cuenta_ahorro = CuentaAhorro()
    cuenta_corriente = CuentaCorriente()
    print(cuenta_ahorro.calcular_interes())
    print(cuenta_corriente.calcular_interes())
