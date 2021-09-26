""" This module contains the Globale data or the data cache

"""

from app.services import config
from app.db_ssh import CNXDBSSH

# Used to store database names
databases = {}

# Used to store database names
tables = {}

# SSH connexion configuration
ssh_host = config("SSH_HOST")
ssh_port = config("SSH_PORT")
ssh_username = config("SSH_USERNAME")
ssh_password = config("SSH_PASSWORD")
ssh_private_key = config("SSH_PRIVATE_KEY")

# Database connexion configuration
db_host = config("DB_HOST")
db_port = config("DB_PORT")
db_username = config("DB_USERNAME")
db_password = config("DB_PASSWORD")

# connect to a remote MySQL Server
cnx_db_ssh = CNXDBSSH(
    ssh_host, ssh_username, ssh_password, ssh_private_key, db_host, db_port,
    db_username, db_password, ssh_port
)
cnx_db_ssh.connect()

print("=======================================================================")
