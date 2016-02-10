#!/usr/bin/python

from math import sqrt


def secret_additive(n):
    """Example of an additive secret function"""
    return n


def generate_primes(n):
    """
    Return a list of all primes less than n.

    Uses the Sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) algorithm to generate the list
    of primes. If we happen to know this function will be used to generate large primes, another algorithm (such as a
    wheel sieve) would probably be more suitable.

    :param n: an integer
    :return: list of all primes less than n
    :raises TypeError: if n is not an integer
    """

    # check for invalid input
    if type(n) is not int:
        raise TypeError('n must be an integer')

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
