import math

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            for i in range(5, int(math.sqrt(n)) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True

        primes = 0
        for i in range(1, n + 1):
            if isPrime(i):
                primes += 1

        return math.factorial(primes) * math.factorial(n - primes) % (10 ** 9 + 7)