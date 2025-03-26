
import pytest
from src.palindrome import is_palindrome

def test_palindrome_lowercase():
    assert is_palindrome("radar") is True
    assert is_palindrome("level") is True
    assert is_palindrome("test") is False

def test_palindrome_mixed_case():
    assert is_palindrome("Racecar") is True  
    assert is_palindrome("Madam") is True

def test_palindrome_empty_string():
    assert is_palindrome("") is True  
