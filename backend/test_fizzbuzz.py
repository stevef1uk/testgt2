from .fizzbuzz import fizzbuzz
import unittest
class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        # Test typical cases
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        # Test edge cases
        self.assertEqual(fizzbuzz(0), "FizzBuzz") # 0 is divisible by any number
        self.assertEqual(fizzbuzz(-3), "Fizz")
        self.assertEqual(fizzbuzz(-5), "Buzz")
        self.assertEqual(fizzbuzz(-15), "FizzBuzz")
if __name__ == '__main__':
    unittest.main()
