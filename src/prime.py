def is_prime(n: int) -> bool:
    """
    Determina si un número entero 'n' es primo.
    Un número primo es mayor que 1 y no tiene divisores
    más allá de 1 y de sí mismo.
    """
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
