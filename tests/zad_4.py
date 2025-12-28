import pytest

from logic import calculate_discount


def test_calculate_discount_1():
    assert calculate_discount(100, 0.2) == 80.0

def test_calculate_discount_2():
    assert calculate_discount(50, 0) == 50.0

def test_calculate_discount_3():
    assert calculate_discount(200, 1) == 0.0

def test_calculate_discount_4():
    with pytest.raises(ValueError):
        calculate_discount(100, -0.1)

def test_calculate_discount_5():
    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)
