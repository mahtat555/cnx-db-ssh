#!/usr/bin/python
# coding: utf-8

""" This module is the source of our application,
it is the default page or home page.

"""

from flask import render_template

from app import app
from app.cache import databases, tables, cnx_db_ssh


@app.route("/", methods=["GET"])
def home():
    """ This function return the home page

    """
    global databases

    databases = __databases(databases)
    return render_template(
        "home.jinja",
        databases=databases
    )


@app.route("/show/<database_name>/<table_name>", methods=["GET"])
def show(database_name, table_name):
    """ This function return the home page

    """
    global databases

    databases = __databases(databases)
    table = cnx_db_ssh.table(database_name, table_name)
    print(table)
    return render_template(
        "show.jinja",
        databases=databases,
        table=table
    )


def __databases(databases):
    """ Returns the list of databases and for each database returns
    its tables.

    """
    if not databases:
        databases_names = cnx_db_ssh.databases()
        for database_name in databases_names:
            databases[database_name] = cnx_db_ssh.tables(database_name)
    return databases
