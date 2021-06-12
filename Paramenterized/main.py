


import sqlite3
from helper_funs import get_user_data

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

with sqlite3.connect('player_database.db') as connection:
    cursor = connection.cursor()
    #
    cursor.execute(player_table_schema)
