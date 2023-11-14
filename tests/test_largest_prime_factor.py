"""
Test module for MathService: Tests the largest_prime_factor method.
"""




from services.prime_factor_service import PrimeFactorService


def test_prime_factor_of_13195():
    # Test with a known value (prime factors of 13195 are 5, 7, 13, and 29)
    prime_factor_service_instance = PrimeFactorService()

    result = prime_factor_service_instance.largest_prime_factor(13195)

    assert result == 29

def test_prime_factor_of_600851475143():
    # Test with the given large number
    prime_factor_service_instance = PrimeFactorService()
    assert prime_factor_service_instance.largest_prime_factor(600851475143) == 6857

def test_prime_factor_of_2():
    # Test with the smallest prime number
    prime_factor_service_instance = PrimeFactorService()
    assert prime_factor_service_instance.largest_prime_factor(2) == 2

def test_prime_factor_of_one():
    # Test for the number 1
    prime_factor_service_instance = PrimeFactorService()
    result = prime_factor_service_instance.largest_prime_factor(1)
    assert result == 1, "The largest prime factor of 1 should be 1"

def test_prime_factor_of_negative_number():
    # Test for a negative number
    prime_factor_service_instance = PrimeFactorService()
    result = prime_factor_service_instance.largest_prime_factor(-20)
    assert result is None, "The function should return None for negative numbers"
    