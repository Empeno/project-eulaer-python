from math_service import MathService

math_service_instance = MathService()

limit = 1000
result = math_service_instance.sum_of_multiples(limit)
print("The sum of multiples of 3 or 5 below 1000 is:", result)
