""" This module contains a class that allows us to connect to a remote
MySQL Server using an SSH key, and get some data from the database.

"""

import sshtunnel
import mysql.connector


class CNXDBSSH:
    """ This class allows us to connect to a remote MySQL Server using an
    SSH key, and get some data from the database.

    """

    def __init__(self, ssh_host, ssh_username, ssh_password,
                 ssh_private_key, db_host, db_port, db_username,
                 db_password, ssh_port=22):

        # SSH connexion configuration
        self.__ssh_host = ssh_host
        self.__ssh_port = int(ssh_port)
        self.__ssh_username = ssh_username
        self.__ssh_password = ssh_password
        self.__ssh_private_key = ssh_private_key

        # Database connexion configuration
        self.__db_host = db_host
        self.__db_port = int(db_port)
        self.__db_username = db_username
        self.__db_password = db_password

        # SSH tunnel
        self.__ssh_tunnel = None

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

    def execute(self, query, database=None):
        """ Send requests to the remote MYSQL server

        """

        # Database connexion configuration
        _db_cnx = mysql.connector.MySQLConnection(
            user=self.__db_username,
            password=self.__db_password,
            host=self.__db_host,
            database=database,
            port=self.__ssh_tunnel.local_bind_port
        )

        _db__cursor = _db_cnx.cursor()

        try:
            _db__cursor.execute(query)
        except mysql.connector.Error as err:
            print(f"Something went wrong: {err}")

        result = _db__cursor.fetchall()

        _db_cnx.close()
        _db__cursor.close()

        return result

    def databases(self):
        """ Get the list of databases

        """
        result = self.execute("show databases;")
        return [item[0] for item in result]

    def tables(self, database):
        """ Get the list of tables in a given database

        """
        result = self.execute("SHOW TABLES;", database)
        return [item[0] for item in result]

    def table(self, database_name, table_name):
        """ Get the list of tables in a given database

        """
        # The table fields
        table_description = self.execute(
            f"DESCRIBE {database_name}.{table_name}",
            database_name
        )
        columns = [item[0] for item in table_description]
        # The table data
        rows = self.execute(
            f"SELECT * FROM {database_name}.{table_name};",
            database_name
        )

        return {
            "columns": columns,
            "rows": rows
        }

    def close(self):
        """ Close the SSH connection and MySQL connection

        """
        self.__ssh_tunnel.close()
