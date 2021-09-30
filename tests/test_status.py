from graphql_spike_jennifer_black.status.controllers import get_status


def test_get_status() -> None:
    status = get_status({}, {})

    assert status["statusCode"] == 200
