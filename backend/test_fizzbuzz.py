import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        # test fizzbuzz function
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(4), "4")
