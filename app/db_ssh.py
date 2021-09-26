""" This module contains a class that allows us to connect to a remote
MySQL Server using an SSH key, and get some data from the database.

"""

import sshtunnel
import mysql.connector


class DBSSH:
    """ This class allows us to connect to a remote MySQL Server using an
    SSH key, and get some data from the database.

    """

    def __init__(self, ssh_host, ssh_username, ssh_password,
                 ssh_private_key, db_host, db_port, db_username,
                 db_password, db_database=None, ssh_port=22):

        # SSH connexion configuration
        self.__ssh_host = ssh_host
        self.__ssh_port = ssh_port
        self.__ssh_username = ssh_username
        self.__ssh_password = ssh_password
        self.__ssh_private_key = ssh_private_key

        # Database connexion configuration
        self.__db_host = db_host
        self.__db_port = db_port
        self.__db_database = db_database
        self.__db_username = db_username
        self.__db_password = db_password

        # SSH tunnel
        self.__ssh_tunnel = None

        # Database connection
        self.__db_cnx = None

    def connect(self):
        """ Create a connection a remote MySQL Server using an SSH key.

        """

        # SSH connexion configuration
        self.__ssh_tunnel = sshtunnel.SSHTunnelForwarder(
            ssh_address_or_host=(self.__ssh_host, self.__ssh_port),
            ssh_username=self.__ssh_username,
            ssh_password=self.__ssh_password,
            ssh_pkey=self.__ssh_private_key,
            remote_bind_address=(self.__db_host, self.__db_port),
        )

        # Start the server
        self.__ssh_tunnel.start()

        # Database connexion configuration
        self.__db_cnx = mysql.connector.MySQLConnection(
            user=self.__db_username,
            password=self.__db_password,
            host=self.__db_host,
            # database=self.db_database,
            port=self.__ssh_tunnel.local_bind_port
        )

    def execute(self, query):
        """ Send requests to the remote MYSQL server

        """
        cursor = self.__db_cnx.cursor()
        try:
            _ = cursor.execute(query)
        except mysql.connector.Error as err:
            print(f"Something went wrong: {err}")

        return cursor.fetchall()
