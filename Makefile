SOURCE_FILES ?= $(shell find . -type d \( -name dist -o -name .venv \) -prune -o -type f -name '*.py' -print)

GIT_REVISION ?= $(shell git rev-parse --short HEAD)
GIT_TAG ?= $(shell git describe --tags --abbrev=0 | sed -e s/v//g)
DEBUG ?= False

DOCKERHUB_USERNAME ?= ks6088ts
DOCKER ?= docker
DOCKER_IMAGE_NAME ?= handson-langchain
DOCKER_PLATFORM ?= linux/amd64
DOCKER_TAG_NAME ?= $(DOCKERHUB_USERNAME)/$(DOCKER_IMAGE_NAME):$(GIT_TAG)

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help

.PHONY: install-deps-dev
install-deps-dev: ## install dependencies for development
	poetry install

.PHONY: install-deps-ci
install-deps-ci: ## install dependencies for CI
	poetry install --with lint,test

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
	REVISION=$(GIT_REVISION) VERSION=$(GIT_TAG) DEBUG=$(DEBUG) \
		poetry run uvicorn api.main:app --host 0.0.0.0 --port 8888 --reload

.PHONY: jupyterlab
jupyterlab: ## run jupyterlab server
	poetry run jupyter lab --port 8889

.PHONY: docker-build
docker-build: ## docker build
	$(DOCKER) build --platform=$(DOCKER_PLATFORM) -t $(DOCKER_TAG_NAME) .

.PHONY: docker-run
docker-run: ## docker run
	$(DOCKER) run --platform=$(DOCKER_PLATFORM) --rm \
		-p "8888:8888" \
		--env "REVISION=$(GIT_REVISION)" \
		--env "VERSION=$(GIT_TAG)" \
		$(DOCKER_TAG_NAME)
