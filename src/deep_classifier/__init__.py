from cmath import log
import os
import sys
import logging
from datetime import datetime
from pathlib import Path

log_dir="logs"
log_file_name=f"log_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}"
log_file_path=Path(os.path.join(log_dir,log_file_name))
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(filename=log_file_path,
                    filemode="w",
                    format="[%(asctime)s:%(levelname)s:%(module)s]:%(message)s",
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler(log_file_path),
                        logging.StreamHandler(sys.stdout)
                    ]
                    )

logger=logging.getLogger("deepclassifierlogger")
