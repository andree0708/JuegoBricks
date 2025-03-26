

def is_palindrome(text: str) -> bool:
    """
    Verifica si 'text' es un palíndromo.
    Un palíndromo se lee igual de izquierda a derecha que de derecha a izquierda.
    """

    normalized_text = text.lower()
    return normalized_text == normalized_text[::-1]
