import sqlite3

# Creates Users Table
create_table = """
CREATE TABLE Users(
    name TEXT,
    email TEXT,
    departmentID INT
);"""

insert_values = """
INSERT INTO Users VALUES(
    'eren',
    'eyaeger@paths.com',
    01
);"""

