"""
Problem One module: Solves a specific problem using MathService.

Example:
```python
from math_service import MathService

result = MathService().sum_of_multiples(1000)
print("Sum of multiples of 3 or 5 below 1000:", result)
"""
from services.math_service import MathService

math_service_instance = MathService()
result = math_service_instance.sum_of_multiples(1000)
print("Sum of multiples of 3 or 5 below 1000:", result)
