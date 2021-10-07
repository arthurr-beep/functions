import json
import unittest
from project.tests.base import BaseTestCase
from project.services.functions_service import fibonacci, factorial, Ackerman


class TestFunctionsService(BaseTestCase):
    """Test Functions Service Class

    Args:
        TestCase ([type]): [description]
    """

    def test_fibonacci(self):
        """Test Correctness of Fibonacci"""

        response = fibonacci(4)
        self.assertEqual(response, 3)

    def test_factorial(self):
        """Test Correctness of Factorial"""

        response = factorial(4)
        self.assertEqual(response, 24)

    def test_ackerman(self):
        """Test Correctness of Ackerman"""

        response = Ackerman().compute(1, 2)
        self.assertEqual(response, 4)
