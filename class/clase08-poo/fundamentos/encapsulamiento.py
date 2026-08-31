class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular  # Público: cualquiera puede leerlo
        self._historial = []  # Protegido
        self.__saldo = saldo  # Privado: acceso controlado

    @property  # Para leer el valor
    def saldo(self):
        return f"Titular: {self.titular}, Saldo: {self.__saldo}"

    @saldo.setter  # Para modificar el valor
    def saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            raise ValueError("El saldo no puede ser negativo")


# Si este archivo es el programa principal ejecuta esto __main__
if __name__ == "__main__":
    cuenta = Cuenta("Juan", 1000)
    # Leyendo el saldo
    print(cuenta.saldo)

    # Modificando el saldo
    cuenta.saldo = 200
    # cuenta.saldo = -200
