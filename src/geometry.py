import math

def circle_area(radius: float) -> float:
    """
    Calcula el área de un círculo dado su radio.
    Fórmula: π * radio^2
    """
    if radius < 0:
        raise ValueError("El radio no puede ser negativo.")
    return math.pi * (radius ** 2)

def rectangle_area(width: float, height: float) -> float:
    """
    Calcula el área de un rectángulo dado su ancho (width) y altura (height).
    """
    if width < 0 or height < 0:
        raise ValueError("El ancho y la altura no pueden ser negativos.")
    return width * height
