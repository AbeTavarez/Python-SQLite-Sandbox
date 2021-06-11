#=============================================
# Interactive user database 
#=============================================

import sqlite3
from sqlite3.dbapi2 import Cursor
from user_fetch import fetch_user_data

# DB Name
db_name = 'users_database.db'


# Table Schema
sql = """
DROP TABLE IF EXISTS User;
CREATE TABLE User (
    FirstName TEXT,
    LastName TEXT,
    Email TEXT
);"""


# Get user data
def get_user_data():
    firstname = input('Enter first name: ')
    lastname = input('Enter last name: ')
    email = input('Enter email: ')
    return (firstname, lastname, email)



# Create query from user-data
def create_query(data):
    query = (
        "INSERT INTO User Values"
        f"('{data[0]}', '{data[1]}', {data[2]});"
    )
    return query


#==========================MAIN=========================================#
user_data = get_user_data() # gets data from user
print(user_data)
insert_data = create_query(user_data) # creates the data for insertion
print(insert_data)


# Execute database
with sqlite3.connect(db_name) as connection:
    cursor = connection.cursor()
    cursor.executescript(sql)

with sqlite3.connect(db_name) as connection:
    cursor = connection.cursor()
    cursor.execute(insert_data)

q1 = "SELECT * FROM User;"
print(fetch_user_data(db_name, q1))