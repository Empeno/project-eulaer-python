class MathService:
    """
    A class that provides mathematical services.

    Methods:
    - sum_of_multiples(self, limit): Calculates the sum of multiples of 3 or 5
      below the specified limit.
    """

    def sum_of_multiples(self, limit):
        """
        Calculate the sum of multiples of 3 or 5 below the specified limit.

        Parameters:
        - limit (int): The upper limit for calculating the sum of multiples.

        Returns:
        - int: The sum of multiples of 3 or 5 below the specified limit.
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