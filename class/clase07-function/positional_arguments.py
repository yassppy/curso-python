"""Positional arguments: Son argumentos que se pasan a una función en el orden en que se declaran"""


def create_user(name, age, city):
    """Crea un usuario con el nombre, edad y ciudad especificados

    Args:
        name (str): Nombre del usuario
        age (int): Edad del usuario
        city (str): Ciudad del usuario

    Returns:
        str: Información del usuario
    """
    return f"Nombre: {name}, Edad: {age}, Ciudad: {city}"


print(f"El orden importa: {create_user('Juan', 30, 'Madrid')}")

print(f"Sin orden: {create_user(30, 'Madrid', 'Juan')}")
