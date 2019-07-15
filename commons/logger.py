import abc
import logging
import sys
from colorlog import ColoredFormatter
from .python import PythonCommons

INPUT = 5
logging.addLevelName(INPUT, 'INPUT')

# Configuring logger properties
formatter = ColoredFormatter(
    ("[%(log_color)s%(levelname)-8s%(reset)s] "
     "%(asctime)s - " +
     PythonCommons.LIGHT_BLUE +
     "%(name)s" +
     PythonCommons.NC +
     " - "
     "%(message)s"),
    datefmt=None,
    reset=True,
    log_colors={
        'INFO':     'cyan',
        "INPUT":    'blue',
        'DEBUG':    'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'bold_white,bg_red',
    },
    secondary_log_colors={},
    style='%'
)

ch = logging.StreamHandler()
ch.setFormatter(formatter)


class Logger(abc.ABC):

    @staticmethod
    def info(cls, msg):
        Logger._log(lvl=logging.INFO, cls=cls, msg=msg)

    @staticmethod
    def input(cls, msg):
        Logger._log(lvl=INPUT, cls=cls, msg=msg)

    @staticmethod
    def debug(cls, msg):
        Logger._log(lvl=logging.DEBUG, cls=cls, msg=msg)

    @staticmethod
    def warn(cls, msg):
        Logger._log(lvl=logging.WARN, cls=cls, msg=msg)

    @staticmethod
    def error(cls, msg):
        Logger._log(lvl=logging.ERROR, cls=cls, msg=msg)
        sys.exit()

    @staticmethod
    def critical(cls, msg):
        Logger._log(lvl=logging.CRITICAL, cls=cls, msg=msg)
        sys.exit()

    @staticmethod
    def _log(lvl, cls, msg):
        logger = logging.getLogger(cls.__name__)
        logger.setLevel(lvl)
        logger.addHandler(ch)
        logger.log(level=lvl, msg=msg)
