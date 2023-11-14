class PrimeFactorService:

    def largest_prime_factor(self, n):
        if n < 1:
            return None
        i = 2
        while i * i <= n:
            while n % i == 0:
                n //= i
            i += 1
        return n if n > 1 else i - 1

    def is_prime(self, number):
        # Handling base cases
        if number <= 1:
            return False
        if number <= 3:
            return True

        # Optimized checking for divisibility by 2 and 3
        if number % 2 == 0 or number % 3 == 0:
            return False

        # Checking divisibility by numbers of the form 6k ± 1 up to sqrt(number)
        divisor = 5
        while divisor * divisor <= number:
            if number % divisor == 0 or number % (divisor + 2) == 0:
                return False
            divisor += 6

        return True
