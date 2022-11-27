import os
import sqlite3


DB_PATH_UP = '../../lib/db/geo.db'

con = sqlite3.connect(DB_PATH_UP)
cur = con.cursor()


req = "SELECT item_id, code FROM items WHERE gamemode_id = 3"
data = cur.execute(req).fetchall()


def rename(folder, item_id, code):
    try:
        os.rename(f"{folder}/{code}.png", f"{folder}/{item_id}.png")
    except FileExistsError:
        pass
    except FileNotFoundError:
        pass

    
for i in data:
    folder = "fr_depts_logo"
    
    rename(folder, i[0], i[1])
    
    folder = "fr_depts_maps"

    rename(folder, i[0], i[1])


req = "SELECT item_id, code FROM items WHERE gamemode_id = 4"
data = cur.execute(req).fetchall()

for i in data:
    folder = "usa_states_flags"
    
    rename(folder, i[0], i[1])
    
    folder = "usa_states_maps"

    rename(folder, i[0], i[1])


        

