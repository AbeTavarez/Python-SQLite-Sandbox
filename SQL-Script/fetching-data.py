#=======================================
# fetches data from the People database
#=======================================

import sqlite3

query = "SELECT * FROM People"

with sqlite3.connect('people_database.db') as conn:
    cursor = conn.cursor()
    results = cursor.execute(query)
    row = results.fetchone()
print(row)
