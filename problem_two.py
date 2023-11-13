from services.math_service import MathService

# Set the limit to four million
limit = 4000000
math_service_instance = MathService()
result = math_service_instance.fibonacci_sum(limit)
print(f"The sum of even-valued terms in the Fibonacci sequence below {limit} is: {result}")
