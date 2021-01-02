from loguru import logger


logger.add("log/file_{time}.log", encoding="utf8")
