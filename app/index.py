#!/usr/bin/python
# coding: utf-8

""" This module is the source of our application,
it is the default page or home page.

"""

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')


@app.route("/", methods=["GET"])
def home():
    """ This function return the home page
    """
    databases = {
        "database 1": ["table 1", "table 2"],
        "database 2": ["table 3", "table 4", "table 5", "table 6"],
    }
    return render_template("home.jinja", databases=databases)


def main():
    """ Main function
    """
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
