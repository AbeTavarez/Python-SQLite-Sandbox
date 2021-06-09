import sqlite3
from sqlite3.dbapi2 import connect

connection = sqlite3.connect('test_database.db')

print(type(connection))