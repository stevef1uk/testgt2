# Simple Test: Hello API

## Goal
Create a simple FastAPI backend with one endpoint.

## Deliverables

1. `backend/main.py` - FastAPI app with:
   - `GET /` → returns `{"message": "Hello from Defender Clone!"}`

2. `backend/requirements.txt` - Contains: `fastapi` `uvicorn`

## Steps

1. Create `backend/` directory
2. Create `main.py` with the endpoint
3. Create `requirements.txt`
4. Test by running `uvicorn main:app --port 8000`
5. Verify with `curl http://localhost:8000/`
6. Commit and run `gt done`