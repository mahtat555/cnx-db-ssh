""" This module run flask server.

"""

from app import app, index


def main():
    """ Main function
    """
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
