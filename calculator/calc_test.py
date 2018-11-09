import pytest
import calc


def test_add():
    assert calc.add(4, 5) == 9
    assert calc.add(5, 2) == 7
    assert calc.add(-5, 3) == -2
    assert calc.add(-2, -3) == -5


def test_subtract():
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(-5, 3) == -8
    assert calc.subtract(-2, -3) == 1


def test_multiply():
    assert calc.multiply(5, 2) == 10
    assert calc.multiply(-5, 3) == -15
    assert calc.multiply(-2, -3) == 6


def test_divide():
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(-5, 2) == -2.5
    assert calc.divide(-15, -3) == 5


if __name__ == '__main__':
    pytest.main()