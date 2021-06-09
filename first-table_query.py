#========================
# Query Person Database 
#========================

import sqlite3



connection = sqlite3.connect('test_database.db')
cursor = connection.cursor()

query = "SELECT * FROM  People;"
results = cursor.execute(query)
row = results.fetchone()
print(row)