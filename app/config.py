#!/usr/bin/python
# coding: utf-8

""" This module contains the application configuration.
It uses the configuration on the .env file

"""

import os
from app.services import config


# Grabs the folder where the script runs.
SECRET_KEY = config("SECRET_KEY")

# Enable debug mode.
basedir = os.path.abspath(os.path.dirname(__file__))
