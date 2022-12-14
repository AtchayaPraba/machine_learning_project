import yaml
from housing.exception import HousingException
import os, sys
from housing.component import *

def read_yaml_flie (file_path:str) -> dict:
    """
    Read a .yaml file and return the content as dictionary
    file_path: str
    """
    try:
        with open(file_path,"rb") as yaml_file:
             return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e, sys) from e
    