"""
Problem One module: Solves a specific problem using MathService.

Example:
```python
from math_service import MathService

result = MathService().sum_of_multiples(1000)
print("Sum of multiples of 3 or 5 below 1000:", result)
"""
from services.math_service import MathService

def solve_problem_one(math_service):
    result = math_service.sum_of_multiples(1000)
    print("Sum of multiples of 3 or 5 below 1000:", result)

if __name__ == "__main__":
    # Create an instance of MathService and inject it into the solve_problem_one function
    math_service_instance = MathService()
    solve_problem_one(math_service_instance)