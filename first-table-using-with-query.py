#========================
# Query Users Database 
#========================

import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect('users_database.db') 
cursor = connection.cursor()

query = "SELECT * FROM Users;"
results = cursor.execute(query)

row = results.fetchone()
print(row)
print(f'Username: {row[0].capitalize()}, Email: {row[1]} with ID: {row[2]}')
