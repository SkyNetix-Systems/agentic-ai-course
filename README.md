# Create and Activate Conda Environment

This guide explains how to set up Python, install Agentic AI dependencies using `uv`, configure Jupyter Notebook in VS Code, and run your first Python notebook.

## 1. Create the Conda Environment

Create a Conda environment named `agentic-ai` with Python 3.12.

```bash
conda create -n agentic-ai python=3.12 -y
```

If the environment already exists, skip this step.

## 2. Activate the Environment

Activate the environment before installing packages or running Python programs.

```bash
conda activate agentic-ai
```

Your terminal prompt should now display `(agentic-ai)`.

## 3. Verify the Python Version

Confirm that Python 3.12 is active.

```bash
python --version
```

Expected output:

```text
Python 3.12.x
```

## 4. Find the Conda Environment Location

On Windows, the environment is typically stored at:

```text
C:\Users\<YourUsername>\anaconda3\envs\agentic-ai
```

Replace `<YourUsername>` with your Windows username. The actual location may differ if you installed Miniconda or Anaconda elsewhere.

To display your environment locations, run:

```powershell
conda env list
```

Look for `agentic-ai` in the output.

To find the exact Python executable used by the active environment, run:

```powershell
python -c "import sys; print(sys.executable)"
```

The path should point to the `agentic-ai` environment.

## 5. Navigate to Your Agentic AI Project

Navigate to your project directory:

```powershell
cd D:\SkyNetix\agentic-ai-course
```

Activate the environment if it is not already active:

```powershell
conda activate agentic-ai
```

Your terminal should look similar to:

```text
(agentic-ai) PS D:\SkyNetix\agentic-ai-course>
```

## 6. Install uv

`uv` is a fast Python package manager that you can use instead of running `pip` directly.

If `uv` is not installed, run:

```powershell
winget install --id astral-sh.uv -e
```

Restart your terminal if necessary, then verify the installation:

```powershell
uv --version
```

Official installation guide: https://docs.astral.sh/uv/getting-started/installation/

## 7. Install Project Dependencies Using uv

Ensure the `agentic-ai` Conda environment is active.

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install all dependencies listed in `requirements.txt`:

```powershell
uv pip install -r requirements.txt
```

**Important:** Do not use `--system`. The command above installs packages into the active environment when that environment is correctly activated.

If you encounter installation errors, read the complete error message before attempting to reinstall packages.

## 8. Install Jupyter Notebook Support

Install Jupyter and the IPython kernel in the active Conda environment:

```powershell
uv pip install ipykernel jupyter
```

These packages allow VS Code to execute Python notebooks using your `agentic-ai` environment.

Install the VS Code extensions if necessary:

1. Open VS Code.
2. Press `Ctrl + Shift + X`.
3. Search for **Python**, published by Microsoft, and install it.
4. Search for **Jupyter**, published by Microsoft, and install it.

## 9. Register the Conda Environment as a Jupyter Kernel

Register the environment so it can be selected inside Jupyter notebooks.

Run:

```powershell
python -m ipykernel install --user --name agentic-ai --display-name "Python (agentic-ai)"
```

The command should confirm that the kernel specification was installed.

## 10. Create a Jupyter Notebook in VS Code

Follow these steps:

1. Open VS Code.
2. Open your `agentic-ai-course` project folder.
3. Press `Ctrl + Shift + P` to open the Command Palette.
4. Search for `Jupyter: Create New Jupyter Notebook`.
5. Select the command.
6. Press `Ctrl + S` to save the notebook.

For example, save it as:

```text
D:\SkyNetix\agentic-ai-course\1_foundations\lab-1.ipynb
```

Ensure the `1_foundations` folder exists before saving.

Your project structure should look similar to:

```text
agentic-ai-course/
│
├── 1_foundations/
│   └── lab-1.ipynb
│
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## 11. Select the Correct Jupyter Kernel

Open `1_foundations/lab-1.ipynb`.

1. Click **Select Kernel** in the top-right corner of the notebook.
2. Select **Python Environments**.
3. Look for your `agentic-ai` Conda environment.
4. Select the interpreter whose path points to your Conda environment.

The displayed name may look like:

```text
Python 3.12.x ('agentic-ai': conda)
```

The interpreter path should resemble:

```text
C:\Users\<YourUsername>\anaconda3\envs\agentic-ai\python.exe
```

Do not select your global Python installation if it points to a different environment.

If the environment does not appear:

1. Confirm that `ipykernel` is installed.
2. Run the kernel registration command from Step 9.
3. Reload VS Code using `Ctrl + Shift + P` → `Developer: Reload Window`.
4. Open the notebook and select the kernel again.

## 12. Create and Run Your First Code Cell

In the notebook toolbar, click **+ Code** to create a new code cell.

Enter:

```python
import sys

