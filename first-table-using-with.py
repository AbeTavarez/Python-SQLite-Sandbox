import sqlite3

# Creates Users Table
create_table = """
CREATE TABLE Users(
    name TEXT,
    email TEXT,
    departmentID INT
);"""

# Values
insert_values = """
INSERT INTO Users VALUES(
    'eren',
    'eyaeger@paths.com',
    11
);"""

# Execute
with sqlite3.connect("users_database.db") as connection:
    cursor = connection.cursor() # creates cursor

    # Execute SQL Commands
    cursor.execute(create_table)
    cursor.execute(insert_values)
