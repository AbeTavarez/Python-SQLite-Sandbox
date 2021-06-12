


import sqlite3
import subprocess
from helper_funcs import get_user_data
from sql_funcs import insert_player_data, fetch_all_players, confirm_admin

cmd = input("""
==================================
Welcome, why are you still here?  :|
1) To insert new record enter (n)
2) To update a record enter (u)
3) fetch all Players (p)
==================================
""")

try:
    if cmd == 'n':
        data = get_user_data()
        insert_player_data(data)
    elif cmd == 'u':
        pass
    elif cmd == 'p':
        fetch_all_players()
    elif cmd == 'admin':
        subprocess.call(confirm_admin())
        
except:
    print('What are you doing? -_-')

else:
    print('Stop playing! (-_-)')
