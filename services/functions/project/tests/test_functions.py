import json
import unittest
from project.tests.base import BaseTestCase


class TestFunctionsApi(BaseTestCase):
    """Test API for Functions Service

    Args:
        BaseTestCase ([type]): [description]
    """

    def test_fibonacci(self):
        """
        Ensure the route for finonacci behaves as expected
        """
        response = self.client.get("/functions/fibonacci/4h")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn("failed", data["status"])
        self.assertIn("valid integer", data["error"])

    def test_fibonacci_negative(self):
        """
        Ensure the route for finonacci behaves as expected
        """
        response = self.client.get("/functions/fibonacci/-4")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn("failed", data["status"])
        self.assertIn("greater than zero", data["error"])

    def test_factorial(self):
        """
        Ensure the route for factorial behaves as expected
        """
        response = self.client.get("/functions/factorial/4h")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn("failed", data["status"])
        self.assertIn("valid integer", data["error"])

    def test_factorial_negative(self):
        """
        Ensure the route for factorial behaves as expected
        """
        response = self.client.get("/functions/factorial/-4")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn("failed", data["status"])
        self.assertIn("greater than zero", data["error"])

    def test_ackerman(self):
        """
        Ensure the route for ackerman receives two param
        """
        response = self.client.get("/functions/ackerman/4h")
        self.assertEqual(response.status_code, 404)

    def test_ackerman_negative(self):
        """
        Ensure the route for ackerman checks for non-negative
        """
        response = self.client.get("/functions/ackerman/-4/2")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn("failed", data["status"])
        self.assertIn("greater than zero", data["error"])

    def test_ackerman_valid_integer(self):
        """
        Ensure the route for ackerman checks for valid integer
        """
        response = self.client.get("/functions/ackerman/4k/2")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn("failed", data["status"])
        self.assertIn("invalid literal", data["error"])
