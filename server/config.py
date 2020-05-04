from os import environ
class BaseConfig(object):
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True

class AppConfig(BaseConfig):
    DATABASE_DB = 'PMS'
    DATABASE_USER = 'lizard'
    DATABASE_PASSWORD = 'ashrab_shai'
    @property
    def DATABASE_SERVER(self):
        return '192.168.0.29' if 'DB_HOST' not in environ else environ['DB_HOST']
    @property
    def DATABASE_PORT(self):
        return 3306 if 'DB_HOST' not in environ else 42069

