import unittest
from .fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_default(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(4), "4")

    def test_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_15(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
