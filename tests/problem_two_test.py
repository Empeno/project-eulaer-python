from problem_two import main
from services.math_service import MathService
import pytest

@pytest.fixture
def math_service_mock():
    class MathServiceMock:
        def fibonacci_sum(self, limit):
            return 42

    return MathServiceMock()

def test_main_with_mock(math_service_mock, capsys):
    main(math_service_mock)
    captured = capsys.readouterr()
    assert "The sum of even-valued terms in the Fibonacci sequence below 4000000 is: 42" in captured.out

# Add more test cases as needed
