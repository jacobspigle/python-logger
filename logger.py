import logging
import logging.config
import yaml
from enum import IntEnum

class severity(IntEnum):
    debug = 10
    info = 20
    warning = 30
    error = 40
    critical = 50

class Logger():
    __logger = None

    def __init__(cls, configFilePath):
        with open(configFilePath, 'r') as stream:
            config = yaml.load(stream, Loader=yaml.FullLoader)
        logging.config.dictConfig(config)

        cls.__logger = logging.getLogger()

    def logMessage(cls, arg_severity, arg_message, *args, **kwargs):
        cls.__logger.log(arg_severity, arg_message, *args, **kwargs)

    @classmethod
    def getLogger(cls):
        logger = logging.getLogger()
        cls.__logger.critical("ayy I did it")
        return logger