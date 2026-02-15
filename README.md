# Steps to set up
uv init
## create virtual environment
uv venv

## Activate Virtual Environment
.venv\Scripts\activate

## Install dependencies
uv add fastapi uvicorn langgraph langchain openai python-dotenv




🧠 Why Modern Python Prefers pyproject.toml

## requirements.txt is:

Flat list of packages

No metadata

No project configuration

No dependency grouping

No reproducible locking (unless you freeze)

## pyproject.toml:

Defines project metadata

Defines dependencies

Supports dev dependencies

Works with modern tools (uv, poetry, hatch)

Has a proper lock file


## How to push to GitHub
Create repo in GitHub.com
Opened git bash from my working folder on local and executed git init (uv had already initiated)
Ensured .gitignore is having all the entries properly
git remote add origin https://github.com/sourav-learning/doc-processing-agentic-ai-poc.git
To check status of files in terms of check in : git status
To add all the files : git add .
To commit the added files: git commit -m "Initial commit: agentic document processing POC"
To check the name of branch created : git branch
(Optional) If the branch name is master, change it to main: git branch -M main
git push -u origin main