import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files=[
    # ".github/workflows/.gitkeep",
    # f"src/{project_name}/__init__.py",
    # f"src/{project_name}/components/__init__.py",
    # f"src/{project_name}/utils/__init__.py",
    # f"src/{project_name}/utils/common.py",
    # f"src/{project_name}/logging//__init__.py",
    # f"src/{project_name}/config/__init__.py",
    # f"src/{project_name}/config/configuration .py",
    # f"src/{project_name}/pipeline/__init__.py",
    # f"src/{project_name}/entity/__init__.py",
    # f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        # Create directory if it doesn't exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Now handle file creation
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating an empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists or has content")        