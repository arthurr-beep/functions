import os


class BaseConfig:
    """
    Base Configuration
    """

    TESTING = False
    JSONIFY_PRETTYPRINT_REGULAR = False
    SECRET_KEY = "we_were_born_to_die_so_live_before_death"
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class DevelopmentConfig(BaseConfig):
    """
    Development Configuration
    """

    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """
    Testing Configuration
    """

    TESTING = True
    DEBUG_TB_ENABLED = True
