import os
from .settings import BASE_DIR
from loguru import logger


logger.remove(handler_id=None)
log_file = os.path.join(BASE_DIR, "log/file_{time}.log")
logger.add(log_file, backtrace=True, retention="5 min", encoding="utf8")
