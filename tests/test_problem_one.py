# test_problem_one.py

from problem_one import solve_problem_one
from services.math_service import MathService
import pytest

# Fixture to create an instance of MathService
@pytest.fixture
def math_service_instance():
    return MathService()

# Fixture to create a mock instance of MathService for testing
@pytest.fixture
def math_service_mock():
    class MathServiceMock:
        def sum_of_multiples(self, limit):
            # Mocked implementation for testing
            return 42

    return MathServiceMock()

# Test the solve_problem_one function with a real MathService instance
def test_solve_problem_one_with_real_math_service(math_service_instance, capsys):
    solve_problem_one(math_service_instance)
    captured = capsys.readouterr()
    assert "Sum of multiples of 3 or 5 below 1000:" in captured.out

# Test the solve_problem_one function with a mocked MathService instance
def test_solve_problem_one_with_mocked_math_service(math_service_mock, capsys):
    solve_problem_one(math_service_mock)
    captured = capsys.readouterr()
    assert "Sum of multiples of 3 or 5 below 1000: 42" in captured.out
