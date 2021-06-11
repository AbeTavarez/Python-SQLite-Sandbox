#=======================================
# fetches data from the Users database
#=======================================

import sqlite3


def fetch_user_data(db, query):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        results = cursor.execute(query)
        print(results)
        row = results.fetchall()
        return row