# Implementation plan
The implementation plan involves creating the following beads:
- te-001: Implement backend/fizzbuzz.py per architecture
- te-002: Implement backend/main.py per architecture
- te-003: Implement backend/test_fizzbuzz.py per architecture
These beads will be used to implement the FizzBuzz library in pure Python standard library, accompanied by a small CLI runner and a unit-test suite.
The library must expose a function fizzbuzz(n: int) -> str that follows the canonical FizzBuzz rules.
The CLI script backend/main.py should iterate over the range 1-15, printing each fizzbuzz(i) result on its own line, ending with FizzBuzz.
The unit-test suite backend/test_fizzbuzz.py should cover at least the four essential cases.
The implementation must be committed in a single conventional commit prefixed with feat:.
The total source lines across backend/fizzbuzz.py, backend/main.py, and backend/test_fizzbuzz.py must not exceed 40.
No extra files may be introduced; the rig scaffolding remains untouched.
