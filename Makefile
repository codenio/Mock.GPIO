# Mock.GPIO Makefile
# Standard Makefile for Python package development

.DEFAULT_GOAL := help
.PHONY: help install test clean build publish dev-install lint format check all

# Variables
PYTHON := /Users/aananth.k/workspace/personal/github/Mock.GPIO/.venv/bin/python3
PIP := /Users/aananth.k/workspace/personal/github/Mock.GPIO/.venv/bin/pip3
PYTEST := /Users/aananth.k/workspace/personal/github/Mock.GPIO/.venv/bin/pytest
SCRIPTS_DIR := scripts

# Colors for output
RED := \033[31m
GREEN := \033[32m
YELLOW := \033[33m
BLUE := \033[34m
RESET := \033[0m

help: ## Show this help message
	@echo "$(BLUE)Mock.GPIO - Available Commands$(RESET)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-15s$(RESET) %s\n", $$1, $$2}'
	@echo ""

install: ## Install the package locally (uses scripts/install.sh)
	@echo "$(YELLOW)Installing Mock.GPIO locally...$(RESET)"
	@chmod +x $(SCRIPTS_DIR)/install.sh
	@./$(SCRIPTS_DIR)/install.sh
	@echo "$(GREEN)✓ Installation completed$(RESET)"

dev-install: ## Install package in development mode
	@echo "$(YELLOW)Installing Mock.GPIO in development mode...$(RESET)"
	@$(PIP) install -e .
	@echo "$(GREEN)✓ Development installation completed$(RESET)"

test: ## Run tests using pytest
	@echo "$(YELLOW)Running tests...$(RESET)"
	@LOG_LEVEL=Info PYTHONPATH=. $(PYTHON) -m pytest tests/ -v
	@echo "$(GREEN)✓ Tests completed$(RESET)"

test-verbose: ## Run tests with verbose output
	@echo "$(YELLOW)Running tests with verbose output...$(RESET)"
	@LOG_LEVEL=Debug PYTHONPATH=. $(PYTHON) -m pytest tests/ -vv -s
	@echo "$(GREEN)✓ Verbose tests completed$(RESET)"

clean: ## Clean build artifacts (uses scripts/clean.sh)
	@echo "$(YELLOW)Cleaning build artifacts...$(RESET)"
	@chmod +x $(SCRIPTS_DIR)/clean.sh
	@./$(SCRIPTS_DIR)/clean.sh
	@rm -rf Mock.GPIO.egg-info/
	@rm -rf Mock/__pycache__/
	@rm -rf tests/__pycache__/
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "$(GREEN)✓ Cleaning completed$(RESET)"

build: clean ## Build distribution packages
	@echo "$(YELLOW)Building distribution packages...$(RESET)"
	@$(PYTHON) setup.py sdist bdist_wheel
	@echo "$(GREEN)✓ Build completed$(RESET)"

publish: ## Push to PyPI (uses scripts/updatepip.sh)
	@echo "$(YELLOW)Publishing to PyPI...$(RESET)"
	@echo "$(RED)⚠️  This will publish to PyPI. Make sure you want to proceed!$(RESET)"
	@read -p "Continue? [y/N] " -n 1 -r; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		echo ""; \
		chmod +x $(SCRIPTS_DIR)/updatepip.sh; \
		set -e; \
		./$(SCRIPTS_DIR)/updatepip.sh; \
		echo "$(GREEN)✓ Published to PyPI$(RESET)"; \
	else \
		echo ""; \
		echo "$(YELLOW)Publication cancelled$(RESET)"; \
	fi

publish-test: build ## Publish to test PyPI
	@echo "$(YELLOW)Publishing to Test PyPI...$(RESET)"
	@twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	@echo "$(GREEN)✓ Published to Test PyPI$(RESET)"

lint: ## Run linting checks
	@echo "$(YELLOW)Running linting checks...$(RESET)"
	@$(PYTHON) -m flake8 Mock/ tests/ --max-line-length=100 --ignore=E203,W503 || echo "$(YELLOW)flake8 not installed, skipping...$(RESET)"
	@echo "$(GREEN)✓ Linting completed$(RESET)"

format: ## Format code using black
	@echo "$(YELLOW)Formatting code...$(RESET)"
	@$(PYTHON) -m black Mock/ tests/ --line-length=100 || echo "$(YELLOW)black not installed, skipping...$(RESET)"
	@echo "$(GREEN)✓ Formatting completed$(RESET)"

check: lint test ## Run all checks (lint + test)
	@echo "$(GREEN)✓ All checks passed$(RESET)"

requirements: ## Install development requirements
	@echo "$(YELLOW)Installing requirements...$(RESET)"
	@$(PIP) install -r requirements.txt
	@echo "$(GREEN)✓ Requirements installed$(RESET)"

all: clean requirements dev-install test lint ## Run complete development setup
	@echo "$(GREEN)✓ Complete setup finished$(RESET)"

info: ## Show project information
	@echo "$(BLUE)Mock.GPIO Project Information$(RESET)"
	@echo "Project: Mock.GPIO"
	@echo "Description: Mock Library for RPi.GPIO"
	@echo "Author: Aananth K"
	@echo "License: GPL-3.0"
	@echo ""
	@echo "$(BLUE)Available Scripts:$(RESET)"
	@ls -la $(SCRIPTS_DIR)/
	@echo ""
