import logging
import os
import sys
from logging import Logger, StreamHandler
from typing import Union

from ariadne import load_schema_from_path
from kink import di


def create_logger(logging_level: Union[int, str] = logging.INFO) -> Logger:
    handler = StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    logger = logging.getLogger(__name__)
    logger.propagate = False
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging_level)

    return logger


di["type_defs"] = lambda _di: load_schema_from_path("graphql_spike_jennifer_black/schema")
di[Logger] = create_logger(os.getenv("LOG_LEVEL", "INFO"))
