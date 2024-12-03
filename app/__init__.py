# -*- coding: utf-8 -*-

import os
from flask import Flask
from app.config import STATIC_PATH


def create_app():
    _config = os.getenv('FLASK_CONFIG') or 'app.config.DevConfig'
    app = Flask(__name__, static_folder=STATIC_PATH)

    app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
    app.config.from_object(_config)

    return app

