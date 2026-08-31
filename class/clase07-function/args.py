"""*args: Permite que una función acepte cualquier cantidad de argumentos posicionales,
Python lo va a empaquetar en una tupla
"""


def sum(*args):
    """Suma todos los argumentos posicionales recibidos

    args: tupla de argumentos posicionales

    return: la suma de todos los argumentos posicionales
    """
    result = 0
    for index in args:
        result += index
    return result


# Los *args van despues de los parámetros posicionales
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}")


print(sum(1, 2, 3, 4, 5))
greet("Hola", "Ana", "Luis", "Pedro")
