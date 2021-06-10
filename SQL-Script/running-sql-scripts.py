# A SQL Script is a collection of SQL statements separated by semicolons(:)
# That can be run all at the same time.

import sqlite3

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

