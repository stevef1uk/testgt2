# testgt2 — Gas Town Reference Rig

This rig is the canonical end-to-end test target for Gas Town
agents (Mayor → Architect → Planner → Polecat → QA).

While Gas Town is in early-alpha, the project intentionally stays
trivial so that any failure can be unambiguously attributed to the
agent system rather than to LLM domain knowledge.

## Default work item

When an operator sends "implement testgt2" without further detail,
build a minimal FastAPI Hello World service.

### Acceptance Criteria

- [ ] Create `backend/main.py` with a FastAPI app
- [ ] Define route `GET /` returning `{"message": "Hello from testgt2!"}`
- [ ] Create `backend/requirements.txt` containing `fastapi` and `uvicorn`
- [ ] Commit both files with message: `feat: hello world backend`

### Notes

- Minimal scope: ~10 lines of Python total.
- No tests required for the alpha canary.
- Polecat must commit ONLY the two `backend/` files (no agent scratch).

## Operator workflow

```
gt mail send mayor/ -s "Project: testgt2 Hello API" --stdin <<MSG
Implement testgt2 per SPEC.md at the rig root.
MSG
gt nudge mayor "Check your mail"
```

Mayor coordinates: slings the Architect for design, then the Planner
for breakdown, then a Polecat for implementation, then QA for review.
