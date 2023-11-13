import pytest
from services.math_service import fibonacci_sum

def test_fibonacci_sum_with_limit_10():
    result = fibonacci_sum(10)
    assert result == 10  # 2 + 8 = 10

def test_fibonacci_sum_with_limit_20():
    result = fibonacci_sum(20)
    assert result == 10  # 2 + 8 = 10

def test_fibonacci_sum_with_limit_50():
    result = fibonacci_sum(50)
    assert result == 44  # 2 + 8 + 34 = 44

def test_fibonacci_sum_with_limit_100():
    result = fibonacci_sum(100)
    assert result == 44  # 2 + 8 + 34 = 44

def test_fibonacci_sum_with_limit_4000000():
    result = fibonacci_sum(4000000)
    assert result == 4613732  # The actual sum
