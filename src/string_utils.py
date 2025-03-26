# src/string_utils.py

def count_vowels(text: str) -> int:
    """
    Cuenta cuántas vocales (a, e, i, o, u) hay en 'text'.
    Ignora mayúsculas y minúsculas.
    """
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

def remove_spaces(text: str) -> str:
    """
    Elimina todos los espacios de la cadena 'text'.
    """
    return text.replace(" ", "")
