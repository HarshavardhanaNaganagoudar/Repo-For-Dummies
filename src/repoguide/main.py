from dotenv import load_dotenv
load_dotenv()
from repoguide.agents.main_agent import build_agent


def run(repo_url: str):

    agent = build_agent()

    result = agent.invoke({
        "messages": [
            {"role": "user", "content": repo_url}
        ]
    })

    print(result["messages"][-1].content)


if __name__ == "__main__":
    run("https://github.com/langchain-ai/deepagents")