import json
import yaml
import os
import joblib
from src.ds_edep import main_logger
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any, Union

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    try:
        with open(path, "r", encoding="utf-8") as f:  # Контекстний менеджер + кодування
            content = yaml.safe_load(f)
            return ConfigBox(content)
    except BoxValueError:
        main_logger.info("Config yaml is empty")
    except Exception as e:
        main_logger.info(f"Error: {e}")
        raise e
    
@ensure_annotations
def save_json(path: Path, data: dict | ConfigBox):
    temp_data = data.to_dict() if isinstance(data, ConfigBox) else data
    with open(path, "w", encoding="utf-8") as file:
        json.dump(temp_data, file, indent=4, ensure_ascii=False)
    main_logger.info(f"JSON file saved succesfully to {path}") 
        
@ensure_annotations
def read_json(path: Path) -> ConfigBox:
    with open(path, "r", encoding="utf-8") as file:
        content = json.load(file)
    
    main_logger.info(f"JSON file loaded succesfully from {path}")   
    return ConfigBox(content)

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            main_logger.info(f"created directory at: {path}")
            

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    main_logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    main_logger.info(f"binary file loaded from: {path}")
    return data
