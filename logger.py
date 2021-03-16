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

    def __init__(self, configFilePath):
        with open(configFilePath, 'r') as stream:
            config = yaml.load(stream, Loader=yaml.FullLoader)
        logging.config.dictConfig(config)

        self.__logger = logging.getLogger()
    
    def logMessage(self, arg_severity, arg_message, *args, **kwargs):
        self.__logger.log(arg_severity, arg_message, *args, **kwargs)

    @classmethod
    def getLogger(self):
        if self.__logger == None:
            self.__logger = logging.getLogger()

        return self.__logger