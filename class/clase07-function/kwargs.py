"""**kwargs: Permite que una función acepte cualquier cantidad de argumentos clave-valor,
Python lo empaqueta en un diccionario."""


def kwargs_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# orden correcto cuando se combinan orden es siempre: parámetros normales → *args → **kwargs.
def example(a, *args, **kwargs):
    return a, args, kwargs


kwargs_function(name="Ana", age=30)
# internamente python crea un diccionario con los argumentos kwargs = {'name': 'Ana', 'age': 30}
