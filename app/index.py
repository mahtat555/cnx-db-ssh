#!/usr/bin/python
# coding: utf-8

""" This module is the source of our application,
it is the default page or home page.

"""

from flask import render_template

from app import app
from app.cache import databases, tables


@app.route("/", methods=["GET"])
def home():
    """ This function return the home page

    """
    return render_template(
        "home.jinja",
        databases=databases
    )


@app.route("/show/<database>/<int:table>", methods=["GET"])
def show(database, table):
    """ This function return the home page

    """
    table = tables[databases[database][table]]
    return render_template(
        "show.jinja",
        databases=databases,
        table=table
    )
