from is_prime import *
import unittest
import pytest


class Prime_test_cases(unittest.TestCase):
    def test_is_five_prime(self):
        self.assertTrue(Prime_numbers.is_number_prime(5))


if __name__ == '__main__':
    unittest.main()
