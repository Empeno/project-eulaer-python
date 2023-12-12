def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
        i += 1
    if n > 1:
        return n
    return i

number = 600851475143
result = largest_prime_factor(number)
print("The largest prime factor of", number, "is:", result)
