
from repoguide.tools.github_tools import get_repo_readme

github_repo_subagent = {
    "name": "github_repo_agent",
    "description": "Fetches the README.md file from a GitHub repository.",
    "system_prompt": """You are a GitHub repository analyzer.

Read the repository README and extract information.
Do not explain anything.
Do not add tutorials.
Only extract facts from the README.""",
    "tools": [get_repo_readme],
    "model":"google_genai:gemini-2.5-flash-lite",  # Optional override, defaults to main agent model
}