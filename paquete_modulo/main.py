import re

import paquete
import paquete_sin_init
import validador_email
from funcion_directa.despedida import (
    despedir,  # Importa la función desde el módulo (ruta explícita)
)
from paquete import (
    saludar,  # Acceso directo a la función expuesta por el __init__.py del paquete
)
from paquete_sin_init import (  # Importa los módulos completos para acceder a sus funciones (calculadora.sumar)
    calculadora,
)

print("=" * 30, "modulo")
print("Suma:", calculadora.sumar(10, 20))
print("¿Email válido?:", validador_email.es_valido("correo@ejemplo.com"))

print("=" * 30, "paquete")
saludar()

print("=" * 30, "funcion_directa")
despedir()


# Imprimimos la ruta del archivo de cada uno
print("1. 'Paquete sin __init__' es:", paquete_sin_init.__file__)
print("2. 'paquete' es:", paquete.__file__)
print("3. 're' es:", re.__file__)
print("4. 'modulo' es:", validador_email.__file__)
