import json
from logging import Logger
from typing import Any

from kink import inject

from graphql_spike_jennifer_black.graphql.clients import SearchApiClient
from graphql_spike_jennifer_black.graphql.dto import SearchRequest


@inject
def get_search_resolver(
    obj: Any,
    info: Any,
    query: str,
    logging: Logger,
    search_client: SearchApiClient,
    limit: int = 10,
    cursor: str = None,
) -> dict:
    logging.info(query)
    search_request = SearchRequest(query=query, limit=limit, cursor=None)
    if cursor is not None:
        search_request.cursor = cursor
    json_results = search_client.get_search_results(search_request)
    logging.debug(json_results)
    response = {"success": True, "results": json.dumps(json_results)}
    return response
