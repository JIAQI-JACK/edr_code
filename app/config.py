import logging
import os
from datetime import timedelta


BASE_PATH = os.path.dirname(__file__)

STATIC_PATH = os.path.join(BASE_PATH, "static")


def get_env(key, default):
    return os.environ.get(key, default)


current_env = get_env("ENV_MODE", "PROD").upper()


class BaseConfig(object):
    DEBUG = False
    PROJECT_PATH = os.path.dirname(BASE_PATH)
    RESULT_PATH = os.path.join(PROJECT_PATH, "result")
    LOG_PATH = get_env("LOG_PATH", os.path.join(BASE_PATH, "logs"))
    LOG_FORMAT = "%(asctime)s [%(process)d] - %(levelname)s - %(name)s[%(lineno)s]: %(message)s"
    LOG_LEVEL = logging.DEBUG

    PERMANENT_SESSION_LIFETIME = timedelta(days=1)



class DevConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    SECRET_KEY = b'D\xd9\xc3ZPI\xd57b7\xbb\xf3\xb8.\x06vA\x16\x96*\xbd\xa5\xc8H'


class ProdConfig(BaseConfig):
    LOG_LEVEL = logging.INFO
    SECRET_KEY = b'\xdd$X\x826\xeb\xf4Sj"\x08\x7f=:\xe9\x89\xfb\xaa\x83T\xea\xe0\xc7\x81'


__env_config = {
    "DEV": DevConfig,
    "TEST": TestConfig,
    "PROD": ProdConfig
}

current_config = __env_config.get(current_env)
if current_config is None or not issubclass(current_config, BaseConfig):
    raise KeyError
