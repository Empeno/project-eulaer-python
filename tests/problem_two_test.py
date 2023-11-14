import pytest
from problem_two import main


@pytest.fixture
def mock_math_service():
    class MathServiceMock:
        def fibonacci_sum(self, limit):
            return 42

    return MathServiceMock()

def test_main_with_mock(mock_math_service, capsys):
    main(mock_math_service)
    captured = capsys.readouterr()
    assert "The sum of even-valued terms in the Fibonacci sequence below 4000000 is: 42" in captured.out
