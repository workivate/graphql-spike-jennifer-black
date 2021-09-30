import json
from datetime import datetime

from graphql_spike_jennifer_black.types import LambdaContext, LambdaEvent, LambdaResponse


def get_status(event: LambdaEvent, context: LambdaContext) -> LambdaResponse:
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "server_time": datetime.utcnow().isoformat(),
                "status": "healthy",
            }
        ),
    }
