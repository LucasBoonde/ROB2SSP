from math import sqrt
import pytest

def hypotenuse(width, height):
    return sqrt(width**2 + height**2)

def test_hypotenuse():
    assert hypotenuse(0, 0) == 0
    assert hypotenuse(3, 4) == 5
    assert hypotenuse(-3, -4) == 5
    assert hypotenuse (1, 1) == pytest.approx(1.4142, 0.001)
    
    