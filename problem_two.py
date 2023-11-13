# my_script.py

from services.math_service import MathService

def main(math_service):
    # Set the limit to four million
    limit = 4000000
    result = math_service.fibonacci_sum(limit)
    print(f"The sum of even-valued terms in the Fibonacci sequence below {limit} is: {result}")

if __name__ == "__main__":
    # Create an instance of MathService and inject it into the main function
    math_service_instance = MathService()
    main(math_service_instance)
