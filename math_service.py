class MathService:

    def sum_of_multiples(self, limit):
        result = 0
        for i in range(limit):
            if i % 3 == 0 or i % 5 == 0:
                result += i
        return result