import sqlite3
################################
# using with to setup connection
################################

from sqlite3.dbapi2 import connect

with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now', 'localtime');"
    results = cursor.execute(query)
    row = results.fetchone()
    time = row[0]


print(time)