""" This module contains all the services using in the application.

"""

import os
import dotenv


dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)


def config(key):
    """ reads key-value pairs from a .env file.

    """
    return os.environ.get(key)
