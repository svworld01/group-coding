# created by KUMAR SHANU

# 3. Count Primes
# https://leetcode.com/problems/count-primes

# The Sieve of Eratosthenes Solution


class Solution:
    def countPrimes(self, n: int) -> int:
        # create boolean array of n size
        isPrime = [True] * n

        # straing from 2 mark all numbers as non prime
        # which are divisible by current number
        i = 2
        while i * i < n:
            if isPrime[i]:

                # starting from i*i because less than that all numbers are
                # already marked
                j = i * i
                while j < n:
                    isPrime[j] = False
                    j += i
            i += 1

        # now count all prime numbers
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count
