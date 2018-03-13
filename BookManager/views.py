# -*- coding: utf-8 -*-

from BookManager import app


@app.route('/')
def index():
    return 'Hello World!'



