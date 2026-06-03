from dotenv import load_dotenv

load_dotenv()

from langchain_core import  __version__ as core_version
from langchain import __version__ as graph_version
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from importlib.metadata import version


def main():
    print("Hello from langc-course!")
    print(f"LangChain Core version: {core_version}")
    print(f"LangChain Graph version: {graph_version}")

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.9)
    response = llm("say setup complete")
    print(f"OpenAI response: {response}")

    # set up anthropic
    llm_anthropic = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0.9)
    response_anthropic = llm_anthropic("say setup complete")
    print(f"Anthropic response: {response_anthropic}")

    print("Setup complete!")


if __name__ == "__main__":
    main()
