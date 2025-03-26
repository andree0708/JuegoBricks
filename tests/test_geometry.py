# tests/test_geometry.py

import pytest
import math
from src.geometry import circle_area, rectangle_area

def test_circle_area():
    assert math.isclose(circle_area(1), math.pi, rel_tol=1e-9)
    assert math.isclose(circle_area(0), 0, rel_tol=1e-9)

    # Verificamos que lance un ValueError para valores negativos
    with pytest.raises(ValueError):
        circle_area(-1)

def test_rectangle_area():
    assert rectangle_area(2, 3) == 6
    assert rectangle_area(0, 5) == 0

    # Verificamos que lance un ValueError para valores negativos
    with pytest.raises(ValueError):
        rectangle_area(-2, 3)
