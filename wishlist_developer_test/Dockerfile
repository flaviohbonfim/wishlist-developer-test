FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY ../wishlist_developer_test/src/pyproject.toml ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

COPY ../wishlist_developer_test/src/ .

EXPOSE 5000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
