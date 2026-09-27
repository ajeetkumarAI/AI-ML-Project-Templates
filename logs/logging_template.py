import os
import logging
from datetime import datetime
from config_module import *


def _set_logger(logger_name:str, verbose:int, filename:str,log_dir:str=None,config:dict={}):
    """
    This function intitalizes the logging

    Parameters
    ---------------------------------
    logger_name: a string (class name)
    verbose: level of log (min=0 and max=4)
    filename: name of the file
    log_dir: path to log file

    Return
    ----------------------------
    root_logger
    """
    
    levels = [
        logging.CRITICAL,
        logging.ERROR,
        logging.WARNING,
        logging.INFO,
        logging.DEBUG,
    ]
    if config:
        log_level=config['logging']['root']['level']
    else:
        verbose = 0 if verbose < 0 else verbose
        log_level = levels[min(len(levels) - 1, verbose)]
    log_format = {
        "default": "%(asctime)s - %(levelname)s "
        "- %(name)s::%(funcName)s::"
        "%(lineno)d - %(message)s",
        "simple": "%(levelname)s - %(message)s",
    }
    # current datetime
    timestamp = datetime.now().strftime(r"%Y_%m_%d_%H_%M_%S")

    # define root logger
    root_logger = logging.getLogger(logger_name)
    root_logger.setLevel(log_level)

    # Create console handler
    console_handler = logging.StreamHandler()
    if config:
        console_handler.setLevel(config['logging']['handlers']['console_handler']['level'])
        console_format=config['logging']['handlers']['console_handler']['format']
    else:
        console_handler.setLevel(log_level)
        console_format="default"
        
    console_handler.setFormatter(
        logging.Formatter(log_format[console_format], datefmt="%Y-%m-%d %H:%M:%S")
    )
    root_logger.addHandler(console_handler)
    
    if log_dir is not None:
        # Create file handlers
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
            
        # info logs file handler        
        if config:
            file_handler = logging.FileHandler(
                os.path.join(log_dir, f"{config['logging']['handlers']['file_handler']['filename']}_log_{timestamp}.log")
            )
            file_handler.setLevel(config['logging']['handlers']['file_handler']['level'])
            file_format=config['logging']['handlers']['file_handler']['format']
        else:
            file_handler = logging.FileHandler(
                os.path.join(log_dir, f"{filename}_log_{timestamp}.log")
            )
            file_handler.setLevel(log_level)
            file_format="default"

        file_handler.setFormatter(
            logging.Formatter(log_format[file_format], datefmt="%d-%m-%Y %H:%M:%S")
        )
        root_logger.addHandler(file_handler)
    if config:
        root_logger.propagate=config['logging']['root']['propagate']
    else:
        root_logger.propagate=False
    return root_logger


config = load_config("config_sample.yaml")
_LOGGER = _set_logger(__name__, 3, 'inference',config['core']['log_base_path'],config)
_LOGGER.info('message from auxiliary module')
_LOGGER.error('error message from auxiliary module')
