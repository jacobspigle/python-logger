import logging
from logger import Logger, severity
from module2 import module2boi

__logger = Logger("logConfig.yaml")

__logger.logMessage(severity.debug, "yoooo there we go")
__logger.logMessage(severity.error, "wait")
__logger.logMessage(severity.critical, "no stop")

module2boi.test()