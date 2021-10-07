from flask.cli import FlaskGroup
import unittest
from project import create_app
import coverage
import logging

COV = coverage.coverage(
    branch=True, include="project/*", omit=["project/tests/*", "project/config.py"]
)
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("test")
def test():
    """
    Runs All Tests
    """
    # print(app.config, file=sys.stderr)
    tests = unittest.TestLoader().discover("project/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command("cov")
def cov():
    """Runs unit tests with coverage"""
    tests = unittest.TestLoader().discover("project/tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print("Coverage Summary")
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


if __name__ == "__main__":
    cli()

else:
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
