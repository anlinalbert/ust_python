import sqlite3

connection = sqlite3.connect(r"../sql/Chinook_Sqlite.sqlite")
curr = connection.cursor()

curr.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = curr.fetchall()

for table in tables:
    print(table)
