""" This file lets the Python interpreter know that a directory contains
code for a Python module.

"""

from flask import Flask


app = Flask(__name__)
app.config.from_object('app.config')
