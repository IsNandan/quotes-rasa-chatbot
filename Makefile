SHELL := /bin/bash

PYTHON ?= python3.10
VENV := .venv
PIP := $(VENV)/bin/pip
RASA := $(VENV)/bin/rasa
PY := $(VENV)/bin/python

.DEFAULT_GOAL := help

.PHONY: help check-python venv install setup train validate test shell run-actions run-server run-frontend smoke clean

help:
	@echo "Available targets:"
	@echo "  make setup         - Create venv and install dependencies"
	@echo "  make train         - Train Rasa model"
	@echo "  make validate      - Validate training data/domain"
	@echo "  make test          - Run Rasa tests"
	@echo "  make run-actions   - Start actions server (port 5055)"
	@echo "  make run-server    - Start Rasa API server (port 5005)"
	@echo "  make run-frontend  - Serve web frontend (port 8000)"
	@echo "  make smoke         - Send a REST test message"
	@echo "  make shell         - Start rasa shell"
	@echo "  make clean         - Remove local artifacts"

check-python:
	@command -v $(PYTHON) >/dev/null 2>&1 || { \
		echo "Error: $(PYTHON) not found."; \
		echo "Install Python 3.10 first, then rerun make setup."; \
		exit 1; \
	}
	@$(PYTHON) -c "import sys; assert sys.version_info[:2]==(3,10), f'Expected Python 3.10, got {sys.version}'"

venv: check-python
	@$(PYTHON) -m venv $(VENV)
	@$(PY) -m pip install --upgrade pip setuptools wheel

install: venv
	@$(PIP) install -r requirements.txt

setup: install
	@echo "Setup complete. Activate env with: source $(VENV)/bin/activate"

train:
	@$(RASA) train

validate:
	@$(RASA) data validate

test:
	@$(RASA) test

shell:
	@$(RASA) shell

run-actions:
	@$(RASA) run actions

run-server:
	@$(RASA) run --enable-api --cors "*" -p 5005

run-frontend:
	@python3 -m http.server 8000 --directory frontend

smoke:
	@echo "Smoke test requires Rasa API on :5005 (and ideally actions on :5055)."
	@bash scripts/smoke_test.sh

clean:
	@rm -rf .pytest_cache __pycache__ .rasa/cache
	@echo "Removed local cache artifacts."
