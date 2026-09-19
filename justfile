#!/usr/bin/env -S just --justfile

# List all files in the project
files:
    git ls-files

# Sync runtime dependencies
sync:
    uv sync

# Sync all extras, dev, and ci dependency groups
sync-all:
    uv sync --extra all --group dev --group ci

# Lint Python code with ruff
lint:
    uv run ruff check .

# Auto-fix issues
fix:
    uv run ruff check --fix .
    uv run ty check --fix .

# Check formatting with ruff (no modifications)
format-check:
    uv run ruff format --check .

# Format Python code with ruff
format:
    uv run ruff format .

# Type-check Python code with ty
ty:
    uv run ty check .

# Run the test suite
test:
    uv run pytest

# Verify REUSE licensing compliance
reuse:
    uv run reuse lint

# Run every check
check: lint format-check ty test reuse
