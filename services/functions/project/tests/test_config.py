import os
import unittest

from flask import current_app
from flask_testing import TestCase
from project import create_app

app = create_app()


class TestDevConfig(TestCase):
    def create_app(self):
        app.config.from_object("project.config.DevelopmentConfig")
        return app

    def test_app_is_dev(self):
        self.assertTrue(
            app.config["SECRET_KEY"] == "we_were_born_to_die_so_live_before_death"
        )
        self.assertFalse(current_app is None)
        self.assertTrue(app.config["DEBUG_TB_ENABLED"])


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object("project.config.TestingConfig")
        return app

    def test_app_is_testing(self):
        self.assertTrue(
            app.config["SECRET_KEY"] == "we_were_born_to_die_so_live_before_death"
        )
        self.assertTrue(app.config["TESTING"])
        self.assertFalse(app.config["PRESERVE_CONTEXT_ON_EXCEPTION"])
        self.assertTrue(app.config["DEBUG_TB_ENABLED"])


if __name__ == "__main__":
    unittest.main()