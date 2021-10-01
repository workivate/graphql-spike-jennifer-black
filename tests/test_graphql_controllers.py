# type: ignore

from pathlib import Path
from unittest.mock import patch

from graphql_spike_jennifer_black.graphql.controllers import get_search
from tests.conftest import mock_event


@patch("os.path.abspath")
def test_can_hit_search_endpoint(test_path) -> None:
    event = mock_event
    file_path = Path(__file__)
    test_path.return_value = (
        file_path.resolve().parents[1].joinpath("graphql_spike_jennifer_black/schema/schema.graphql")
    )
    result_dict: dict = get_search(event, context=None)

    assert result_dict["statusCode"] == 200
