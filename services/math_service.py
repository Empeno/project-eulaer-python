"""
MathService module: Provides mathematical services.

MathService class:
- sum_of_multiples(self, limit): Calculate sum of multiples of 3 or 5 below the limit.
"""
class MathService:
    """
    MathService class methods:
    - sum_of_multiples(self, limit): Calculate sum of multiples of 3 or 5 below the limit.
    """

    def sum_of_multiples(self, limit):
        """
        Calculate sum of multiples of 3 or 5 below the limit.

        Parameters:
        - limit (int): Upper limit for sum calculation.

        Returns:
        - int: Sum of multiples of 3 or 5 below the limit.
        """
        result = 0
        for i in range(limit):
            if i % 3 == 0 or i % 5 == 0:
                result += i
        return result

    def sum_of_multiples_custom(self, x, y, limit):
        """
        Calculate sum of multiples of x and y below the limit.

        Parameters:
        - x (int): First multiplier.
        - y (int): Second multiplier.
        - limit (int): Upper limit for sum calculation.

        Returns:
        - int: Sum of multiples of x and y below the limit.
        """
        result = 0
        for i in range(limit):
            if i % x == 0 or i % y == 0:
                result += i
        return result

    def fibonacci_sum(self, limit):
        # gets sum of even fibonaccis
        a, b = 1, 2
        even_sum = 0

        while a <= limit:
            if a % 2 == 0:
                even_sum += a
            #The following three lines are the same as: a, b = b, a + b
            new_a = b
            new_b = a + b
            a, b = new_a, new_b

        return even_sum
    