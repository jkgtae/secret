#!/usr/bin/python

import unittest
from contextlib import contextmanager
import sys
from StringIO import StringIO
from secret import *


# mock the command line input from the user
@contextmanager
def mock_raw_input(mock):
    original_raw_input = __builtins__.raw_input
    __builtins__.raw_input = lambda _: mock
    yield
    __builtins__.raw_input = original_raw_input

# helper function to test error messages printed to std out
@contextmanager
def capture_std_out():
    original_out = sys.stdout
    sys.stdout = StringIO()
    yield sys.stdout
    sys.stdout = original_out


class IsSecretAdditiveTestCase(unittest.TestCase):

    def test_with_additive_secret(self):
        with mock_raw_input('20'):
            self.assertTrue(is_secret_additive(secret_additive))

    def test_with_non_additive_secret(self):
        with mock_raw_input('20'):
            self.assertFalse(is_secret_additive(secret_non_additive))

    def test_error_msg_for_non_numeric_input(self):
        with capture_std_out() as std_out:
            with mock_raw_input('foo'):
                is_secret_additive()
                output = std_out.getvalue().strip()
                self.assertEqual(output, 'You must input a number')

    def test_error_msg_for_negative_number(self):
        with capture_std_out() as std_out:
            with mock_raw_input(-10):
                is_secret_additive()
                output = std_out.getvalue().strip()
                self.assertEqual(output, 'Cannot determine if secret is additive; there are no primes less than -10')


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
