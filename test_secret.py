#!/usr/bin/python

import unittest


class GeneratePrimesTestCase(unittest.TestCase):

    def test_return_empty_list_for_input_under_2(self):
        self.assertEqual(generate_primes(2), [])
        self.assertEqual(generate_primes(-10), [])


if __name__ == '__main__':
    unittest.main()
