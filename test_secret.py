#!/usr/bin/python

import unittest
from secret import *


class IsSecretAdditiveTestCase(unittest.TestCase):

    def test_with_additive_secret(self):
        self.assertTrue(is_secret_additive(20, secret_additive))


class GeneratePrimesTestCase(unittest.TestCase):

    def test_raise_type_error_for_non_integer(self):
        self.assertRaises(TypeError, generate_primes, 'foo')
        self.assertRaises(TypeError, generate_primes, 10.0)

    def test_return_empty_list_for_input_under_2(self):
        self.assertEqual(generate_primes(2), [])
        self.assertEqual(generate_primes(-10), [])

    def test_generate_primes_under_200(self):
        primes_under_200 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                            97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                            191, 193, 197, 199]
        self.assertEqual(generate_primes(200), primes_under_200)


if __name__ == '__main__':
    unittest.main()
