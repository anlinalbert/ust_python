import sqlite3
from pathlib import Path

# Path for better cross-platform compatibility
db_path = Path(r"../sql/Chinook_Sqlite.sqlite")

# Auto closing
with sqlite3.connect(db_path) as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

for table in tables:
    print(table)
