import pytest

from problem_one import solve_problem_one
from services.math_service import MathService



@pytest.fixture(Name = 'Math Service')
def math_service_instance():
    return MathService()


@pytest.fixture(Name = 'Mocked Math Service')
def math_service_mock():
    class MathServiceMock:
        def sum_of_multiples(self, limit):
            if limit is None:
                return None
            return 42

    return MathServiceMock()

def test_solve_problem_one_with_real_math_service(math_service_instance, capsys):
    solve_problem_one(math_service_instance)
    captured = capsys.readouterr()
    assert "Sum of multiples of 3 or 5 below 1000:" in captured.out

def test_solve_problem_one_with_mocked_math_service(math_service_mock, capsys):
    solve_problem_one(math_service_mock)
    captured = capsys.readouterr()
    assert "Sum of multiples of 3 or 5 below 1000: 42" in captured.out
