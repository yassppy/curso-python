# Early return: Salida anticipada antes de que la función termine su ejecución
def validate_age(age):
    if age < 0:
        return "Edad invalida"
    if age < 18:
        return "Menor de edad"
    return "Mayor de edad"


def es_par(numero):
    return numero % 2 == 0  # Boolean


def obtener_numeros():
    return [1, 2, 3, 4]  # lista


def obtener_usuario():
    return {"nombre": "Ana"}  # diccionario


def coordenadas():
    return (10, 20)  # tupla


print(validate_age(17))
print(validate_age(-6))
