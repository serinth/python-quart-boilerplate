import pytest
import pytest_asyncio
from pytest_mock import MockerFixture
from config import create_app, Config

@pytest_asyncio.fixture
async def app(mocker: MockerFixture):
    config_mock = mocker.Mock(spec=Config)
    app = create_app(config_mock)
    await app.app_context().push()
    return app


@pytest.mark.asyncio
async def test_returns_status_ok(app):
    client = app.test_client()
    """Should return status OK and HTTP 200 when hitting health endpoint"""
    response = await client.get('/health', follow_redirects=True)
    r = await response.get_json()

    assert 200 == response.status_code
    assert 'OK' == r['status']