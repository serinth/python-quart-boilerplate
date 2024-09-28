import logging
from config.config import Config

def get_logging_handler() -> logging.StreamHandler:
    formatter = logging.Formatter(fmt='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    return handler

def setup_logger(name: str, config: Config) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if config.debug == True else logging.INFO)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.propagate = False
    logger.addHandler(get_logging_handler())    
    return logger