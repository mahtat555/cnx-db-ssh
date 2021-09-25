#  Connect to the Database using an SSH key

The purpose of this tool is to **use SSH keys to connect to a remote MySQL Server**

**This project is written with python3.8 +**

## The objectives of the application

1.  This tool allow you to connect to a remote MySQL Server use an SSH key.

2.  Get a list of the tables in a particular database.

3.  Show data for each table from these tables

4. Update and/or delete these tables


## Building

It is better to use the python tool `virtualenv` to build locally:

```sh
$ # Clone the repository from Github
$ git clone https://github.com/mahtat555/conn-db-ssh.git
$ cd conn-db-ssh
$
$ # Create isolated Python environment
$ pip install virtualenv
$ python3 -m venv env
$ source env/bin/activate
$
$ # Install the required libraries
$ pip install -r requirements.txt
$
$ # Start the program
$ cd app
$ python index.py
```