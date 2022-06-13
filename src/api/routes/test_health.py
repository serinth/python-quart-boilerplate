import json
import pytest
import unittest
from config import create_app, Config

class BaseTestCase(unittest.TestCase):
    """A base test case"""
    def setUp(self):
        app = create_app(Config())
        app.app_context().push()
        self.app = app.test_client()

    def tearDown(self):
        print("teardown complete")

@pytest.mark.asyncio
class TestHealthEndpoint(BaseTestCase):
    """Test Health Endpoint"""
    def setUp(self):
        super(TestHealthEndpoint, self).setUp()

    async def test_returns_status_ok(self):
        """Should return status OK and HTTP 200 when hitting health endpoint"""
        response = await self.app.get('/metrics/health')
        r = json.dumps(str(response.data))

        self.assertEqual(200, response.status_code)
        self.assertTrue('"status":"OK"', r)