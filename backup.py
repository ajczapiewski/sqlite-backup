import sqlite3
import apsw
import time
current_time = time.strftime ("%m.%d.%y %H:%M", time.localtime())
_connection = apsw.Connection('app.db')
connection = sqlite3.connect(_connection)
# Use connection as DB-API 2.0, then "Save-As" like this:
destdb = apsw.Connection('test' + str(current_time) + ".db")
with destdb.backup("main", _connection, "main") as backup:
    while not backup.done:
    	backup.step(100)
