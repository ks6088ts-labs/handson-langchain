import os

import typer
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain_experimental.tools.python.tool import PythonREPLTool

app = typer.Typer()


@app.command()
def run(
    prompt: str = None,
    env_file: str = "./notebooks/credentials.env",
):
    """
    Use cases:
        Test code generation: Generate test code from a given code snippet
            > poetry run python scripts/code.py --env-file "./notebooks/credentials.env" --prompt '"あなたは python で書かれたプログラムコードからテストフレームワーク pytest を使ったテストコードを生成するのに役立つ Microsoft のソフトウェアエンジニアです。以下のプログラムコードに対応するテストコードを作成し、test_generated.py として保存してください。\\n```python\\n def add(a: int, b: int):\\n  return a + b```"'
        Test code generation: Review codes passed from prompt
            > poetry run python scripts/code.py --env-file "./notebooks/credentials.env" --prompt '"あなたは Microsoft のソフトウェアエンジニアです。以下のプログラムコードをレビューし、Reviewdog Diagnostic Format に沿ったフォーマットでレビュー結果を result.rdjson として保存してください。\\n```python\\n def add(a: int, b: int):\\n  return a - b```"'
    """
    if prompt is None:
        _prompt = typer.prompt("Please input prompt")
        prompt = f'"{_prompt}"'

    typer.echo(f"Running pipeline with {env_file}, {prompt}")
    load_dotenv(env_file)

    llm = ChatOpenAI(
        model_name=os.getenv("OPENAI_MODEL_NAME"),
        openai_api_base=os.getenv("OPENAI_API_BASE"),
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0,
        model_kwargs={
            "deployment_id": os.getenv("OPENAI_DEPLOYMENT_ID"),
            "api_type": os.getenv("OPENAI_API_TYPE"),
            "api_version": os.getenv("OPENAI_API_VERSION"),
        },
    )

    tools = [
        PythonREPLTool(),
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        verbose=True,
    )

    agent.run(prompt)


if __name__ == "__main__":
    app()
