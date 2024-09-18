poetry run ruff check .
poetry run black --check .
poetry run mypy .
poetry run pytest --verbose . --cov --cov-report term-missing