# Implementation plan
The plan is to implement the FizzBuzz library in pure Python stdlib, with no third-party dependencies.
The library must expose a function fizzbuzz(n: int) -> str that follows the canonical rules:
- return "FizzBuzz" for numbers divisible by 15
- return "Fizz" for numbers divisible by 3 only
- return "Buzz" for numbers divisible by 5 only
- return the number itself as a string otherwise

The implementation will consist of three files:
- backend/fizzbuzz.py: contains the FizzBuzz function
- backend/main.py: a tiny CLI script that iterates i from 1 to 15, printing each fizzbuzz(i) result on its own line
- backend/test_fizzbuzz.py: unit tests for the FizzBuzz function using the stdlib unittest framework

The beads for this implementation are:
- Implement backend/fizzbuzz.py per architecture
- Implement backend/main.py per architecture
- Implement backend/test_fizzbuzz.py per architecture

These beads will be created and tracked to ensure the implementation is completed correctly.
