# Architecture for testgt2 FizzBuzz rig

## Overview
This architecture outlines a minimal FizzBuzz implementation in Python using only the standard library, fully aligned with the provided SPEC. The goal is to create a clean, testable, and maintainable codebase within strict constraints: no third-party dependencies, total code under 40 lines, and compliance with conventional commits. The system is divided into three core components, each mapped directly to acceptance criteria.

## Planned file layout
- `backend/fizzbuzz.py` — Contains a pure function `fizzbuzz(n)` that returns the appropriate string based on canonical FizzBuzz rules: "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for multiples of both, and the string representation of the number otherwise.
- `backend/main.py` — A short script that calls and prints the results of `fizzbuzz(i)` for i from 1 to 15, inclusive, with each result on a new line, ending with "FizzBuzz" for input 15.
- `backend/test_fizzbuzz.py` — A unittest-based test suite that validates key cases: 1 (returns "1"), 3 (returns "Fizz"), 5 (returns "Buzz"), and 15 (returns "FizzBuzz"). The test must pass when executed via `python3 -m unittest backend.test_fizzbuzz`.

## Notes for polecat
1. Implementation order: First `fizzbuzz.py`, then `test_fizzbuzz.py`, and finally `main.py`.
2. After writing files, run `python3 -m unittest backend.test_fizzbuzz` from the repository root to verify correctness.
3. Commit all files using `feat: add FizzBuzz functionality` or similar conventional commit messages.
