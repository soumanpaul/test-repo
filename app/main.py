
from fastapi import FastAPI 

app = FastAPI(
    title="LLM Gateway",
    description="A backend for controlled access to LLM providers.",
    version="0.1.0"
)

@app.get("/health/live", tags=["health"])
async def liveness() -> dict[str, str]:
    return {"status": "ok"}
    