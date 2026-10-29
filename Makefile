PYTHON := python3
UV := uv
ARGS ?= default

.PHONY: install run debug clean lint lint-strict

install:
	$(UV) sync

run:
	$(UV) run $(PYTHON) -m src $(ARGS)

debug:
	$(UV) run $(PYTHON) -m pdb -m main.py

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type d -name .mypy_cache -prune -exec rm -rf {} +

lint:
	$(UV) run flake8 . --exclude .venv
	$(UV) run mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs --exclude .venv

lint-strict:
	$(UV) run flake8 . --exclude .venv
	$(UV) run mypy .