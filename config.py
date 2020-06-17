# all the configurations should be added here
import os


class config(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.environ.get('SECRET_KEY')


class Production(config):
    DEBUG = False
    TESTING = False


class Development(config):
    pass


class Testing(config):
    pass
