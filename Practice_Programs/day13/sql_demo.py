import sqlite3

connection = sqlite3.connect(r"../sql/Chinook_Sqlite.sqlite")
curr = connection.cursor()

print(curr)
