import unittest

from src.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_3_return_fizz(self):
        self.assertEqual("fizz",fizzbuzz(3))