#========================================
# creates table and insers data to table
#========================================

import sqlite3

# Creates table named People with 3 attibutes
create_table = """
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
);
"""

# Insert values (person info) into the People's table
insert_values = """
INSERT INTO People VALUES(
    'Abe',
    'Tav',
    28
);
"""
connection = sqlite3.connect('test_database.db')
cursor = connection.cursor()
cursor.execute(create_table)
cursor.execute(insert_values)

connection.commit()
connection.close()


