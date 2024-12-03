#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import create_app

from app.api.apis.main_api import main_bp

API_PREFIX = '/media/'
app = create_app()

app.register_blueprint(main_bp, url_prefix=API_PREFIX + 'main')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=10052,
        debug=False,
    )
