import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
    def test_default(self):
        self.assertEqual(fizzbuzz(1), "1")

if __name__ == "__main__":
    unittest.main()
