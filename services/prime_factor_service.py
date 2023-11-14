class PrimeFactorService:

    def largest_prime_factor(self, n):
        if n <= 1:
            return None
        i = 2
        while i * i <= n:
            while n % i == 0:
                n //= i
            i += 1
        return n if n > 1 else i - 1
    
    def is_prime(self, number):
        if number <= 1:
            return False
        if number <= 3:
            return True
        
        # Check divisibility by 2 or 3
        if number % 2 == 0 or number % 3 == 0:
            return False
        
        # Check divisibility by numbers of the form 6k ± 1 up to sqrt(number)
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        
        return True
    