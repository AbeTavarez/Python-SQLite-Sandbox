

import sqlite3


player_table_schema = """
CREATE TABLE Player(
    username TEXT,
    name TEXT,
    age INT,
    email TEXT,
    password TEXT
);"""

# CREATE PLAYER DB
def create_player_db():
    # Create database and create tables
    with sqlite3.connect('player_database.db') as connection:
        cursor = connection.cursor()
        # Create Player Table
        cursor.executescript(player_table_schema)


# INSERT INTO
def insert_player_data(data):
    with sqlite3.connect('player_database.db') as conn:
        c = conn.cursor()
        # populates Player table
        c.execute("INSERT INTO Player VALUES(?,?,?,?,?);", data)




def fetch_all_players():
    with sqlite3.connect('player_database.db') as conn:
        c = conn.cursor()
         # Query all data from the Player table
        c.execute('SELECT * FROM Player')
        rows = c.fetchall()
        print(rows)



def confirm_admin():
    passwd = input('Enter pasword: ')

    if passwd == 'admin':
        admin_cmd = admin_menu()
        if admin_cmd == 'c':
            create_player_db()



def admin_menu():
    cmd = input("""
    ================================
    ============ ADMIN =============
    1) To create database enter (c)

    Enter (q) to quit....
    ================================
    """)
    return cmd

    
        
