import sqlite3
from pathlib import Path

db_path = Path(r"../sql/Chinook_Sqlite.sqlite")

new_customer = (123, "Ken", "Adams", "UST", "ken.adams@ust", "USA")

try:
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()

        # Create
        # cursor.execute(
        #     """
        #     INSERT INTO Customer(CustomerId, FirstName, LastName, Company, Email, Country)
        #     VALUES(?, ?, ?, ?, ?, ?)
        #     """, new_customer
        # )
        # print("New customer added.")

        # Read
        customer = cursor.execute(
            """
            SELECT * FROM Customer
            WHERE CustomerId = 123
            """
        )
        for row in customer:
            print(row)

except sqlite3.Error as e:
    print("Error!")
