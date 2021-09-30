# flake8: noqa

from typing import Any, Dict

from aws_lambda_context import LambdaContext
from mypy_boto3_dynamodb import ServiceResource
from mypy_boto3_s3.client import S3Client
from mypy_boto3_s3.service_resource import S3ServiceResource

LambdaEvent = Dict[str, Any]
LambdaResponse = Dict[str, Any]
S3SdkClient = S3Client
S3SdkResource = S3ServiceResource
DynamoDBSdkClient = ServiceResource
