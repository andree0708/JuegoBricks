import pytest
from src.prime import is_prime

def test_prime_basic_cases():
    assert is_prime(2) is True   
    assert is_prime(3) is True
    assert is_prime(4) is False  

def test_prime_larger_numbers():
    assert is_prime(17) is True
    assert is_prime(18) is False
    assert is_prime(19) is True

def test_prime_negative_and_zero():
    assert is_prime(0) is False
    assert is_prime(-1) is False
    assert is_prime(-10) is False
