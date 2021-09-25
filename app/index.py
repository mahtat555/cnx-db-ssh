#!/usr/bin/python
# coding: utf-8

""" This module is the source of our application,
it is the default page or home page.

"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
def home():
    """ This function return the home page
    """
    return "Hello"


def main():
    """ Main function
    """
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
