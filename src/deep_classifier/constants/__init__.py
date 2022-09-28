from pathlib import Path
from datetime import datetime
import os

ROOT_DIR=os.getcwd()
CONFIG_DIR="configs"
CONFIG_FILE_NAME="config.yaml"

CONFIG_FILE_PATH=os.path.join(CONFIG_DIR,CONFIG_FILE_NAME)
PARAMETERS_FILE_PATH=Path("params.yaml")

CURRENT_TIMESTAMP=datetime.now().strftime("%d-%m-%Y_%H-%M-%S")