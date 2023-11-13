"""
Tests for the fibonacci_sum function in math_service module.
"""

from services.math_service import MathService

def test_fibonacci_sum_with_limit_10():
    """
    Test the fibonacci_sum function with a limit of 10.
    """
    math_service_instance = MathService()
    result = math_service_instance.fibonacci_sum(10)
    assert result == 10  # 2 + 8 = 10

def test_fibonacci_sum_with_limit_20():
    """
    Test the fibonacci_sum function with a limit of 20.
    """
    math_service_instance = MathService()
    result = math_service_instance.fibonacci_sum(20)
    assert result == 10  # 2 + 8 = 10

def test_fibonacci_sum_with_limit_50():
    """
    Test the fibonacci_sum function with a limit of 50.
    """
    math_service_instance = MathService()
    result = math_service_instance.fibonacci_sum(50)
    assert result == 44  # 2 + 8 + 34 = 44

def test_fibonacci_sum_with_limit_100():
    """
    Test the fibonacci_sum function with a limit of 100.
    """
    math_service_instance = MathService()
    result = math_service_instance.fibonacci_sum(100)
    assert result == 44  # 2 + 8 + 34 = 44

def test_fibonacci_sum_with_limit_4000000():
    """
    Test the fibonacci_sum function with a limit of 4000000.
    """
    math_service_instance = MathService()
    result = math_service_instance.fibonacci_sum(4000000)
    assert result == 4613732  # The actual sum
