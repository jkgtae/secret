#!/usr/bin/python

from math import sqrt


def generate_primes(n):

    # there are no primes less than 2
    if n <= 2:
        return []

    # start by assuming all numbers are prime
    sieve = [True] * n

    # mark multiples of prime numbers as NOT prime (i = prime number, j = multiple of a prime number)
    limit = int(sqrt(n)) + 1
    for i in range(2, limit):  # only need to mark multiples for primes up to sqrt(n)
        if sieve[i] is True:
            for j in range(i**2, n, i):  # start marking multiples at i^2, because lower multiples are already marked
                sieve[j] = False

    # remaining numbers are prime
    return [k for k in range(2, len(sieve)) if sieve[k] is True]
