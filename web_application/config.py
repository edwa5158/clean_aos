import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration"""


class ProductionConfig(Config):
    """Production Configuration"""


class DevelopmentConfig(Config):
    """Development Configuration"""


class TestingConfig(Config):
    """Testing Configuration"""

    TESTING = True
