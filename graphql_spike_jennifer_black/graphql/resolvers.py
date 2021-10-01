from logging import Logger
from typing import Any

from kink import inject


@inject
def get_search_resolver(obj: Any, info: Any, logging: Logger) -> dict:
    logging.info(info)
    logging.info(obj)
    response = {"success": True, "results": ["It's working so far!"]}
    return response
