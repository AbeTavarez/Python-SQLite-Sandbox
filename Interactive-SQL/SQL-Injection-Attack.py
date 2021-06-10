#=============================================
# Interactive user database 
#=============================================

import sqlite3

# Get user data
def get_user_data():
    firstname = input('Enter first name: ')
    lastname = input('Enter last name: ')
    email = input('Enter email: ')
    return (firstname, lastname, email)

user_data = get_user_data()
# print(user_data)

def create_query(user_data):
    query = (
        "INSERT INTO Users VALUES"
        f"('{user_data[0]}', '{user_data[1]}', {user_data[2]})"
    )
    return query
    