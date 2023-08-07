SOURCE_FILES ?= $(shell find . -type d \( -name dist -o -name .venv \) -prune -o -type f -name '*.py' -print)

GIT_REVISION ?= $(shell git rev-parse --short HEAD)
GIT_TAG ?= $(shell git describe --tags --abbrev=0 | sed -e s/v//g)

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help

.PHONY: install-deps-dev
install-deps-dev: ## install dependencies for development
	poetry install

.PHONY: install-deps-ci
install-deps-ci: ## install dependencies for CI
	poetry install --without playground

.PHONY: format
format: ## format codes
	poetry run isort $(SOURCE_FILES)
	poetry run black $(SOURCE_FILES)

.PHONY: fix
fix: ## fix codes
	poetry run ruff $(SOURCE_FILES) --fix

.PHONY: lint
lint: ## lint
	poetry run isort --check-only $(SOURCE_FILES)
	poetry run black --check $(SOURCE_FILES)
	poetry run ruff $(SOURCE_FILES)

.PHONY: test
test: ## run tests
	poetry run pytest

.PHONY: ci-test
ci-test: install-deps-ci lint test ## ci test

.PHONY: run
run: ## run server
	REVISION=$(GIT_REVISION) VERSION=$(GIT_TAG) \
		poetry run uvicorn api.main:app --port 8888 --reload

.PHONY: jupyterlab
jupyterlab: ## run jupyterlab server
	poetry run jupyter lab --port 8889
