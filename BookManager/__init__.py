# -*- coding: utf-8 -*-

"""
BookManager

ref: http://flask.pocoo.org/docs/0.12/patterns/packages/
1. the Flask application object creation has to be in the __init__.py file. That way each module can import it safely and the __name__ variable will resolve to the correct package.
2. all the view functions (the ones with a route() decorator on top) have to be imported in the __init__.py file. Not the object itself, but the module it is in. Import the view module after the application object is created.
"""

from flask import  Flask

app = Flask("BookManager")

import BookManager.views
