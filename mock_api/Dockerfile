# Use Python 3.11 as base
FROM python:3.11-slim

# Define working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy files needed for dependency installation
COPY ../mock_api/src/pyproject.toml ./

# Create empty README.md (if needed)
RUN touch README.md

# Generate poetry.lock
RUN poetry lock

# Install dependencies without virtual environment
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

# Copy the rest of the project including produtos.json
COPY ../mock_api/src/ ./

# Expose FastAPI port
EXPOSE 8000

# Command to run the API
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
