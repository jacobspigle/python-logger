import logging
from logger import Logger, severity
from module2 import module2boi

__logger = Logger("logConfig.yaml")

__logger.logMessage(severity.debug, "yoooo there we go")
__logger.logMessage(severity.error, "oh shit")
__logger.logMessage(severity.critical, "oh fuckkk")

module2boi.test()

def main():
    print("what the hell")
    __logger.info("Heyo")
    __logger.error("uh-oh")
    __logger.critical("uhhhhhhhhh")