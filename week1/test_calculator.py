import pytest
from calculator import add, subtract, multiply, divide, power, is_even


# ─── ARITHMETIC TESTS ───

@pytest.mark.arithmetic
def test_add_two_positive_integers():
    assert add(2, 3) == 5


@pytest.mark.arithmetic
def test_add_positive_and_negative():
    assert add(10, -3) == 7


@pytest.mark.arithmetic
def test_add_two_floats():
    assert add(1.5, 2.5) == 4.0


@pytest.mark.arithmetic
def test_add_zero():
    assert add(7, 0) == 7


@pytest.mark.arithmetic
def test_subtract_positive_result():
    assert subtract(10, 4) == 6


@pytest.mark.arithmetic
def test_subtract_negative_result():
    assert subtract(3, 10) == -7


@pytest.mark.arithmetic
def test_multiply_two_integers():
    assert multiply(4, 5) == 20


@pytest.mark.arithmetic
def test_multiply_by_zero():
    assert multiply(99, 0) == 0


@pytest.mark.arithmetic
def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6


# ─── EDGE CASE TESTS ───

@pytest.mark.edge_case
def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        divide(10, 0)