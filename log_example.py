import logging

fmt = "%(asctime)s %(levelname)s %(lineno)s %(message)s"

logging.basicConfig(level=logging.DEBUG, filename="logging.log", format=fmt)

logging.debug("logging...... debug")
logging.info("logging ..... info")
logging.warn("logging .... warn")
logging.error("logging .... error")
logging.critical("logging .... ciritical")


logger = logging.getLogger("bunyun")
logger.debug("logger ----- debug")
logger.info("hello world")



numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError("Invalid log level: %s " % loglevel)
print("======== numeric_level = ", numeric_level)
logging.basiConfig(loglevel=numeric_level)
