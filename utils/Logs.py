import os
import logging
from config.config_reader import log_cfg
from logging.handlers import TimedRotatingFileHandler

_BaseHome = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

_log_level = eval(log_cfg['log_level'])
_log_path = log_cfg['log_path']
_log_format = log_cfg['log_format']

_log_file = os.path.join(_BaseHome, _log_path, 'log.txt')


def log_init():
    logger = logging.getLogger('main')
    logger.setLevel(level=_log_level)
    formatter = logging.Formatter(_log_format)

    handler = TimedRotatingFileHandler(filename=_log_file, when="M", interval=4, backupCount=30)
    handler.setLevel(_log_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console = logging.StreamHandler()
    console.setLevel(_log_level)
    console.setFormatter(formatter)
    logger.addHandler(console)

