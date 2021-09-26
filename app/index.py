#!/usr/bin/python
# coding: utf-8

""" This module is the source of our application,
it is the default page or home page.

"""

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

# Global data
databases = {
    "database1": ["table1", "table2"],
    "database2": ["table3", "table4", "table5", "table6"],
}

tables = {
    "table1": {
        "columns": ["name", "email", "age"],
        "rows": [
            ["Alice", "alice@gmail.com", 19],
            ["Bob", "bob@gmail.com", 31],
        ]
    }
}

@app.route("/", methods=["GET"])
def home():
    """ This function return the home page
    """
    return render_template("home.jinja", databases=databases)


@app.route("/show/<database>/<int:table>", methods=["GET"])
def show(database, table):
    """ This function return the home page
    """
    table = tables[databases[database][table]]
    return render_template(
        "show.jinja", databases=databases, table=table)


def main():
    """ Main function
    """
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
