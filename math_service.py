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
