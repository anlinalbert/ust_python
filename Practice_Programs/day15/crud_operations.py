import sqlite3
from pathlib import Path

db_path = Path(r"../sql/Chinook_Sqlite.sqlite")

new_customer = (123, "Ken", "Adams", "UST", "ken.adams@ust", "USA")

with sqlite3.connect(db_path) as connection:
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO Customer(CustomerId, FirstName, LastName, Company, Email, Country)
        VALUES(?, ?, ?, ?, ?, ?)
        """, new_customer
    )

    connection.commit()

print("New customer added.")
