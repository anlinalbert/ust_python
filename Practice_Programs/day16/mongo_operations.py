import pandas as pd
from mongodb import MongoClient
from config import MONGODB_URI

connection_string = MONGODB_URI

try:
    client = MongoClient(connection_string)
    print("Connected to MongoDB.")

    db = client["sample_mflix"]

    collection = db["movies"]

    results = collection.find().limit(5)
    print(pd.DataFrame(results))
except Exception as e:
    print(e)
