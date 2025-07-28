import os
from flask import Flask
from Infrastructure.context import *
from dotenv import load_dotenv

load_dotenv()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    return app


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False


class LocalConfig(Config):
    # Base de datos
    CONTEXT_FACTORY = SQLContext
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_LOCAL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 20
    DEBUG = True
    MAX_OVERFLOW = 0

class DevelopmentConfig(Config):
    # Base de datos
    CONTEXT_FACTORY = SQLContext
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DEV')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 280, 'pool_timeout': 100, 'pool_pre_ping': True}
    DEBUG = True

class ProductionConfig(Config):
    # Base de datos
    CONTEXT_FACTORY = SQLContext
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_PROD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 280, 'pool_timeout': 100, 'pool_pre_ping': True}
    DEBUG = True

config_by_name = dict(
    loc=LocalConfig,
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

ENVIROMMENT_NAME = 'prod'


