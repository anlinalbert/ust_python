import os
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()
uri = os.getenv("MONGODB_URI")

# Create a client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"), tlsAllowInvalidCertificates=True)

# Send a ping to check if connection successful
try:
    client.admin.command("ping")
    print("Pinged. Connection successful.")

    # Connecting...
    database = client["ust_live_quiz"]
    collection = database["basic_collection_test"]
    document_id = ObjectId("67383929ff9b6251fcbab5f7")

    # Print based on age
    print(pd.DataFrame(collection.find({"age": {"$gt": 20}})))

except Exception as e:
    print(e)
