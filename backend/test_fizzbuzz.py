import unittest
from backend.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_multiples_of_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
    def test_multiples_of_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
    def test_multiples_of_15(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
    def test_others(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(4), "4")

if __name__ == "__main__":
    unittest.main()
