# SkyNetix Systems LLP
## Agentic AI Engineering — Student Setup Checklist

This checklist prepares students for the Agentic AI Engineering course. Install the core tools first, then add AI frameworks as you reach each module.

## A. Software Installations

1. **Anaconda Distribution** — Python, Conda, Jupyter Notebook, and JupyterLab  
   https://www.anaconda.com/download

2. **Visual Studio Code** — Primary code editor  
   https://code.visualstudio.com/download

3. **Python Extension for VS Code** — Python support and debugging  
   https://marketplace.visualstudio.com/items?itemName=ms-python.python

4. **Git for Windows** — Version control and GitHub integration  
   https://git-scm.com/install/windows

5. **Postman** — REST API testing  
   https://www.postman.com/downloads/

6. **Node.js (LTS)** — JavaScript runtime for Node.js-based tools and integrations  
   https://nodejs.org/en/download

7. **uv** — Python package and environment management tool  
   https://docs.astral.sh/uv/getting-started/installation/

## B. Python Package

8. **python-dotenv** — Loads API keys and configuration from `.env` files.

   Install it inside your project's activated Python environment:

   ```bash
   python -m pip install python-dotenv
   ```

   Documentation: https://pypi.org/project/python-dotenv/

## C. Accounts to Create

9. **GitHub** — Source code hosting and project repositories  
   https://github.com/

10. **Google AI Studio** — Access to Gemini models and API keys  
    https://aistudio.google.com/

## D. AI Frameworks — Install During the Course

Install these when the corresponding training module begins:

- **CrewAI** — Multi-agent AI systems
- **LangChain** — LLM integrations and tools
- **LangGraph** — Stateful agent workflows
- **MCP Python SDK** — Model Context Protocol integrations
- **ChromaDB** — Vector storage and retrieval
- **FastAPI** — Build APIs for AI applications

## Important Notes

- Do not install JupyterLab separately if it is already available in your Anaconda installation.
- Do not install VS Code again if it is already installed.
- Keep API keys in environment variables or `.env` files; never commit secrets to GitHub.
- Use a dedicated Python environment for each project to avoid dependency conflicts.
- Node.js is needed only for modules or tools that depend on it; it is not required for every Python-based AI project.
- Some AI APIs have usage limits or charges. Check the provider's current pricing before use.

## Recommended Setup Order

1. Install Anaconda and VS Code.
2. Install the Python extension in VS Code.
3. Install Git and verify that it works.
4. Create your GitHub and Google AI Studio accounts.
5. Install `uv` and learn which Python environment each project uses.
6. Install Python packages and AI frameworks as they are introduced in the course.
