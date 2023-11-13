"""
Test module for MathService: Tests the sum_of_multiples method.
"""

from math_service import MathService

def test_sum_of_multiples():
    """
    Test the sum_of_multiples method of MathService.

    Test cases:
    1. limit is 10, expected result is 23.
    2. limit is 1000, expected result is 233168.
    """
    math_service_instance = MathService()

    # Test case 1: limit is 10
    result = math_service_instance.sum_of_multiples(10)
    assert result == 23

    # Test case 2: limit is 1000
    result = math_service_instance.sum_of_multiples(1000)
    assert result == 233168
