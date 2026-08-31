"""Default values: Se establece un parametro por defecto si no se proporciona un valor en el argumento
volviendolo opcional"""


def greet(first_name: str | None = "World"):
    print(f"Hello, {first_name}!")


greet()
greet("Juan")
