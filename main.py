######################################
# Sandbox for basic setup and commands
######################################

from os import close
import sqlite3
from sqlite3.dbapi2 import connect

# creates a DB connection
connection = sqlite3.connect('test_database.db')

# Creates a Cursor
cursor = connection.cursor()

# Creates a Query
query = "SELECT datetime('now', 'localtime');"

# Executing the Query
result = cursor.execute(query)
print(result)

# Fetches the first row of results
row = result.fetchone() # returns a tuple
print(row) 

# Access the time from the tuple
time = row[0] # selects the first item (in this case the only item) in the tuple 
print(time)


# Close DB Connection
connection.close()