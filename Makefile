# Mock.GPIO Makefile
# Copyright (c) 2025 codenio ( Aananth K )
# SPDX-License-Identifier: GPL-3.0-only

.DEFAULT_GOAL := help
.PHONY: help install test clean build publish publish-test tox

PYTHON ?= /Users/aananth.k/workspace/personal/github/Mock.GPIO/.venv/bin/python3
PIP ?= /Users/aananth.k/workspace/personal/github/Mock.GPIO/.venv/bin/pip3
SCRIPTS_DIR ?= scripts

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-15s %s\n", $$1, $$2}'

install: ## Install the package locally (uses scripts/install.sh)
	chmod +x $(SCRIPTS_DIR)/install.sh
	./$(SCRIPTS_DIR)/install.sh

test: ## Run tests using pytest
	LOG_LEVEL=Info $(PYTHON) -m pytest -v

tox: ## Run tests across versions with tox (requires pyenv interpreters)
	$(PIP) install -r requirements-dev.txt
	tox -p auto

clean: ## Clean build artifacts (uses scripts/clean.sh)
	chmod +x $(SCRIPTS_DIR)/clean.sh
	./$(SCRIPTS_DIR)/clean.sh
	rm -rf Mock.GPIO.egg-info/ dist/

build: clean ## Build distribution packages
	$(PYTHON) setup.py sdist bdist_wheel

publish: ## Push to PyPI (uses scripts/updatepip.sh)
	chmod +x $(SCRIPTS_DIR)/updatepip.sh
	./$(SCRIPTS_DIR)/updatepip.sh

publish-test: build ## Publish to Test PyPI
	$(PYTHON) -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
