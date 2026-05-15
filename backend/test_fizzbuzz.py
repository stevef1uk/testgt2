import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_multiples_of_3(self):
        for i in range(3, 101, 3):
            if i % 5 != 0:
                self.assertEqual(fizzbuzz(i), "Fizz")
    def test_multiples_of_5(self):
        for i in range(5, 101, 5):
            if i % 3 != 0:
                self.assertEqual(fizzbuzz(i), "Buzz")
    def test_multiples_of_15(self):
        for i in range(15, 101, 15):
            self.assertEqual(fizzbuzz(i), "FizzBuzz")
    def test_others(self):
        for i in range(1, 101):
            if i % 3 != 0 and i % 5 != 0:
                self.assertEqual(fizzbuzz(i), "")

if __name__ == "__main__":
    unittest.main()
