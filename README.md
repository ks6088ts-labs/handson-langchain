[![test](https://github.com/ks6088ts-labs/handson-langchain/workflows/test/badge.svg)](https://github.com/ks6088ts-labs/handson-langchain/actions/workflows/test.yml)
[![release](https://github.com/ks6088ts-labs/handson-langchain/workflows/release/badge.svg)](https://github.com/ks6088ts-labs/handson-langchain/actions/workflows/release.yml)

# handson-langchain
Hands on langchain

## Prerequisites

- [Poetry](https://python-poetry.org/): Python packaging and dependency management tool
- [Python](https://www.python.org/downloads/): 3.11
- [GNU Make](https://www.gnu.org/software/make/): As a task runner

## Get Started

### Environment settings

Put following files in the project root directory.

**chat.env**
```
openai_model_name = "gpt-35-turbo"
openai_deployment_id = "chat"
openai_api_type = "azure"
openai_api_key = "your-api-key"
openai_api_base = "https://AOAI_NAME.openai.azure.com/"
openai_api_version = "2023-07-01-preview"
```

**azure_cognitive_search.env**
```
service_name = "your-service-name"
index_name = "your-index-name"
api_key = "your-api-key"
```

### Run server

**Install dependencies**

```shell
make install-deps-dev
```

**Run API server**

```shell
make run
```

**Run docker container**

```shell
# See Makefile to set environment variables via `--env` option
make docker-run
```

### Development

**Play with API server**

Run API server locally and access to the API server's swagger UI http://localhost:8888/docs

**Run jupyterlab server as a playground**

```shell
make jupyterlab
```

**Run CI tests locally**

```shell
make ci-test
```
