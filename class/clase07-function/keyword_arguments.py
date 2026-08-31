"""Keyword arguments: Son argumentos que pasas utilizando el nombre del parámetro explícitamente,
el orden no importa ya que Python sabe qué valor corresponde a cada parámetro"""


def create_user(name: str, age: int, city: str) -> str:
    """Crea un usuario con el nombre, edad y ciudad especificados

    Args:
        name (str): Nombre del usuario
        age (int): Edad del usuario
        city (str): Ciudad del usuario

    Returns:
        str: Información del usuario
    """
    return f"Nombre: {name}, Edad: {age}, Ciudad: {city}"


user = create_user(name="Juan", age=30, city="Madrid")
print(user)

# Puedes mezclarlo pero los posicional van primero
user2 = create_user("Pedro", 25, city="Barcelona")
print(user2)
