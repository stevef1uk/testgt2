# testgt2 — Gas Town Reference Rig

This rig is the canonical end-to-end test target for Gas Town
agents (Mayor → Architect → Planner → Polecat → QA).

While Gas Town is in early-alpha, the project intentionally stays
trivial so that any failure can be unambiguously attributed to the
agent system rather than to LLM domain knowledge.

## Default work item

When an operator sends "implement testgt2" without further detail,
build a minimal **FizzBuzz** library + runner + tests, in pure
Python stdlib (no third-party deps, no pip install required).

### Acceptance Criteria

- [ ] Create `backend/fizzbuzz.py` exporting `def fizzbuzz(n: int) -> str`
      with the canonical rules:
        - return `"FizzBuzz"` if `n` is divisible by 15
        - return `"Fizz"`     if `n` is divisible by 3 (and not 15)
        - return `"Buzz"`     if `n` is divisible by 5 (and not 15)
        - return `str(n)`     otherwise
- [ ] Create `backend/main.py` that, when run as `python3 backend/main.py`,
      prints the result of `fizzbuzz(i)` for `i` in `1..15` inclusive,
      one value per line, in that order. Final printed line must be
      `FizzBuzz`.
- [ ] Create `backend/test_fizzbuzz.py` using the stdlib `unittest`
      module, with at least these four cases:
        - `fizzbuzz(1)  == "1"`
        - `fizzbuzz(3)  == "Fizz"`
        - `fizzbuzz(5)  == "Buzz"`
        - `fizzbuzz(15) == "FizzBuzz"`
      The test must pass when run as `python3 -m unittest backend.test_fizzbuzz`.
- [ ] Commit all three files with a single conventional commit message
      starting `feat: ` (e.g. `feat: add fizzbuzz module with tests`).

### Notes

- Pure stdlib — do NOT add a `requirements.txt`, do NOT import
  fastapi, pytest, or any non-stdlib package.
- Total source size target: ≤ 40 lines across all three files.
- Polecat must commit ONLY the three `backend/` files (no scratch,
  no `typescript`, no `.gt-agent`, no `AGENTS.md`). Fix #95b enforces
  this at the worktree level — agents do not need to manage it.

## Operator workflow

```
gt mail send mayor/ -s "Project: testgt2 FizzBuzz" --stdin <<MSG
Implement testgt2 per SPEC.md at the rig root.
MSG
gt nudge mayor "Check your mail"
```

Mayor coordinates: slings the Architect for design, then the Planner
for breakdown, then a Polecat for implementation, then QA for review.
