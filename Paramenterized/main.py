


import sqlite3
from helper_funcs import get_user_data

data = get_user_data()


player_table_schema = """
DROP TABLE IF EXISTS Player;
CREATE TABLE Player(
    username TEXT,
    name TEXT,
    age INT,
    email TEXT,
    password TEXT
);"""


#
with sqlite3.connect('player_database.db') as connection:
    cursor = connection.cursor()
    # create Player table
    cursor.executescript(player_table_schema)
    # populates Player table
    cursor.execute("INSERT INTO Player VALUES(?,?,?,?,?);", data)
    # query all data from the Player table
    cursor.execute('SELECT * FROM Player')
    rows = cursor.fetchall()
    print(rows)

