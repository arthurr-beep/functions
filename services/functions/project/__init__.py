import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from project.middleware.metrics import Metrics
import logging


# print(app.config, file=sys.stderr)

toolbar = DebugToolbarExtension()


def create_app(script_info=None):
    # create an instance of the app
    app = Flask(__name__)

    app.logger.debug("this is a test")

    # Custom Metrics
    Metrics().app_metrics(app)

    # set configurations
    app_config = os.getenv("APP_SETTINGS")
    app.config.from_object(app_config)

    # set extensions

    toolbar.init_app(app)

    # register blueprints
    from project.api.functions import functions_blueprint

    app.register_blueprint(functions_blueprint)

    # shell context for flask cli
    app.shell_context_processor({"app": app})
    return app
