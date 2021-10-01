import json
from logging import Logger

from ariadne import ObjectType, graphql_sync, make_executable_schema, snake_case_fallback_resolvers
from aws_lambda_context import LambdaContext
from kink import inject

from graphql_spike_jennifer_black.graphql.resolvers import get_search_resolver
from graphql_spike_jennifer_black.types import LambdaEvent, LambdaResponse


@inject
def get_search(event: LambdaEvent, context: LambdaContext, type_defs: str, logging: Logger) -> LambdaResponse:
    logging.info("getting a search with graphql")
    logging.debug(event)
    data = json.loads(event["body"])
    query = ObjectType("Query")
    query.set_field("searchResult", get_search_resolver)
    schema = make_executable_schema(type_defs, query, snake_case_fallback_resolvers)
    success, result = graphql_sync(schema, data, debug=True)
    logging.debug(success)
    logging.debug(result)
    status_code = 200 if success else 400
    return {"statusCode": status_code, "body": json.dumps(result)}
