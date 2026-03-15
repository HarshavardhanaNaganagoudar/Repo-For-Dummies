from typing import Dict
import requests
import base64
from langchain.tools import tool


@tool
def get_repo_readme(owner: str, repo: str) -> Dict:
    """
    Fetches the README.md file from a GitHub repository.

    Args:
        owner: GitHub username or organization name.
        repo: Name of the repository.

    Returns:
        dict: Contains repository name and decoded README content.
    """

    url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    headers = {
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {
            "error": f"Failed to fetch README. Status code: {response.status_code}"
        }

    data = response.json()

    readme_encoded = data.get("content", "")

    if not readme_encoded:
        return {"error": "README content not found."}

    readme_decoded = base64.b64decode(readme_encoded).decode("utf-8")

    return {
        "repository": f"{owner}/{repo}",
        "readme": readme_decoded
    }