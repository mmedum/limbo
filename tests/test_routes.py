from api import app
import unittest


class TestRoutes(unittest.TestCase):

    def test_index_returns_200(self):
        request, response = app.test_client.get('/')
        self.assertEqual(response.status, 200)
