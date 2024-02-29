import sqlite3
from contextlib import contextmanager

database = './test.sqlite'


@contextmanager
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        yield conn
        conn.close()
    except sqlite3.Error as error:
        raise RuntimeError(f"Failed to create database connection: {error} ")
