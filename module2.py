import logging
from logger import Logger, severity

logger = Logger.getLogger()

class module2boi():
    def test():
        logger.debug("module2 whaddup")
        logger.error("module2 oh")
        logger.critical("module2 oh no")