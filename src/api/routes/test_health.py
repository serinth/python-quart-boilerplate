import pytest
from unittest import mock
from config import create_app

_app = None

@mock.patch('config.factory.Config')
def _setUp(mock_config):
    global _app
    mock_config.return_value = {}
    app = create_app(mock_config)
    app.app_context().push()
    _app = app


@pytest.mark.asyncio
async def test_returns_status_ok():
    _setUp()
    client = _app.test_client()
    """Should return status OK and HTTP 200 when hitting health endpoint"""
    response = await client.get('/health', follow_redirects=True)
    r = await response.get_json()

    assert 200 == response.status_code
    assert 'OK' == r['status']