from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from deep_classifier import logger
from ensure import ensure_annotations
from typing import Any
import os
import yaml
import json
import joblib

@ensure_annotations
def read_yaml_file(file_path:Path)->ConfigBox:

    """ 
    reads yaml file and returns
    Args:
          file_path(str): path like input
    Raises:
          Value Error: if yaml file is empty
          e: empty file
    Returns:
          ConfigBox: ConfigBox type """
    try:
        with open(file_path,"r") as yaml_file:
            data=yaml.safe_load(yaml_file)
            logger.info(f"yaml_file:{file_path} is loaded successfully")
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path:list,verbose=True):

    """ Creating the list of directories
    Args:
         path(list): list of path of directories
    """
    try:
        for dir_path in path:
            os.makedirs(dir_path,exist_ok=True)
            if verbose:
                logger.info(f"Created the directory at {dir_path}")
    except Exception as e:
        raise e

@ensure_annotations
def load_json(file_path:Path)->ConfigBox:

    """ Loads the json file data
    Args:
         file_path(path): path to json file
    Returns:
            ConfigBox: data as class attributes instead of dict.
    """
    try:
        with open(file_path,"r") as json_file:
            data=json.load(json_file)
            logger.info(f"json_file:{file_path} is loaded successfully")
            return ConfigBox(data)
    except Exception as e:
        raise e

@ensure_annotations
def save_json(path:Path,data:dict):

    """ Save the Json data
    Args:
         path(Path): path of the json file
         data(dict): data to be saved in format of Json
    """
    try:
        with open(path,"w") as f:
            json.dump(data,f,intend=4)
        logger.info(f"json file saved at: {path}")
    except Exception as e:
        raise e

@ensure_annotations
def load_binary_file(file_path:Path)->Any:

    """Loads the Binary file
    Args:
         file_path(Path): path of the binary file
    Returns:
            Any: Object stored in the file
    """
    try:
        data=joblib.load(file_path)
        logger.info(f"binary file loaded from: {file_path}")
        return data
    except Exception as e:
        raise e

@ensure_annotations
def save_binary_file(path:Path,data:Any):
    """Save the binary file
    Args:
         path(Path): path of the binary file
         data(Any): data to be saved as binary
    """
    try:
        joblib.dump(data,path)
        logger.info(f"binary file saved at: {path}")
    except Exception as e:
        raise e

@ensure_annotations
def get_size(path:Path)->str:
    """get size in KB
    Args:
         path(Path): path of the file
    Returns:
            str: size in KB
    """
    try:
        size_in_KB=round(os.path.getsize(path)/1024)
        return f"~{size_in_KB} KB"
    except Exception as e:
        raise e
