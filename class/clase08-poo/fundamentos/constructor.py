class Car:
    """
    Representa vehiculos del mundo real
    """

    # Atributo de clase
    total_wheels = 4

    # Constructor (Se ejecuta al crear una instancia automáticamente y pide los parámetros make y color)
    def __init__(self, make, color):
        self.make = make
        self.color = color

    # Funcionalidad
    def star(self):
        print(f"El carro {self.make} arranco")


# Python ejecuta __init__ automáticamente y nos devuelve una instancia única de Car
car_tesla = Car("tesla", "negro")
car_toyota = Car("toyota", "blanco")

print(f"El carro 1 es un {car_tesla.make} de color {car_tesla.color}")
print(f"El número de ruedas es {car_tesla.total_wheels}")
car_tesla.star()

# Comprobando la instancia
print("=" * 50)
print(f"Carro tesla = {id(car_tesla)}")
print(f"Carro toyota = {id(car_toyota)}")
