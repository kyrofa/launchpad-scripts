#!/bin/sh -e

dir=$(CDPATH="" cd -- "$(dirname -- "$0")" && pwd)

# Run black
echo "Running black..."
black --check --diff "$dir"

# Run flake8
echo "Running flake8..."
flake8 "$dir"

# Run mypy
echo "Running mypy..."
python3 -m mypy "$dir"

# Run unit tests
pytest
