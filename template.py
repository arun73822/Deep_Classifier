import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO,format= "[%(asctime)s]: %(message)s: ")

package_name = "deep_classifier"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/utility/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "research/example_1.ipynb",
    "configs/config.yaml",
    "dvc.yaml",  
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
]

for file_path in list_of_files:
    file_path=Path(file_path)
    file_dir,file_name=os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"creating the directory: {file_dir} for file {file_name} is successfull")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"creating the file: {file_name} is successfull")
    
    else:
        logging.info(f"{file_name} Already file exits ")
