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

        # Database connection
        self.__db_cnx = None
        self.__db__cursor = None

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
            # database=self.__db_database,
            port=self.__ssh_tunnel.local_bind_port
        )

    def execute(self, query):
        """ Send requests to the remote MYSQL server

        """
        self.__db__cursor = self.__db_cnx.cursor()
        try:
            _ = self.__db__cursor.execute(query)
        except mysql.connector.Error as err:
            print(f"Something went wrong: {err}")

        return self.__db__cursor.fetchall()

    def databases(self):
        """ Get the list of databases

        """
        result = self.execute("show databases;")
        return [item[0] for item in result]

    def tables(self, database):
        """ Get the list of tables in a given database

        """
        self.execute(f"USE {database};")
        result = self.execute("SHOW TABLES;")
        return [item[0] for item in result]

    def table(self, database_name, table_name):
        """ Get the list of tables in a given database

        """
        self.execute(f"USE {database_name};")
        # The table fields
        table_description = self.execute(f"DESCRIBE {table_name}")
        columns = [item[0] for item in table_description]
        # The table data
        rows = self.execute(f"SELECT * FROM {table_name};")

        return {
            "columns": columns,
            "rows": rows
        }

    def close(self):
        """ Close the SSH connection and MySQL connection

        """
        self.__ssh_tunnel.close()
        self.__db_cnx.close()
        self.__db__cursor.close()
