# Architecture for testgt2

## Overview
The testgt2 rig serves as the canonical end‑to‑end test target for Gas Town agents. Its purpose is to verify that the agent pipeline (Mayor → Architect → Planner → Polecat → QA) can correctly interpret a simple specification, produce the required source files, and validate them without external dependencies. The implementation is a minimal FizzBuzz library written in pure Python standard library, accompanied by a small CLI runner and a unit‑test suite. All source code resides under a top‑level directory named `backend`, and the total line count across the three files must not exceed 40 lines.

## Goals and Constraints
- **Goal 1:** Provide a function `fizzbuzz(n: int) -> str` that follows the canonical FizzBuzz rules.
- **Goal 2:** Expose a CLI script (`backend/main.py`) that prints `fizzbuzz(i)` for `i` from 1 to 15, one per line, ending with `FizzBuzz`.
- **Goal 3:** Deliver a comprehensive unit‑test suite (`backend/test_fizzbuzz.py`) using the `unittest` framework, covering at least the four essential cases.
- **Constraint 1:** No third‑party packages; only Python stdlib may be used.
- **Constraint 2:** The implementation must be committed in a single conventional commit prefixed with `feat:`.
- **Constraint 3:** Total source lines across `backend/fizzbuzz.py`, `backend/main.py`, and `backend/test_fizzbuzz.py` must be ≤ 40.
- **Constraint 4:** No extra files (e.g., `requirements.txt`, configuration files, or scratch files) may be introduced; the rig scaffolding remains untouched.

## System Architecture
The system is intentionally simple, consisting of three modules that interact as follows:

1. **fizzbuzz.py** – Contains the core logic. It defines a single public function `fizzbuzz(n)` that returns the appropriate string based on divisibility by 3, 5, and 15.
2. **main.py** – Imports `fizzbuzz` from `fizzbuzz.py` and iterates over the range 1‑15, printing each result. This serves as a demonstration and a quick sanity check.
3. **test_fizzbuzz.py** – Imports `fizzbuzz` and defines a `unittest.TestCase` with test methods for the required cases (and optionally additional edge cases). The test suite can be invoked via `python3 -m unittest backend.test_fizzbuzz`.

There are no external services, databases, or network components; all communication is via direct function calls and standard I/O.

## Components

### backend/fizzbuzz.py
- **Responsibility:** Encapsulate the FizzBuzz rule set.
- **Public API:** `def fizzbuzz(n: int) -> str`
- **Behavior:**
  - If `n % 15 == 0` → return `"FizzBuzz"`
  - Else if `n % 3 == 0` → return `"Fizz"`
  - Else if `n % 5 == 0` → return `"Buzz"`
  - Else → return `str(n)`
- **Design Notes:** No state is maintained; the function is pure and deterministic.

### backend/main.py
- **Responsibility:** Provide a runnable script that demonstrates the library.
- **Execution:** When invoked as `python3 backend/main.py`, it prints the FizzBuzz sequence for 1‑15.
- **Implementation:** Imports `fizzbuzz`, loops `for i in range(1, 16)`, prints `fizzbuzz(i)`.
- **Output Format:** One result per line, no extra whitespace or banners.

### backend/test_fizzbuzz.py
- **Responsibility:** Validate correctness of `fizzbuzz`.
- **Framework:** Python `unittest` (stdlib).
- **Test Cases (minimum):**
  - `test_one`: `fizzbuzz(1) == "1"`
  - `test_three`: `fizzbuzz(3) == "Fizz"`
  - `test_five`: `fizzbuzz(5) == "Buzz"`
  - `test_fifteen`: `fizzbuzz(15) == "FizzBuzz"`
- **Additional Coverage (optional but encouraged):** Other numbers (e.g., 2, 6, 10, 30) to ensure robustness.
- **Execution:** `python3 -m unittest backend.test_fizzbuzz` should exit with code 0 if all tests pass.

## Interfaces
- **Module Interface:** `fizzbuzz.py` exports a single function; both `main.py` and `test_fizzbuzz.py` import it via `from fizzbuzz import fizzbuzz`.
- **CLI Interface:** `main.py` reads no arguments; its output is stdout only.
- **Test Interface:** The test suite is discovered by unittest via standard naming conventions (`test_*` methods).

## Data Flow
1. **Development:** Author writes the three files.
2. **Build/Compile:** No compilation step; Python interprets the source directly.
3. **Execution (Demo):** Running `main.py` triggers:
   - Import of `fizzbuzz`.
   - Loop over integers 1‑15.
   - For each integer, call `fizzbuzz(i)` and capture its return string.
   - Print the string to stdout.
4. **Validation (Test):** Running the unittest command triggers:
   - Import of `fizzbuzz` and `unittest`.
   - Execution of each test method, which calls `fizzbuzz` with specific inputs and asserts equality with expected strings.
   - Reporting of success/failure to stdout.

## Testing Strategy
- **Unit Tests:** Focus on the functional correctness of `fizzbuzz`. Each test is isolated and exercises a distinct branch of the conditional logic.
- **Regression Prevention:** By committing the test suite alongside the implementation, future changes that break the contract will be immediately detected.
- **Run‑time Validation:** The CLI script provides a quick visual check; the automated test suite provides deterministic validation.
- **Coverage:** The four required cases cover all branches (divisible by 3 only, 5 only, both, and neither). Additional cases may be added to increase confidence without violating the line‑count limit.

## Implementation Plan
1. **Create `backend/fizzbuzz.py`** – Implement the `fizzbuzz` function with a simple if‑elif‑else chain.
2. **Create `backend/main.py`** – Write the loop and print statements.
3. **Create `backend/test_fizzbuzz.py`** – Define the unittest test case with the four required test methods.
4. **Verify Line Count:** Ensure total lines ≤ 40 (approximately 12‑15 lines per file).
5. **Commit:** Stage the three files and commit with a message like `feat: add fizzbuzz module with tests`.
6. **Validate:** Run `python3 -m unittest backend.test_fizzbuzz` and manually inspect `python3 backend/main.py` output.

## Acceptance Mapping
| SPEC Requirement | Architectural Decision |
|------------------|------------------------|
| `backend/fizzbuzz.py` exporting `fizzbuzz(n: int) -> str` | Core component implements the function exactly as specified. |
| Canonical rules (15 → FizzBuzz, 3 → Fizz, 5 → Buzz, else str(n)) | Implemented via ordered if‑elif‑else checks. |
| `backend/main.py` prints fizzbuzz(i) for i in 1..15, one per line, final line FizzBuzz | Simple loop with print; no extra output. |
| `backend/test_fizzbuzz.py` using unittest with at least four cases | Test suite defines test methods for 1, 3, 5, 15; uses stdlib unittest. |
| Tests runnable via `python3 -m unittest backend.test_fizzbuzz` | Test module follows unittest discovery conventions. |
| Single conventional commit prefixed with `feat:` | Implementation plan specifies a single commit after all three files are ready. |
| No third‑party dependencies, pure stdlib | All components import only from the standard library. |
| Total source lines ≤ 40 across three files | Each file is kept concise; the architecture does not mandate exceeding this limit. |
| Only the three backend files committed; no extra files | Architecture limits itself to describing those three files; no additional artifacts are proposed. |

## Conclusion
This architecture provides a clear, minimal, and SPEC‑aligned blueprint for the testgt2 rig. It delineates the responsibilities of each module, defines their interactions, outlines the testing and validation approach, and maps directly to the acceptance criteria. Following this plan will enable the downstream roles (Planner, Polecat, QA) to produce a correct, compliant implementation with minimal overhead.