print("Welcome to SkyNetix Agentic AI Training!")
print("Python executable:", sys.executable)
print("Python version:", sys.version)
```

Click the **Run Cell (▶)** button.

You should see the welcome message, Python version, and executable path.

Verify that the executable path points to the `agentic-ai` Conda environment.

### Useful Notebook Shortcuts

| Action                                 | Shortcut              |
| -------------------------------------- | --------------------- |
| Create a code cell                     | Click `+ Code`        |
| Create a Markdown cell                 | Click `+ Markdown`    |
| Run the current cell                   | `Ctrl + Enter`        |
| Run the cell and move to the next cell | `Shift + Enter`       |
| Insert a cell below                    | Press `Esc`, then `B` |
| Insert a cell above                    | Press `Esc`, then `A` |
| Convert a cell to Markdown             | Press `Esc`, then `M` |
| Convert a cell to Code                 | Press `Esc`, then `Y` |

For the `Esc` shortcuts, press `Esc` first to enter command mode.

## 13. Install and Test python-dotenv

If your notebook reports:

```text
ModuleNotFoundError: No module named 'dotenv'
```

it means the selected Python environment cannot find the `dotenv` module.

The package is named `python-dotenv`, but the Python import is `dotenv`.

In the VS Code terminal, activate your environment and install the package:

```powershell
conda activate agentic-ai
uv pip install python-dotenv
```

Alternatively, install all project dependencies again if `python-dotenv` is already listed in your `requirements.txt`:

```powershell
uv pip install -r requirements.txt
```

After installation:

1. Return to your notebook.
2. Restart the kernel using the **Restart** button.
3. Run the import cell again.

Test the installation:

```python
from dotenv import load_dotenv

load_dotenv()

print("python-dotenv imported successfully!")
```

Expected output:

```text
python-dotenv imported successfully!
```

## 14. Load the .env File from the Project Root

Your `.env` file is located in the project root:

```text
agentic-ai-course/
├── .env
└── 1_foundations/
    └── lab-1.ipynb
```

Because your notebook is inside `1_foundations`, the following code can load `.env` from the project root when the notebook's working directory is `1_foundations`:

```python
from pathlib import Path
from dotenv import load_dotenv

env_path = Path.cwd().parent / ".env"

print("Environment file:", env_path)
print("Environment file exists:", env_path.exists())

load_dotenv(env_path)
```

Expected output:

```text
Environment file exists: True
```

If the file check returns `False`, inspect the notebook's working directory:

```python
from pathlib import Path

print("Current working directory:", Path.cwd())
```

Adjust the path to `.env` based on the displayed directory.

**Important:** `load_dotenv()` loads environment variables from the specified file. It does not validate whether your API keys are genuine or usable.

## 15. Verify Environment Variables Without Revealing API Keys

After loading `.env`, check whether the variables are present without printing their values:

```python
import os

for key in [
    "OPENAI_API_KEY",
    "GOOGLE_API_KEY",
    "ANTHROPIC_API_KEY",
]:
    value = os.getenv(key)
    print(f"{key} configured:", bool(value))
```

A result of `True` means a non-empty value exists. It does not prove that the API key is valid.

If you use placeholder values, replace them with your actual keys before making API requests.

## 16. Verify Installed Dependencies

Check for dependency conflicts:

```powershell
uv pip check
```

If everything is compatible, the output should indicate:

```text
No broken requirements found.
```

You can also test important AI libraries:

```powershell
python -c "import langchain, langgraph, crewai, anthropic, openai; print('Agentic AI packages imported successfully!')"
```

If a package is missing, install the relevant dependency in the active environment.

## 17. Run a Python Program

To run your regular Python application:

```powershell
python main.py
```

To launch JupyterLab from your active environment:

```powershell
jupyter lab
```

## 18. Troubleshooting Common Problems

### Problem 1: ModuleNotFoundError

Example:

```text
ModuleNotFoundError: No module named 'dotenv'
```

Solution:

```powershell
conda activate agentic-ai
uv pip install python-dotenv
```

Restart the notebook kernel and run the cell again.

### Problem 2: The Notebook Uses the Wrong Python Environment

Check the executable from a notebook cell:

```python
import sys

print(sys.executable)
```

If the path does not point to your `agentic-ai` environment, select the correct kernel.

### Problem 3: The Jupyter Server Connection Closes

Try these steps:

1. Save the notebook.
2. Restart the notebook kernel.
3. If necessary, reload VS Code.
4. Confirm that Jupyter and `ipykernel` are installed in the Conda environment.
5. Select the `agentic-ai` kernel again.

### Problem 4: uv Reports Access Denied

Avoid installing into the system Python directory with:

```powershell
uv pip install --system -r requirements.txt
```

Instead, activate your Conda environment and run:

```powershell
conda activate agentic-ai
uv pip install -r requirements.txt
```

### Problem 5: Dependencies Have Conflicts

Run:

```powershell
uv pip check
```

Read the complete error output and identify the conflicting package versions before changing your requirements.

## Important Notes

- Always activate `agentic-ai` before installing packages or running Python programs.
- Use `uv pip install -r requirements.txt` to install dependencies into the active Conda environment.
- Select the `agentic-ai` kernel for notebooks that require these dependencies.
- Restart the notebook kernel after installing packages that were missing.
- Keep API keys in `.env`; never hard-code them into notebooks.
- Ensure `.env` is listed in `.gitignore`.
- Never commit API keys to GitHub.
- If an API key was exposed in a screenshot or repository, revoke it and generate a replacement.
- If dependency installation fails, inspect the complete error message before attempting to reinstall everything.
