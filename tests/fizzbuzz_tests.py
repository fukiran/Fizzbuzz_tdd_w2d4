import unittest

from src.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_3_return_fizz(self):
        self.assertEqual("fizz",fizzbuzz(3))

    def test_fizzbuzz_6_return_fizz(self):
        self.assertEqual('fizz',fizzbuzz(6))

    
    def test_fizzbuzz_5_returns_buzz(self):
        self.assertEqual('buzz',fizzbuzz(5))

    def test_fizzbuzz_10_returns_buzz(self):
        self.assertEqual('buzz',fizzbuzz(10))

    def test_fizzbuzz_15_return_fizzbuzz(self):
        self.assertEqual('fizzbuzz',fizzbuzz(15))

    def test_fizzbuzz_45_return_fizzbuzz(self):
        self.assertEqual('fizzbuzz',fizzbuzz(45))

    def test_fizzbuzz_4_return_4str(self):
        self.assertEqual('4',fizzbuzz(4))