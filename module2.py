import logging
from logger import Logger, severity

class module2boi():
    def test():
        logger = Logger.getLogger()

        logger.debug("module2 whaddup")
        logger.error("oh snap")
        logger.critical("oh fuddggeeee")