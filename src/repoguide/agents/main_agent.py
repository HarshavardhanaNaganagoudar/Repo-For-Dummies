from deepagents import create_deep_agent
from repoguide.agents.sub_agent import github_repo_subagent


instructions = """
You are a technical writer that creates extremely beginner-friendly setup guides.

Audience:
People with almost zero programming knowledge.

Rules:
- Write step-by-step instructions
- Assume the reader has never used a terminal
- Explain every command briefly
- Separate Mac / Windows / Linux
- Include troubleshooting
- Use Markdown headings
"""


def build_agent():
    agent = create_deep_agent(
        model="mistral-large-latest",
        system_prompt=instructions,
        subagents=[github_repo_subagent],
    )

    return agent