FROM python:3.11-slim-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./ ./

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --without dev,playground

CMD [ "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8888" ]
