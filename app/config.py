#!/usr/bin/python
# coding: utf-8

""" This module contains the application configuration.
It uses the configuration on the .env file

"""

import os

import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

# Grabs the folder where the script runs.
SECRET_KEY = os.environ.get("SECRET_KEY")

# Enable debug mode.
basedir = os.path.abspath(os.path.dirname(__file__))
