import os
from logging import Logger
from typing import Protocol, runtime_checkable

import requests
from bson import ObjectId
from kink import inject
from requests import RequestException, Response

from graphql_spike_jennifer_black.graphql.dto import SearchRequest


@runtime_checkable
class ISearchApiClient(Protocol):
    def get_denied_listings(self, search_request: SearchRequest) -> Response:
        ...


@inject(alias=ISearchApiClient)
class SearchApiClient(ISearchApiClient):
    def __init__(self, logging: Logger):
        self.search_url = os.environ["SEARCH_API_URL"]
        self.logging = logging

    def get_search_results(self, search_request: SearchRequest) -> Response:
        self.logging.info("Collecting search results")
        try:
            if search_request.limit is None:
                search_request.limit = 10
            query = {
                "limit": search_request.limit,
                "deny_originator": ObjectId(),  # for PoC purposes, TODO: find a way to get this from graphql context
                "deny_type": "COMPANY",  # see above comment
                "query": search_request.query,
            }
            if search_request.cursor is not None:
                query["cursor"] = search_request.cursor
            response = requests.get(f"{self.search_url}/records", params=query)
            return response.json()
        except RequestException as e:
            raise RuntimeError(f"error getting search api results, exception: {e}")
