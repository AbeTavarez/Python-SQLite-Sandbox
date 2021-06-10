# ================================================
# Creates database and inserts data using a script
# ================================================
# A SQL Script is a collection of SQL statements separated by semicolons(:)
# That can be run all at the same time.

import sqlite3

# Creating script....
sql = """
DROP TABLE IF EXISTS People;
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
);
INSERTE INTO People VALUES(
    'Eren',
    'Yaeger',
    '33'
);"""


# Executing....
with sqlite3.connect('people_database.db') as connection:
    cursor = connection.cursor()
    cursor.executescript(sql)


