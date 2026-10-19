# Build an LLM Gateway Python and FastAPI



# Generate Repo
- uv init --no-package --python 3.12 .
- uv add "fastapi[standard]" pydantic-settings httpx
- uv add --dev pytest pytest-asyncio ruff mypy

# App structure
- mkdir -p app/api/v1 app/core app/services app/providers tests docs
- touch app/__init__.py
- touch app/api/__init__.py app/api/v1/__init__.py
- touch app/core/__init__.py app/services/__init__.py - app/providers/__init__.py

- uv run uvicorn app.main:app --reload


# Install deps
- uv sync --locked
