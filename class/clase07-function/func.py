"""Una función es un código reutilizable donde recibe parámetros y devuelve un resultado"""


def sum(a: int, b: int) -> int:
    """Calculates the sum of two numerical values.

    Args:
        a: The first numeric value.
        b: The second numeric value.

    Returns:
        The arithmetic sum of a and b.
    """
    return a + b


def multiply(a: int, b: int) -> int:
    """Calculates the product of two numerical values.

    Args:
        a: The first numeric value.
        b: The second numeric value.

    Returns:
        The arithmetic product of a and b.
    """
    return a * b


print(f"Suma: {sum(3, 5)}")
print(f"Multiplicación: {multiply(3, 5)}")
