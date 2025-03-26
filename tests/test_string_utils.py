# tests/test_string_utils.py

import pytest
from src.string_utils import count_vowels, remove_spaces

def test_count_vowels():
    assert count_vowels("Hello") == 2  # 'e' y 'o'
    assert count_vowels("XYZ") == 0
    assert count_vowels("AEIOU") == 5
    assert count_vowels("") == 0

def test_remove_spaces():
    assert remove_spaces("Hello World") == "HelloWorld"
    assert remove_spaces("  Leading and trailing  ") == "Leadingandtrailing"
    assert remove_spaces("") == ""
