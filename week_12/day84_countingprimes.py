"""
This question is asked by Google. Given a positive integer N, return the number of prime numbers less than N.

Ex: Given the following N…

N = 3, return 1.
2 is the only prime number less than 3.
Ex: Given the following N…

N = 7, return 3.
2, 3, and 5 are the only prime numbers less than 7.
"""
# https://www.geeksforgeeks.org/how-is-the-time-complexity-of-sieve-of-eratosthenes-is-nloglogn/
# Time O(n * log(log n))
# Space O(n)
def countprimes(n):
    if n <= 2:
        return 0
    primes = [True] * (n)
    primes[0] = False
    primes[1] = False

    for i in range(2,int(n ** 0.5) + 1):
        if not primes[i]:
            continue

        for j in range(i+i,n, i):
            if primes[j]:
                primes[j] = False

    return sum(primes)

print(countprimes(1))