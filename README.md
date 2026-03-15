# Repo For Dummies

Turn any GitHub repository into a **step-by-step beginner setup guide**.

Repo For Dummies reads a repository README and generates simple instructions so anyone can run the project — even with little technical experience.

---

## Example

Input:

https://github.com/langchain-ai/deepagents

Output:

```
# Run DeepAgents Today

Step 1: Install Python  
Step 2: Clone the repository  
Step 3: Install dependencies  
Step 4: Run the project
```

---

# Installation

Clone the repository:

```
git clone https://github.com/HarshavardhanaNaganagoudar/Repo-For-Dummies.git
cd Repo-For-Dummies
```

Install dependencies using **uv**:

```
uv sync
```

---

# Setup

Create a `.env` file:

```
cp .env.example .env
```

Add your API keys:

```
GEMINI_API_KEY=
MISTRAL_API_KEY=
GITHUB_API_KEY=
```

---

# Run the Agent

```
uv run python scripts/run.py
```

Example:

```
repo_url = "https://github.com/langchain-ai/deepagents"
```

The agent will generate a beginner-friendly setup guide.

---

# Project Structure

```
repo-for-dummies
│
├── scripts
│   └── run.py
│
├── src
│   └── repoguide
│       ├── agents
│       ├── tools
│       ├── main.py
│       └── config.py
│
├── .env.example
├── pyproject.toml
└── README.md
```

---

# How It Works

The system uses **two agents**:

**Main Agent**

* Generates beginner-friendly instructions

**GitHub Subagent**

* Fetches repository README
* Extracts technical information

---

# Future Improvements

* Parse full repositories (not just README)
* Auto-detect install commands
* CLI interface
* Docker execution testing

---

# License

MIT License
