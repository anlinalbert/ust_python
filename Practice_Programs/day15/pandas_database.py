import sqlite3
import pandas as pd
from pathlib import Path

db_path = Path(r"../sql/Chinook_Sqlite.sqlite")

with sqlite3.connect(db_path) as connection:
    query = """
    SELECT * FROM Customer LIMIT 10
    """

    customer_data = pd.read_sql_query(query, connection)

    query = """
    SELECT BillingCountry, SUM(Total) as Total FROM Invoice
    GROUP BY BillingCountry
    """

    total = pd.read_sql_query(query, connection)

    query = """
        SELECT *
        FROM Invoice
        """
    new_total = pd.read_sql_query(query, connection)

    new_total = new_total.groupby("BillingCountry")["Total"].sum()
print(new_total)
