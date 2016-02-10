#!/usr/bin/python

from math import sqrt, ceil
from itertools import combinations


def secret_additive(n):
    """Example of an additive secret function"""
    return n


def secret_non_additive(n):
    """Example of a non-additive secret function"""
    return n**2


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


def is_secret_additive(secret=secret_additive):
    """
    Takes a number passed at the command line and determines if the secret() function is additive for all combinations x
    and y, where x and y are all prime numbers less than the number passed via the command-line argument.

    :param secret: a function that accepts a single integer parameter and returns an integer (this is an optional
                   parameter that facilitates testing both additive and non-additive versions of secret; if parameter is
                   not passed, it defaults to the additive version)
    :return: True if secret is additive; False if secret is not additive
    """

    user_input = raw_input('Please input a number: ')

    # check that input is a number
    try:
        n = float(user_input)
    except ValueError:
        print 'You must input a number\n'
    else:

        # convert n to an integer
        # int truncates toward zero, so we have to use ceil if we want to check the prime 5 for an input of 5.6
        n = int(ceil(n))

        # generate list of prime numbers less than n
        primes = generate_primes(n)

        # handle cases where there are too few primes less than n
        if not primes:
            print 'Cannot determine if secret is additive; there are no primes less than %s\n' % user_input
        elif len(primes) == 1:
            print 'Cannot determine if secret is additive; there is only one prime less than %s\n' % user_input
        else:

            # determine whether secret is additive for all combinations of primes less than n
            for x, y in combinations(primes, 2):
                print 'Checking primes %s and %s' % (x, y)
                if secret(x+y) != secret(x) + secret(y):
                    print 'Secret is not additive\n'
                    return False

            print 'Secret is additive\n'
            return True
